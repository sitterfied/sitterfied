# -*- coding: utf-8 -*-
import django_filters
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import get_object_or_404

from drf_ujson.renderers import UJSONRenderer
from rest_framework import viewsets, permissions
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import action, link


from sitterfied.app.forms import AvatarForm, ActiveForm
from sitterfied.children.models import Child
from sitterfied.children.serializers import ChildSerializer
from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.parents.models import Parent
from sitterfied.parents.serializers import ParentSerializer
from sitterfied.schedules.models import Schedule
from sitterfied.schedules.serializers import ScheduleSerializer
from sitterfied.sitters.models import Sitter, SitterReview
from sitterfied.sitters.serializers import ReviewSerializer, SitterSerializer
from sitterfied.users.models import Settings, User
from sitterfied.users.serializers import SettingsSerializer, UserSerializer
from sitterfied.utils.models import Certification, Group, Language, OtherService, SpecialNeed
from sitterfied.utils.serializers import (
    CertificationSerializer,
    GroupSerializer,
    LanguageSerializer,
    OtherServiceSerializer,
    SpecialNeedSerializer
)


class IdFilterViewset(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, UJSONRenderer)

    def get_queryset(self):
        queryset = super(IdFilterViewset, self).get_queryset()
        if 'id' in self.request.GET:
            ids = self.request.GET.get('id')
            ids = ids.split(",")
            queryset = queryset.filter(id__in=ids)
        return queryset


class UserViewSet(IdFilterViewset):
    queryset = User.objects.all().prefetch_related(
        'languages',
        'sitter_groups',
        'sitter',
        'parent',
        'friends',
        'settings',
    ).all()

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('friends',)

    @link()
    def bookings(self, request, pk=None):
        queryset = Booking.objects.filter(Q(parent=pk) | Q(sitters=pk))
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    @action()
    def avatar_upload(self, request, pk=None):
        form = AvatarForm(request.POST)
        user = request.user

        if not form.is_valid():
            return Response(status=400)

        user.avatar = form.cleaned_data['avatar']
        user.save()

        response = Response(data={'avatar': user.avatar.cdn_url})
        return response

    @action()
    def active(self, request, pk=None):
        form = ActiveForm(request.POST)
        user = request.user

        if not form.is_valid():
            return Response(status=400)

        user.is_active = form.cleaned_data['active']
        user.save()
        logout(request)
        return Response({})

    @link()
    def reviews(self, request, pk=None):
        queryset = SitterReview.objects.filter(Q(parent_id=pk) | Q(sitter_id=pk))
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def languages(self, request, pk=None):
        queryset = Language.objects.filter(users=pk)
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def users_in_network(self, request, pk=None):
        queryset = User.objects.filter(users_in_network=pk)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def friends(self, request, pk=None):
        queryset = User.objects \
            .select_related('settings') \
            .prefetch_related(
                'friends',
                'languages',
                'sitter_groups',
                'parent',
                'sitter',
            ).filter(friends=pk)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class SitterViewSet(IdFilterViewset):
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
        )
    serializer_class = SitterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @link()
    def bookings(self, request, pk=None):
        queryset = Booking.objects \
            .prefetch_related('sitters', 'declined_sitters',) \
            .filter(Q(parent=pk) | Q(sitters=pk))
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)


class ParentViewSet(IdFilterViewset):
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

        serializer = SitterSerializer(queryset, many=True)
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
            .prefetch_related(
                'sitters',
                'declined_sitters',
            ).filter(Q(parent=pk) | Q(sitters=pk))

        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)


class GroupFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type="icontains")

    class Meta:
        model = Group
        fields = ('name',)


class GroupViewSet(IdFilterViewset):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter


class CertificationViewSet(IdFilterViewset):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = (permissions.AllowAny,)


class OtherServiceViewSet(IdFilterViewset):
    queryset = OtherService.objects.all()
    serializer_class = OtherServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SettingsViewSet(IdFilterViewset):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ScheduleViewSet(IdFilterViewset):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewViewSet(IdFilterViewset):
    queryset = SitterReview.objects.all().select_related('parent', 'sitter')
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookingViewSet(IdFilterViewset):
    queryset = Booking.objects.all().select_related('parent').prefetch_related('sitters', 'declined_sitters')
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @link()
    def sitters(self, request, pk=None):
        queryset = Sitter.objects.filter(bookings=pk)
        serializer = SitterSerializer(queryset, many=True)
        return Response(serializer.data)

    @link()
    def declined_sitters(self, request, pk=None):
        queryset = Sitter.objects.filter(declined_bookings=pk)
        serializer = SitterSerializer(queryset, many=True)
        return Response(serializer.data)

    @action()
    def accept_booking(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)
        sitter = request.user.sitter
        booking.accept(sitter)
        serializer = BookingSerializer(booking)
        response = Response(serializer.data)
        return response

    @action()
    def cancel_booking(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)
        booking.cancel(request.user)
        serializer = BookingSerializer(booking)
        response = Response(serializer.data)
        return response

    @action()
    def decline_booking(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)
        sitter = request.user.sitter
        booking.decline(sitter)
        serializer = BookingSerializer(booking)
        response = Response(serializer.data)
        return response


class LanguageViewSet(IdFilterViewset):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SpecialNeedViewSet(IdFilterViewset):
    queryset = SpecialNeed.objects.all()
    serializer_class = SpecialNeedSerializer


class ChildrenViewSet(IdFilterViewset):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('parent', 'school', 'special_needs')
