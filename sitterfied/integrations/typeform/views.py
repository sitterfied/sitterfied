# -*- coding: utf-8 -*-
from copy import copy
from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from sitterfied.parents.models import Parent, SitterTeamMembership
from sitterfied.sitters.models import Sitter
from sitterfied.utils import authentication


def clean_data(data):
    """
    Remove any keys from the dict that are not used.

    """
    ignored_keys = [
        'created',
        'email',
        'Full Name',
        'ID',
        'Submit date',
        'token',
    ]
    for key in ignored_keys:
        data.pop(key, None)

    return data


def get_sitter_names(data):
    """
    Get sitter names from the request data.

    """
    cleaned_data = clean_data(copy(data))
    return [name.split(' ') for name in cleaned_data.values() if name]


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def sitterchoices(request, *args, **kwargs):
    # If there's no email field, we can't do anything so fail fast
    if 'email' not in request.data:
        return Response(
            {'no_email': 'The request must contain an `email` attribute.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    parent_email = request.data.get('email')
    try:
        parent = Parent.objects.get(email=parent_email)
    except Parent.DoesNotExist:
        return Response({
            'parent_not_found': 'No parent with email `%s` could be found.' % parent_email
        }, status=status.HTTP_400_BAD_REQUEST)

    # Get the first and last names of all the sitters, hopefully, this
    # corresponds to the names in the database.
    sitter_names = get_sitter_names(request.data)
    if not sitter_names:
        # If no sitter names were present, than ignore the request
        return Response(
            {'no_sitters_in_request': 'No sitters were specified in the request.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    name = sitter_names.pop(0)

    # Build the database filters for use in retrieving the sitters.
    filters = Q(first_name=name[0], last_name=name[1])
    for name in sitter_names:
        filters |= Q(first_name=name[0], last_name=name[1])

    sitters = Sitter.objects.filter(filters)
    if not sitters:
        return Response({'sitters_not_found': 'No sitters could be found.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a sitter team membership for each sitter in the array, ignore
    # errors
    for sitter in sitters:
        SitterTeamMembership.objects.get_or_create(
            parent=parent,
            sitter=sitter,
            source='typeform:{}'.format(request.data.get('ID', '')),
        )

    return Response(status=status.HTTP_204_NO_CONTENT)
