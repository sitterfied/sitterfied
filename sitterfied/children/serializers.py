# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.children.models import Child


class ChildSerializer(serializers.ModelSerializer):
    # Allow legacy datetime formats
    dob = serializers.DateField(input_formats=[
        'iso-8601',
        '%Y-%m-%dT%H:%M:%S.%fZ',
    ])

    class Meta:
        model = Child
