# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.db import models
from model_utils.models import TimeStampedModel

from sitterfied.users.models import User


class Parent(User):
    """
    Represents a parent user.

    """
    bookmarks = models.ManyToManyField('Sitter', related_name='bookmarks', blank=True)
    cell = models.CharField(max_length=17, blank=True, unique=True, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{10,15}$',
            message='Phone number must be entered in the format: "+9999999999". Up to 15 digits allowed.')],
        null=True
    )
    emergency_contact_one_name = models.CharField(max_length=128, blank=True)
    emergency_contact_one_phone = models.CharField(max_length=10, blank=True)
    emergency_contact_two_name = models.CharField(max_length=128, blank=True)
    emergency_contact_two_phone = models.CharField(max_length=10, blank=True)
    sitter_teams = models.ManyToManyField(
        'Sitter', related_name='sitter_teams', through='SitterTeamMembership', blank=True)

    class Meta:
        app_label = 'app'
        verbose_name = 'Parent'


class SitterTeamMembership(TimeStampedModel):
    parent = models.ForeignKey('Parent')
    sitter = models.ForeignKey('Sitter')

    def __unicode__(self):
        return '{} is a member of {}\'s sitter team'.format(self.sitter, self.parent)

    class Meta:
        app_label = 'app'
        db_table = 'app_parent_sitter_teams'
        unique_together = (('parent', 'sitter'))
