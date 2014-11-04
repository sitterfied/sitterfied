# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.parents.models import Parent
from sitterfied.users.serializers import default_fields


class ParentSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.Field(source='avatar_url')
    parent_or_sitter = serializers.Field(source='is_parent_or_sitter')

    class Meta:
        model = Parent
        fields = default_fields + (
            'emergency_contact_one_name',
            'emergency_contact_one_phone',
            'emergency_contact_two_name',
            'emergency_contact_two_phone',
            'reviews',
            'bookings',
            'children',
            'bookmarks',
            'sitter_teams',
            'parent_or_sitter',
        )

