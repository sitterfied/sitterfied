from django import forms
from django.forms import ModelForm
from models import User
from registration.forms import RegistrationFormUniqueEmail as DjangoRegistrationFormUniqueEmail

from django.utils.translation import ugettext_lazy as _

class RegistrationForm(DjangoRegistrationFormUniqueEmail):
    parent_or_sitter = forms.ChoiceField(widget = forms.RadioSelect,
                                         choices = ([("sitter", "sitter"), ("parent", "parent") ]),  required = True,)


    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']


    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


import mimetypes
from base64 import b64decode
from django.core.files.base import ContentFile
import uuid

from pyuploadcare.dj.forms import ImageField as UploadcareImageField

class AvatarForm(forms.Form):
    avatar = UploadcareImageField()
