# -*- codingg: utf-8 -*-
from rest_framework import serializers

from sitterfied.schedules.models import Schedule


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Schedule
