# -*- coding: utf-8 -*-
from rest_framework import serializers


from sitterfied.utils.models import Certification, Group, Language, OtherService, SpecialNeed


class CertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certification


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language


class OtherServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = OtherService


class SpecialNeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialNeed
