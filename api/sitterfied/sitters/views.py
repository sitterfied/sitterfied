# -*- coding: utf-8 -*-
from django.db.models import Q
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.sitters.models import Sitter
from sitterfied.sitters.serializers import SitterSerializer
from sitterfied.utils.views import IdFilterViewset, OutputSerializerMixin


class SitterViewSet(OutputSerializerMixin, IdFilterViewset):
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Sitter.objects \
        .select_related() \
        .prefetch_related(
            'reviews',
            'languages',
            'sitter_groups',
            'friends',
            'certifications',
            'schedule',
            'other_services',
            'bookings',
            'sitter_teams',
            'bookmarks',
            'settings',
        ).all()
    serializer_class = SitterSerializer

    @detail_route(methods=['get'])
    def bookings(self, request, pk=None):
        queryset = Booking.objects \
            .prefetch_related('sitters') \
            .filter(Q(parent=pk) | Q(sitters=pk))
        serializer = BookingSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
