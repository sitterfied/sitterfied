# -*- coding: utf-8 -*-
from rest_framework import serializers

from sitterfied.children.models import Child


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
