# -*- coding: utf-8 -*-
import django_filters

from rest_framework import permissions

from sitterfied.schedules.models import Schedule
from sitterfied.schedules.serializers import ScheduleSerializer
from sitterfied.sitters.models import SitterReview
from sitterfied.sitters.serializers import ReviewSerializer
from sitterfied.users.models import Settings
from sitterfied.users.serializers import SettingsSerializer
from sitterfied.utils.models import Certification, Group, Language, OtherService, SpecialNeed
from sitterfied.utils.serializers import (
    CertificationSerializer,
    GroupSerializer,
    LanguageSerializer,
    OtherServiceSerializer,
    SpecialNeedSerializer
)
from sitterfied.utils.views import IdFilterViewset


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
