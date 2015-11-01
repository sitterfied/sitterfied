# -*- coding: utf-8 -*-
from django import forms
from django.core import validators
from django.db.models import fields
from django.forms import widgets


class CaseInsensitiveTextField(fields.TextField):
    """
    Provides a case insensitive text field in the db.

    By default, the created field will have a unique constraint on it.

    """
    def __init__(self, *args, **kwargs):
        kwargs['unique'] = kwargs.get('unique', True)
        super(CaseInsensitiveTextField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        if connection.vendor == 'sqlite':
            return 'text collate nocase'
        return 'citext'

    def deconstruct(self):
        name, path, args, kwargs = super(CaseInsensitiveTextField, self).deconstruct()
        kwargs['unique'] = self.unique
        return name, path, args, kwargs


class CaseInsensitiveCharField(CaseInsensitiveTextField):
    """
    Provides a case insensitive char field in the db.

    By default, the created field will have a unique constraint on it.

    """
    def formfield(self, **kwargs):
        kwargs['widget'] = widgets.TextInput
        return super(CaseInsensitiveCharField, self).formfield(**kwargs)


class CaseInsensitiveEmailField(CaseInsensitiveTextField):
    default_validators = [validators.validate_email]
    description = 'Email address'

    def __init__(self, *args, **kwargs):
        # max_length=254 to be compliant with RFCs 3696 and 5321
        kwargs['max_length'] = kwargs.get('max_length', 254)
        super(CaseInsensitiveEmailField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CaseInsensitiveEmailField, self).deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # As with CharField, this will cause email validation to be performed
        # twice.
        defaults = {
            'form_class': forms.EmailField,
        }
        defaults.update(kwargs)
        return super(CaseInsensitiveEmailField, self).formfield(**defaults)
