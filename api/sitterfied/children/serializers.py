# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.children.models import Child


class ChildSerializer(serializers.ModelSerializer):
    # Allow legacy datetime formats
    dob = serializers.DateField(input_formats=[
        'iso-8601',
        '%Y-%m-%dT%H:%M:%S.%fZ',
    ])
    url = serializers.HyperlinkedIdentityField(
        lookup_field='id',
        read_only=True,
        view_name='child-detail',
    )

    class Meta:
        model = Child
        fields = (
            'dob',
            'id',
            'created',
            'modified',
            'name',
            'parent',
            'school',
            'special_needs',
            'url',
        )
