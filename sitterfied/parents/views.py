# -*- coding: utf-8 -*-
from django.db.models import Q
from rest_framework import permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.children.models import Child
from sitterfied.children.serializers import ChildSerializer
from sitterfied.parents.models import Parent
from sitterfied.parents.serializers import ParentSerializer, ParentCreateUpdateSerializer
from sitterfied.sitters.models import Sitter
from sitterfied.sitters.serializers import SitterSerializer
from sitterfied.utils import UNSAFE_HTTP_METHODS
from sitterfied.utils.views import IdFilterViewset, OutputSerializerMixin


class ParentViewSet(OutputSerializerMixin, IdFilterViewset):
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
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

    def get_serializer_class(self):
        if self.request.method in UNSAFE_HTTP_METHODS:
            return ParentCreateUpdateSerializer
        return ParentSerializer

    @detail_route(methods=['get'])
    def children(self, request, pk=None):
        queryset = Child.objects.select_related('parent').prefetch_related('special_needs').filter(parent=pk)
        serializer = ChildSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'])
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

        serializer = SitterSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'])
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

        serializer = SitterSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def bookings(self, request, pk=None):
        queryset = Booking.objects \
            .select_related('parent') \
            .prefetch_related('sitters') \
            .filter(Q(parent=pk) | Q(sitters=pk))

        serializer = BookingSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def sitters(self, request, id=None):
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
            ).filter(sitter_teams=id)

        serializer = SitterSerializer(queryset, many=True, context=self.get_serializer_context());
        return Response(serializer.data);


class FriendsViewSet(OutputSerializerMixin, IdFilterViewset):
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Parent.objects \
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
        ).all()
    serializer_class = ParentSerializer
    def get_queryset(self):
        qs = self.queryset
        if 'parents_id' in self.kwargs:
            qs = qs.filter(friends=self.kwargs.get('parents_id'))
        return qs

    @list_route(methods=['get'])
    def sitters(self, request, parents_id=None):
        friends = Parent.objects.filter(friends=parents_id)
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
            ).filter(sitter_teams=friends)

        serializer = SitterSerializer(queryset, many=True, context=self.get_serializer_context())

        return Response(serializer.data)
