# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.bookings.models import Booking, BookingResponse


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking


class BookingResponseSerializer(serializers.ModelSerializer):
    """
    Creates and updates booking responses for a booking resource.

    """
    sitter = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = BookingResponse
        fields = ('sitter',)
