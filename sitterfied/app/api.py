# -*- coding: utf-8 -*-
import django_filters
from django.contrib.auth import logout
from django.db.models import Q

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action, link


from sitterfied.app.forms import AvatarForm, ActiveForm
from sitterfied.children.models import Child
from sitterfied.children.serializers import ChildSerializer
from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
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
from sitterfied.utils.views import IdFilterViewset


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
            .prefetch_related('sitters') \
            .filter(Q(parent=pk) | Q(sitters=pk))
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
