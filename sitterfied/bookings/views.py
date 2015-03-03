# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import action, link
from rest_framework.response import Response

from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingResponseSerializer, BookingSerializer
from sitterfied.sitters.serializers import SitterSerializer
from sitterfied.utils import views


class BookingViewSet(views.SubSerializerViewMixin, views.IdFilterViewset):
    queryset = Booking.objects.all().select_related('parent').prefetch_related('sitters')
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    sub_serializers = {
        'sitters': {
            'serializer': BookingResponseSerializer,
            'to_field': 'sitter',
            'from_field': 'booking',
            'related_name': 'responses',
        }
    }

    @link()
    def sitters(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = SitterSerializer(booking.sitters.all(), many=True)
        return Response(serializer.data)

    @link()
    def declined_sitters(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = SitterSerializer(booking.declined_sitters, many=True)
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
