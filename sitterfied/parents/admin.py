# -*- coding: utf-8 -*-
import copy

from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm

from sitterfied.children.models import Child
from sitterfied.parents.models import Parent, SitterTeamMembership
from sitterfied.sitters.models import SitterReview
from sitterfied.users.admin import UserAdmin, UserCreationForm


class ParentChangeForm(UserChangeForm):

    class Meta:
        model = Parent
        exclude = ()


class ParentCreationForm(UserCreationForm):

    class Meta:
        model = Parent
        exclude = ()


class ChildInline(admin.StackedInline):
    model = Child


class SitterReviewsInline(admin.StackedInline):
    model = SitterReview


class SitterTeamInline(admin.StackedInline):
    model = SitterTeamMembership


class ParentAdmin(UserAdmin):
    parent_fieldsets = ('Parent Details', {
        'fields': (
            'avatar',
            'emergency_contact_one_name',
            'emergency_contact_one_phone',
            'emergency_contact_two_name',
            'emergency_contact_two_phone',
            'users_in_network',
            'friends',
            'zip',
            'cell',
            'sitter_groups',
        )
    }),

    add_fieldsets = UserAdmin.add_fieldsets + parent_fieldsets
    add_form = ParentCreationForm
    fieldsets = UserAdmin.fieldsets + parent_fieldsets
    form = ParentChangeForm
    inlines = copy.copy(UserAdmin.inlines) + (ChildInline, SitterReviewsInline, SitterTeamInline,)


admin.site.register(Parent, ParentAdmin)
