# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.bookings.models import Booking, BookingResponse


class BookingSerializer(serializers.ModelSerializer):
    """
    Booking serializer.

    """
    accepted = serializers.BooleanField(required=False)
    accepted_sitter = serializers.SerializerMethodField('get_id')
    declined_sitters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def get_id(self, obj):
        if obj and hasattr(obj, 'accepted_sitter'):
            accepted_sitter = getattr(obj, 'accepted_sitter', None)
            if accepted_sitter:
                return accepted_sitter.id

        return None

    class Meta:
        model = Booking
        fields = (
            'accepted',
            'accepted_sitter',
            'address1',
            'address2',
            'booking_status',
            'booking_type',
            'canceled',
            'created',
            'city',
            'declined_sitters',
            'emergency_phone',
            'id',
            'modified',
            'notes',
            'num_children',
            'overnight',
            'parent',
            'rate',
            'respond_by',
            'start_date_time',
            'state',
            'sitters',
            'stop_date_time',
            'zip',
        )


class BookingResponseSerializer(serializers.ModelSerializer):
    """
    Creates and updates booking responses for a booking resource.

    """
    sitter = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = BookingResponse
        fields = ('sitter',)
