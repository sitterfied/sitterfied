# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.parents.models import Parent, SitterTeamMembership
from sitterfied.users.serializers import default_fields


class ParentSerializer(serializers.ModelSerializer):
    avatar = serializers.Field(source='avatar_url')
    parent_or_sitter = serializers.Field(source='is_parent_or_sitter')
    sitter_teams = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Parent
        fields = sorted(default_fields + (
            'bookings',
            'bookmarks',
            'cell',
            'children',
            'emergency_contact_one_name',
            'emergency_contact_one_phone',
            'emergency_contact_two_name',
            'emergency_contact_two_phone',
            'parent_or_sitter',
            'reviews',
            'sitter_teams',
        ))
        read_only_fields = (
            'date_joined',
            'last_login',
        )


class ParentCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer used when creating or updating a Parent

    """
    class Meta:
        model = Parent
        fields = (
            'address1',
            'address2',
            'avatar',
            'bookings',
            'bookmarks',
            'cell',
            'children',
            'city',
            'email',
            'emergency_contact_one_name',
            'emergency_contact_one_phone',
            'emergency_contact_two_name',
            'emergency_contact_two_phone',
            'facebook_id',
            'facebook_token',
            'friends',
            'first_name',
            'languages',
            'last_name',
            'reviews',
            'sitter_groups',
            'state',
            'username',
            'zip',
        )


class SitterTeamMembershipSerializer(serializers.ModelSerializer):
    """
    Creates and updates sitter team memberships for a parent resource.

    """
    sitter = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = SitterTeamMembership
        fields = ('sitter',)
