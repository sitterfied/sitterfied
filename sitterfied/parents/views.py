# -*- coding: utf-8 -*-
from django.db.models import Q
from rest_framework import permissions
from rest_framework.decorators import link
from rest_framework.response import Response

from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.children.models import Child
from sitterfied.children.serializers import ChildSerializer
from sitterfied.parents.models import Parent
from sitterfied.parents.serializers import (
    ParentSerializer, ParentCreateUpdateSerializer, SitterTeamMembershipSerializer)
from sitterfied.sitters.models import Sitter
from sitterfied.sitters.serializers import SitterSerializer
from sitterfied.utils import UNSAFE_HTTP_METHODS
from sitterfied.utils.views import IdFilterViewset, SubSerializerViewMixin


class ParentViewSet(SubSerializerViewMixin, IdFilterViewset):
    queryset = Parent.objects.all() \
        .select_related('settings') \
        .prefetch_related(
            'reviews',
            'languages',
            'settings',
            'sitter_groups',
            'bookings',
            'children',
            'friends',
            'sitter_teams',
            'bookmarks',
        )
    serializer_class = ParentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    sub_serializers = {
        'sitter_teams': {
            'serializer': SitterTeamMembershipSerializer,
            'to_field': 'sitter',
            'from_field': 'parent',
            'related_name': 'sitterteammembership_set',
        }
    }

    def get_serializer_class(self):
        if self.request.method in UNSAFE_HTTP_METHODS:
            return ParentCreateUpdateSerializer
        return ParentSerializer

    @link()
    def children(self, request, pk=None):
        queryset = Child.objects.select_related('parent').prefetch_related('special_needs').filter(parent=pk)
        serializer = ChildSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def sitter_teams(self, request, pk=None):
        queryset = Sitter.objects \
            .prefetch_related(
                'reviews',
                'languages',
                'sitter_teams',
                'sitter_groups',
                'bookmarks',
                'friends',
                'certifications',
                'schedule',
                'other_services',
                'bookings',
                'settings',
            ).filter(sitter_teams=pk)

        serializer = SitterSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @link()
    def bookmarks(self, request, pk=None):
        queryset = Sitter.objects \
            .prefetch_related(
                'reviews',
                'languages',
                'sitter_groups',
                'friends',
                'certifications',
                'schedule',
                'other_services',
                'bookings',
                'bookmarks',
                'sitter_teams',
                'settings',
            ).filter(bookmarks=pk)

        serializer = SitterSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def bookings(self, request, pk=None):
        queryset = Booking.objects \
            .select_related('parent') \
            .prefetch_related('sitters') \
            .filter(Q(parent=pk) | Q(sitters=pk))

        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)
