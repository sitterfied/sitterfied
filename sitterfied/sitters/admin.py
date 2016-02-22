# -*- coding: utf-8 -*-
import copy

from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm

from sitterfied.schedules.models import Schedule
from sitterfied.sitters.models import Sitter, SitterReview
from sitterfied.users.admin import UserAdmin, UserCreationForm


class SitterChangeForm(UserChangeForm):

    class Meta:
        model = Sitter
        exclude = ()


class SitterCreationForm(UserCreationForm):

    class Meta:
        model = Sitter
        exclude = ()


class ScheduleInline(admin.TabularInline):
    model = Schedule


class ReviewsInline(admin.TabularInline):
    model = SitterReview


class SitterAdmin(UserAdmin):
    sitter_fieldsets = ('Sitter Details', {
        'fields': (
            'biography',
            'id_verified',
            'dob',
            'cell',
            'zip',
            'smoker',
            'will_transport',
            'total_exp',
            'infant_exp',
            'toddler_exp',
            'preschool_exp',
            'school_age_exp',
            'pre_teen_exp',
            'teen_exp',
            'avatar',
            'highest_education',
            'last_school',
            'current_student',
            'travel_distance',
            'other_services',
            'one_child_min_rate',
            'one_child_max_rate',
            'two_child_min_rate',
            'two_child_max_rate',
            'three_child_min_rate',
            'three_child_max_rate',
            'smokers_ok',
            'dogs_ok',
            'cats_ok',
            'other_animals_ok',
            # 'users_in_network',
            # 'friends',
        )
    }),

    add_fiedsets = UserAdmin.add_fieldsets + sitter_fieldsets
    add_form = SitterCreationForm
    fieldsets = UserAdmin.fieldsets + sitter_fieldsets
    form = SitterChangeForm
    inlines = copy.copy(UserAdmin.inlines) + (ReviewsInline, ScheduleInline,)


admin.site.register(Sitter, SitterAdmin)
admin.site.register(SitterReview)
