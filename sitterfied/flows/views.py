# -*- coding: utf-8 -*-
import re
import random

from datetime import datetime
from delorean import Delorean
from django.db.models import Count, Q
from parsedatetime import Calendar
from rest_framework import permissions, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from sitterfied.bookings.models import Booking, BookingResponse
from sitterfied.flows.serializers import TextItInWebhookSerializer
from sitterfied.parents.models import Parent
from sitterfied.sitters.models import Sitter
from sitterfied.utils import authentication
from sitterfied.utils.time import get_time_zone_for_zip, get_today

calendar = Calendar()

TIER_1_SITTER_TEAM = 1
TIER_2_FRIENDS_WITH_SITTER = 2
TIER_3_NO_SITTERS_NO_FRIENDS = 3


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def booking_requests(request, *args, **kwargs):
    """
    Handle a "find" request. This is a request where a parent has sent in a text
    along the lines of "find me a sitter today from 5pm-10pm". The text is passed
    through the natural language parser to get start and end timestamps. If the
    message is understood, a 200 response is returned along with data about the
    requested booking.

    """

    data = {
        'is_valid': False,
    }

    serializer = TextItInWebhookSerializer(data=request.data)
    if not serializer.is_valid():
        data.update({
            'reason': 'bad_data',
            'details': serializer.errors,
        })
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    # Ensure that a user exists with the given cellphone number
    if not Parent.objects.filter(cell=serializer.validated_data.get('phone')).exists():
        data.update({'reason': 'no_user'})
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    # Attempt to parse the request into a date range
    text = serializer.validated_data.get('text')
    start, end, type = calendar.evalRanges(text, get_today().timetuple())
    if type != 2:  # 2, parsed as a time
        data.update({'reason': 'invalid_date_range'})
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    start_dt = datetime(*start[:7])
    end_dt = datetime(*end[:7])
    data = {
        'is_valid': True,
        'start_date': '{dt:%a}, {dt:%b} {dt.day}'.format(dt=start_dt),
        'start_time': '{dt:%l}:{dt.minute:02}{dt:%P}'.format(dt=start_dt).strip(),
        'end_date': '{dt:%b} {dt.day}'.format(dt=end_dt),
        'end_time': '{dt:%l}:{dt.minute:02}{dt:%P}'.format(dt=end_dt).strip(),
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def booking_tier(request, *args, **kwargs):
    serializer = TextItInWebhookSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    text = serializer.validated_data.get('text', '')
    response_pattern = r'(yes|yeah|yup|y)'

    result = re.search(response_pattern, text, re.I | re.S)
    if result is None or len(result.groups()) == 0:
        return Response({'detail': 'Response not understood.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        parent = Parent.objects \
            .prefetch_related('sitter_teams', 'friends') \
            .annotate(num_children=Count('children')) \
            .get(cell=serializer.validated_data.get('phone'))
    except Parent.DoesNotExist as exc:
        return Response(str(exc), status=status.HTTP_400_BAD_REQUEST)

    tier, num_sitters = _get_sitter_tier(parent)
    book_friends_sitters = request.query_params.get('tier', None)
    if tier == TIER_1_SITTER_TEAM or book_friends_sitters == TIER_2_FRIENDS_WITH_SITTER:
        # A user can run through this flow multiple times and the
        # array of values will contain all of the user's texts so we
        # need to get the most recent text that requests a time.
        time_values = [
            value for value in serializer.validated_data.get('values')
            if value.get('label') == 'is_valid' and value.get('text') is not None
        ]
        sorted_values = sorted(time_values, key=lambda k: k['time'], reverse=True)
        time_value = sorted_values[0]

        # Parse out the start and end datetimes for the job request.
        # These values will be in UTC time.
        start, end, type = calendar.evalRanges(time_value.get('text'), get_today().timetuple())
        start_dt = datetime(*start[:7])
        end_dt = datetime(*end[:7])

        # Now shift the values to UTC
        timezone = get_time_zone_for_zip(parent.zip)
        utc_start = Delorean(start_dt, timezone=timezone).shift('UTC').datetime
        utc_end = Delorean(end_dt, timezone=timezone).shift('UTC').datetime

        # Create a booking request if the parent is tier 1
        booking = Booking(
            address1=parent.address1,
            address2=parent.address2,
            booking_status=Booking.BOOKING_STATUS_PENDING,
            booking_type=Booking.BOOKING_TYPE_JOB,
            city=parent.city,
            num_children=parent.num_children,
            parent=parent,
            start_date_time=utc_start,
            state=parent.state,
            stop_date_time=utc_end,
            zip=parent.zip,
        )
        booking.save(send_notifications=False)
        # The parent does not receive a notification at this point as
        # the textit in flow will provide the response.

        sitters = parent.sitter_teams.all() if tier == TIER_1_SITTER_TEAM else _get_friends_sitters(parent)
        for sitter in sitters:
            # Notifications will automatically be sent to sitters
            BookingResponse.objects.create(booking=booking, sitter=sitter)

    data = {
        'tier': tier,
        'num_sitters': num_sitters,
    }
    return Response(data, status=status.HTTP_200_OK)


def _get_sitter_tier(parent):
    """
    Determine the tier of the parent's request.

    Tier 1 means the parent has a sitter team.

    Tier 2 means the parent has friends with sitters.

    Tier 3 means the parent has no sitter team and no friends with sitters.

    """
    # If a parent has a sitter team, return tier 1
    num_sitters = parent.sitter_teams.count()
    if num_sitters > 0:
        return (TIER_1_SITTER_TEAM, num_sitters)

    # If a parent has friends with sitters, return tier 2
    friends_sitters = parent.friends.filter(
        parent__isnull=False,
        parent__sitter_teams__isnull=False
    ).aggregate(
        num_sitters=Count('parent__sitter_teams')
    )

    num_sitters = friends_sitters.get('num_sitters')
    if num_sitters > 0:
        return (TIER_2_FRIENDS_WITH_SITTER, num_sitters)

    # If a parent has no sitter team and no friends with sitters,
    # return tier 3
    return (TIER_3_NO_SITTERS_NO_FRIENDS, 0)


def _get_friends_sitters(parent, count=5):
    """
    Get a random sample of recommended or rehired sitters.

    """
    # Retrieve all sitters from friends sitter teams.
    friends_sitters = Sitter.objects.filter(
        friends__in=parent.friends.filter(parent__isnull=False, parent__sitter_teams__isnull=False)
    ).distinct().exclude(sitter_teams=parent)

    # Retrieve the sitters that have been marked as would rehire or recommended.
    top_sitters = friends_sitters.filter(Q(reviews__rehire=True) | Q(reviews__recommended=True))

    # Return up to 5 random sitters from the top sitters list
    return random.sample(top_sitters, count)
