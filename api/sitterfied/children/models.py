# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Child(TimeStampedModel):
    """
    Child model

    """
    dob = models.DateField(blank=False)
    name = models.CharField(max_length=50, blank=True, default='')
    parent = models.ForeignKey('Parent', related_name='children')
    school = models.CharField(max_length=50, blank=True, default="")
    special_needs = models.ManyToManyField('SpecialNeed', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'app'
        verbose_name_plural = 'children'
