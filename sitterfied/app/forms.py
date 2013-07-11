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

class AvatarForm(forms.Form):
    avatar = forms.CharField()
    def clean_avatar(self):
        mime_data, avatarb64 = self.cleaned_data['avatar'].split(';')
        avatarb64 = avatarb64.split(',')[1]
        mime_data = mime_data.split(':')[1]

        extensions = mimetypes.guess_all_extensions(mime_data)
        avatar_data = b64decode(avatarb64)

        filename = str(uuid.uuid4())
        filename = filename + extensions[0]

        avatar = ContentFile(avatar_data, filename)

        return avatar
