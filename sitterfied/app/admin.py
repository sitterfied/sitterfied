from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *



admin.site.register(ComingSoonInterest)




class SitterUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            # Not sure why UserCreationForm doesn't do this in the first place,
            # or at least test to see if _meta.model is there and if not use User...
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta:
        model = User
        fields = ("username",)

class SitterUserChangeForm(UserChangeForm):
    class Meta:
        model = User

class SitterUserAdmin(UserAdmin):
    form = SitterUserChangeForm
    add_form = SitterUserCreationForm


admin.site.register(User, SitterUserAdmin)
