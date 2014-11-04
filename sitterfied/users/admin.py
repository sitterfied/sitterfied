# -*- coding: utf-8 -*-
from django.contrib.admin import TabularInline
from django.contrib.auth import admin, forms
from django.forms import ValidationError

from sitterfied.users.models import Settings


class SettingsInline(TabularInline):
    model = Settings


class UserCreationForm(forms.UserCreationForm):

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username

        return ValidationError(self.error_messages['duplicate_username'])


class UserAdmin(admin.UserAdmin):
    inlines = (SettingsInline,)
