# -*- coding: utf-8 -*-
from django.db import models

from sitterfied.users.models import User


class Parent(User):
    """
    Represents a parent user.

    """
    bookmarks = models.ManyToManyField('Sitter', related_name='bookmarks', blank=True)
    emergency_contact_one_name = models.CharField(max_length=128, blank=True)
    emergency_contact_one_phone = models.CharField(max_length=10, blank=True)
    emergency_contact_two_name = models.CharField(max_length=128, blank=True)
    emergency_contact_two_phone = models.CharField(max_length=10, blank=True)
    sitter_teams = models.ManyToManyField('Sitter', related_name='sitter_teams', blank=True)

    class Meta:
        app_label = 'app'
        verbose_name = 'Parent'
