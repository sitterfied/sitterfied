# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.serializers import empty

from sitterfied.bookings.models import Booking, BookingResponse
from sitterfied.sitters.models import Sitter


class BookingSerializer(serializers.ModelSerializer):
    """
    Booking serializer.

    """
    accepted = serializers.BooleanField(required=False)
    accepted_sitter = serializers.SerializerMethodField()
    declined_sitters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    sitters = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Sitter.objects.all(),
        required=True,
    )
    url = serializers.HyperlinkedIdentityField(
        lookup_field='id',
        read_only=True,
        view_name='booking-detail')

    def get_accepted_sitter(self, obj):
        if obj and hasattr(obj, 'accepted_sitter'):
            accepted_sitter = getattr(obj, 'accepted_sitter', None)
            if accepted_sitter:
                return accepted_sitter.id

        return None

    def create(self, validated_data):
        sitters = validated_data.pop('sitters', empty)

        instance = super(BookingSerializer, self).create(validated_data)

        if sitters is not empty:
            # For each sitter in the array, create a new booking response.
            for sitter in sitters:
                BookingResponse.objects.create(booking=instance, sitter=sitter)

        return instance

    def update(self, instance, validated_data):
        sitters = validated_data.pop('sitters', empty)

        # Call the super method to get and update the instance.
        instance = super(BookingSerializer, self).update(instance, validated_data)

        # If the sitters array is empty, or not present and this is a PUT,
        # delete all the responses.
        if sitters == [] or (sitters is empty and not self.partial):
            instance.responses.all().delete()
        elif sitters is not empty:
            for sitter in sitters:
                response, created = BookingResponse.objects.get_or_create(
                    booking=instance,
                    sitter=sitter,
                )

            # Delete any response not contained in the siters array
            instance.responses.exclude(sitter__in=sitters).delete()

        return instance

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
            'url',
            'zip',
        )
