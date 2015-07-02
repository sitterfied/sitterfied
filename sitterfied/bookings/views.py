# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.sitters.serializers import SitterSerializer
from sitterfied.utils.views import IdFilterViewset, OutputSerializerMixin


class BookingViewSet(OutputSerializerMixin, IdFilterViewset):
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Booking.objects.select_related('parent').prefetch_related('sitters').all()
    serializer_class = BookingSerializer

    @detail_route(methods=['get'])
    def sitters(self, request, id=None):
        booking = get_object_or_404(Booking, id=id)
        serializer = SitterSerializer(booking.sitters.all(), many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def declined_sitters(self, request, id=None):
        booking = get_object_or_404(Booking, id=id)
        serializer = SitterSerializer(booking.declined_sitters, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def accept_booking(self, request, id=None):
        booking = get_object_or_404(Booking, id=id)
        sitter = request.user.sitter
        booking.accept(sitter)
        serializer = BookingSerializer(booking, context=self.get_serializer_context())
        response = Response(serializer.data)
        return response

    @detail_route(methods=['post'])
    def cancel_booking(self, request, id=None):
        booking = get_object_or_404(Booking, id=id)
        booking.cancel(request.user)
        serializer = BookingSerializer(booking, context=self.get_serializer_context())
        response = Response(serializer.data)
        return response

    @detail_route(methods=['post'])
    def decline_booking(self, request, id=None):
        booking = get_object_or_404(Booking, id=id)
        sitter = request.user.sitter
        booking.decline(sitter)
        serializer = BookingSerializer(booking, context=self.get_serializer_context())
        response = Response(serializer.data)
        return response
