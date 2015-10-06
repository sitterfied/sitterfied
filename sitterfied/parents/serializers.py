# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.fields import empty

from sitterfied.parents.models import Parent, SitterTeamMembership
from sitterfied.sitters.models import Sitter
from sitterfied.users.serializers import default_fields


class ParentSerializer(serializers.ModelSerializer):
    avatar = serializers.ReadOnlyField(source='avatar_url')
    parent_or_sitter = serializers.ReadOnlyField(source='is_parent_or_sitter')
    sitter_teams = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )
    url = serializers.HyperlinkedIdentityField(
        lookup_field='id',
        read_only=True,
        view_name='parent-detail',
    )

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
            'url',
        ))
        read_only_fields = (
            'date_joined',
            'last_login',
        )


class ParentCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer used when creating or updating a Parent

    """
    sitter_teams = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Sitter.objects.all(),
        required=False
    )

    def create(self, validated_data):
        sitter_teams = validated_data.pop('sitter_teams', empty)

        instance = super(ParentCreateUpdateSerializer, self).create(validated_data)

        if sitter_teams is not empty:
            for sitter in sitter_teams:
                SitterTeamMembership.objects.create(parent=instance, sitter=sitter)

        return instance

    def update(self, instance, validated_data):
        sitter_teams = validated_data.pop('sitter_teams', empty)

        if sitter_teams == [] or (sitter_teams is empty and not self.partial):
            instance.sitterteammembership_set.all().delete()
        elif sitter_teams is not empty:
            for sitter in sitter_teams:
                team_membership, created = SitterTeamMembership.objects.get_or_create(
                    parent=instance,
                    sitter=sitter,
                )

            # Delete any response not contained in the siter_teams array
            instance.sitterteammembership_set.exclude(sitter__in=sitter_teams).delete()

        return super(ParentCreateUpdateSerializer, self).update(instance, validated_data)

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
            'id',
            'languages',
            'last_name',
            'reviews',
            'sitter_groups',
            'sitter_teams',
            'state',
            'username',
            'zip',
        )
        extra_kwargs = {
            'bookings': {'required': False},
            'children': {'required': False},
            'reviews': {'required': False},
        }
