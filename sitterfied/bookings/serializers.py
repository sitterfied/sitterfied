# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.bookings.models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Booking
