# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.db.models import Q
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from sitterfied.app.forms import AvatarForm, ActiveForm
from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.sitters.models import SitterReview
from sitterfied.sitters.serializers import ReviewSerializer
from sitterfied.users.models import User
from sitterfied.users.permissions import IsStaffOrSelf
from sitterfied.users.serializers import UserSerializer
from sitterfied.utils.models import Language
from sitterfied.utils.serializers import LanguageSerializer
from sitterfied.utils.views import IdFilterViewset


class UserViewSet(IdFilterViewset):
    filter_fields = ('friends',)
    permission_classes = (IsStaffOrSelf,)
    queryset = User.objects.all().prefetch_related(
        'languages',
        'sitter_groups',
        'sitter',
        'parent',
        'friends',
        'settings',
    ).all()
    serializer_class = UserSerializer

    @detail_route(methods=['get'], permission_classes=(permissions.IsAuthenticated, IsStaffOrSelf,))
    def bookings(self, request, pk=None):
        queryset = Booking.objects.filter(Q(parent=pk) | Q(sitters=pk))
        serializer = BookingSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['post'], permission_classes=(permissions.IsAuthenticated, IsStaffOrSelf,))
    def avatar_upload(self, request, pk=None):
        form = AvatarForm(request.POST)
        user = request.user

        if not form.is_valid():
            return Response(status=400)

        user.avatar = form.cleaned_data['avatar']
        user.save()

        response = Response(data={'avatar': user.avatar.cdn_url})
        return response

    @detail_route(methods=['post'], permission_classes=(permissions.IsAuthenticated, IsStaffOrSelf,))
    def active(self, request, pk=None):
        form = ActiveForm(request.POST)
        user = request.user

        if not form.is_valid():
            return Response(status=400)

        user.is_active = form.cleaned_data['active']
        user.save()
        logout(request)
        return Response({})

    @detail_route(methods=['get'], permission_classes=(permissions.IsAuthenticated, IsStaffOrSelf,))
    def reviews(self, request, pk=None):
        queryset = SitterReview.objects.filter(Q(parent_id=pk) | Q(sitter_id=pk))
        serializer = ReviewSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'], permission_classes=(permissions.IsAuthenticated, IsStaffOrSelf,))
    def languages(self, request, pk=None):
        queryset = Language.objects.filter(users=pk)
        serializer = LanguageSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'], permission_classes=(permissions.IsAuthenticated, IsStaffOrSelf,))
    def users_in_network(self, request, pk=None):
        queryset = User.objects.filter(users_in_network=pk)
        serializer = UserSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'], permission_classes=(permissions.IsAuthenticated, IsStaffOrSelf,))
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
        serializer = UserSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
