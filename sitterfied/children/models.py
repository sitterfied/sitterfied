# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel


class Child(TimeStampedModel):
    """
    Child model

    """
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now)
    name = models.CharField(max_length=50, blank=True, default='')
    parent = models.ForeignKey('Parent', related_name='children')
    school = models.CharField(max_length=50, blank=True, default="")
    special_needs = models.ManyToManyField('SpecialNeed', blank=True)

    class Meta:
        app_label = 'app'
        verbose_name_plural = 'children'
