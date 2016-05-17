# -*- coding: utf-8 -*-
import re

from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm, widgets
from django.forms.models import BaseInlineFormSet
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from pyuploadcare.dj.forms import ImageField as UploadcareImageField

from sitterfied.children.models import Child
from sitterfied.bookings.models import Booking
from sitterfied.parents.models import Parent
from sitterfied.sitters.models import Sitter
from sitterfied.users.models import User
from sitterfied.users.utils import get_valid_username
from sitterfied.utils import time


USER_FIELDS =  ["address1", "address2", "city", "state", "zip", "cell", "first_name", "last_name", "email", "avatar", "tos"]

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        exclude = ()

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}),
                                label=_("Password"), )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password (again)"}),
                                label=_("Password (again)"),)

    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_(u'I have read and agree to the Terms of Service.'),
                             error_messages={'required': _('You must agree to the terms to register')})


    def save(self, *args, **kwargs):
        email, password = self.cleaned_data['email'], self.cleaned_data['password1']
        username = get_valid_username(email.split('@')[0])

        user = super(RegistrationForm, self).save(*args,commit=False, **kwargs)
        user.username = username
        user.set_password(password)
        user.save()
        self.save_m2m()
        new_user = authenticate(username=email, password=password)
        return new_user



    def clean_password1(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data['password1']

    def clean_password2(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data['password2']


    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']




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
            if key in ["certifications",
                       "special_needs_exp",
                       "infant_exp",
                       "toddler_exp",
                       "preschool_exp",
                       "school_age_exp",
                       "pre_teen_exp",
                       "teen_exp",
                       "address2"]:
                continue
            self.fields[key].required = True

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob.year > time.now().year - 18:
            raise forms.ValidationError("You are too young to register!")
        return dob

    def clean_infant_exp(self):
        dob = self.cleaned_data.get('infant_exp')
        if not dob:
            return 0
        return dob

    def clean_toddler_exp(self):
        dob = self.cleaned_data.get('toddler_exp')
        if not dob:
            return 0
        return dob
    def clean_preschool_exp(self):
        dob = self.cleaned_data.get('preschool_exp')
        if not dob:
            return 0
        return dob
    def clean_school_age_exp(self):
        dob = self.cleaned_data.get('school_age_exp')
        if not dob:
            return 0
        return dob
    def clean_pre_teen_exp(self):
        dob = self.cleaned_data.get('pre_teen_exp')
        if not dob:
            return 0
        return dob
    def clean_teen_exp(self):
        dob = self.cleaned_data.get('teen_exp')
        if not dob:
            return 0
        return dob
    def clean_biography(self):
        bio = self.cleaned_data.get('biography')
        return bio

    class Meta:
        model = Sitter
        fields = USER_FIELDS + ['gender', 'dob', "biography", "total_exp",
                                "infant_exp",    "toddler_exp",    "preschool_exp",
                                "school_age_exp",    "pre_teen_exp",    "teen_exp","special_needs_exp",
                                "certifications",  "one_child_min_rate", "one_child_max_rate",
                                "two_child_min_rate",    "two_child_max_rate",
                                "three_child_min_rate",    "three_child_max_rate",
        ]
        rate_prompt = "Amount in Dollars"
        exp_prompt = "Number of Years"
        widgets = {
            "address1":widgets.TextInput(attrs={"placeholder":"Street Address", "class": "large"}),
            "address2":widgets.TextInput(attrs={"placeholder":"Apt/Suite", "class":"small"}),
            "city":widgets.TextInput(attrs={"placeholder":"City"}),
            "state": widgets.Select(attrs={"class": "extra-small"}),
            "zip":widgets.TextInput(attrs={"placeholder":"Zip Code", "class":"small"}),
            "cell":widgets.TextInput(attrs={"placeholder":"555-555-5555"}),
            "first_name":widgets.TextInput(attrs={"placeholder":"First"}),
            "last_name":widgets.TextInput(attrs={"placeholder":"Last"}),
            "email":widgets.TextInput(attrs={"placeholder":"Email", "class": "large"}),
            'gender':widgets.RadioSelect(attrs={'id': 'gender'}),
            'dob':SelectDateWidget(years=list(reversed(range(time.now().year-100, time.now().year + 1)))),
            "biography":widgets.Textarea(),
            "one_child_min_rate": widgets.TextInput(attrs={"placeholder": rate_prompt}),
            "one_child_max_rate": widgets.TextInput(attrs={"placeholder": rate_prompt}),
            "two_child_min_rate": widgets.TextInput(attrs={"placeholder": rate_prompt}),
            "two_child_max_rate": widgets.TextInput(attrs={"placeholder": rate_prompt}),
            "three_child_min_rate": widgets.TextInput(attrs={"placeholder": rate_prompt}),
            "three_child_max_rate": widgets.TextInput(attrs={"placeholder": rate_prompt}),
            "total_exp": widgets.TextInput(attrs={"placeholder": exp_prompt}),
            "infant_exp": widgets.TextInput(attrs={"placeholder": exp_prompt}),
            "toddler_exp": widgets.TextInput(attrs={"placeholder": exp_prompt}),
            "preschool_exp": widgets.TextInput(attrs={"placeholder": exp_prompt}),
            "school_age_exp": widgets.TextInput(attrs={"placeholder": exp_prompt}),
            "pre_teen_exp": widgets.TextInput(attrs={"placeholder": exp_prompt}),
            "teen_exp": widgets.TextInput(attrs={"placeholder": exp_prompt})
        }


class GroupsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["sitter_groups"]


class ParentRegisterForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super(ParentRegisterForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            if key in ["address2","sitter_groups"]:
                self.fields[key].required = False
                continue
            self.fields[key].required = True

    class Meta:
        model = Parent
        fields = USER_FIELDS + ['sitter_groups']
        widgets = {
            "address1":widgets.TextInput(attrs={"placeholder":"Street Address", "class": "large"}),
            "address2":widgets.TextInput(attrs={"placeholder":"Apt/Suite", "class":"small"}),
            "city":widgets.TextInput(attrs={"placeholder":"City"}),
            "state": widgets.Select(attrs={"class": "extra-small"}),
            "zip":widgets.TextInput(attrs={"placeholder":"Zip Code", "class":"small"}),
            "cell":widgets.TextInput(attrs={"placeholder": "555-555-5555"}),
            "first_name":widgets.TextInput(attrs={"placeholder":"First"}),
            "last_name":widgets.TextInput(attrs={"placeholder":"Last"}),
            "email":widgets.TextInput(attrs={"placeholder":"Email", "class": "large"})
        }


class RequiredFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

class ChildForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["dob"].required = True

    class Meta:
        model = Child
        fields = ('name', 'dob', 'school', 'special_needs')
        widgets = {
            "name":widgets.TextInput(attrs={"placeholder":"Name", "class":"left"}),
            'dob':SelectDateWidget(years=list(reversed(range(time.now().year-50, time.now().year + 1)))),
            "school":widgets.TextInput(attrs={"placeholder":"School (if applicable)", "class":"long"}),
            "special_needs": widgets.SelectMultiple(attrs={"placeholder":"Special needs"}),
        }
