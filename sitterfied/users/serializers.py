# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.users.models import Settings, User


default_fields = (
    'avatar',
    'address1',
    'address2',
    'cell',
    'city',
    'date_joined',
    'email',
    'facebook_id',
    'facebook_token',
    'friends',
    'first_name',
    'id',
    'languages',
    'last_login',
    'last_name',
    'settings',
    'sitter_groups',
    'state',
    'url',
    'username',
    'zip',
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.Field(source='avatar_url')
    parent_or_sitter = serializers.Field(source='is_parent_or_sitter')

    class Meta:
        model = User
        fields = default_fields + ('parent_or_sitter',)


class SettingsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Settings
