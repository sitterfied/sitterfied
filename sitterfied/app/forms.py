import re
import datetime
from django import forms
from django.forms import ModelForm
from models import User, Sitter, Parent, Booking

from django.utils.translation import ugettext_lazy as _

from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget

from django.contrib.auth import authenticate
from .models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML#Fieldset, ButtonHolder, Submit




USER_FIELDS =  ["address1", "address2", "city", "state", "zip", "cell", "first_name", "last_name", "email", "avatar"]

class RegistrationForm(ModelForm):
    class Meta:
        model = User

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}),
                                label=_("Password"), )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password (again)"}),
                                label=_("Password (again)"))

    # tos = forms.BooleanField(widget=forms.CheckboxInput,
    #                          label=_(u'I have read and agree to the Terms of Service'),
    #                          error_messages={'required': _("You must agree to the terms to register")})


    def save(self, *args, **kwargs):
        email, password = self.cleaned_data['email'], self.cleaned_data['password1']
        username = (self.cleaned_data['first_name'][0] + self.cleaned_data['last_name']).lower()
        username = re.sub('\W', "", username)
        otherusers = User.objects.filter(username__startswith=username).count()
        username = username + str(otherusers)
        user = super(RegistrationForm, self).save(*args,commit=False, **kwargs)
        user.username = username
        user.set_password(password)
        user.save()
        new_user = authenticate(username=email, password=password)
        return new_user



    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data


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

class ActiveForm(forms.Form):
    active = forms.BooleanField(required=False)


class BookingForm(forms.Form):
    booking = forms.IntegerField()

    def booking_clean(self):
        booking_id = self.cleaned_data['booking']
        booking = Booking.objects.get(pk=booking_id)
        if booking.accepted_sitter:
            raise forms.ValidationError("Someone has already accepted that booking")
        return booking



class AcceptBookingForm(BookingForm):
    def save(self):
        booking = self.cleaned_data['booking']
        sitter = self.cleaned_data['sitter']
        booking.accept(sitter)
        return booking

class DeclineBookingForm(BookingForm):
    def save(self):
        booking = self.cleaned_data['booking']
        sitter = self.cleaned_data['sitter']
        booking.decline(sitter)
        return booking



class SitterRegisterForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super(SitterRegisterForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            if key in ['certifications', "special_needs_exp"]:
                continue
            self.fields[key].required = True


    class Meta:
        model = Sitter
        fields = USER_FIELDS + ['gender', 'dob', "biography", "total_exp",
                                "infant_exp",    "toddler_exp",    "preschool_exp",
                                "school_age_exp",    "pre_teen_exp",    "teen_exp","special_needs_exp",
                                "certifications",  "one_child_min_rate", "one_child_max_rate",
                                "two_child_min_rate",    "two_child_max_rate",
                                "three_child_min_rate",    "three_child_max_rate",
        ]
        widgets = {
            "address1":widgets.TextInput(attrs={"placeholder":"Street Address"}),
            "address2":widgets.TextInput(attrs={"placeholder":"Apt/Suite", "class":"small"}),
            "city":widgets.TextInput(attrs={"placeholder":"City"}),
            "zip":widgets.TextInput(attrs={"placeholder":"Zip Code", "class":"small"}),
            "cell":widgets.TextInput(attrs={"placeholder":"(123) 456-7890"}),
            "first_name":widgets.TextInput(attrs={"placeholder":"First"}),
            "last_name":widgets.TextInput(attrs={"placeholder":"Last"}),
            "email":widgets.TextInput(attrs={"placeholder":"Email"}),
            'gender':widgets.RadioSelect(attrs={'id': 'gender'}),
            'dob':SelectDateWidget(years=list(reversed(range(datetime.date.today().year-100, datetime.date.today().year)))),
            "biography":widgets.Textarea(),
        }






class ParentRegisterForm(RegistrationForm):

    class Meta:
        model = Parent
        fields = USER_FIELDS
