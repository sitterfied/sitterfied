import copy

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

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




class SitterCreationForm(SitterUserCreationForm):
    class Meta:
        model = Sitter

class ParentCreationForm(SitterUserCreationForm):
    class Meta:
        model = Parent


class SitterChangeForm(UserChangeForm):
    class Meta:
        model = Sitter

class ParentChangeForm(UserChangeForm):
    class Meta:
        model = Parent



class SettingsInline(admin.TabularInline):
    model = Settings

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0
class AddressInline(admin.TabularInline):
    model = Address

class ChildInline(admin.StackedInline):
    model = Child

class SittersReviewedInline(admin.StackedInline):
    model = SitterReview

class ReviewsInline(admin.StackedInline):
    model = SitterReview

class ContactInline(admin.TabularInline):
    model = Contact

class BookingInline(admin.StackedInline):
    model = Booking


class UserAdmin(DjangoUserAdmin):
    inlines = [
        SettingsInline,
        AddressInline,
        BookingInline,
        PhoneInline,
    ]





class ParentAdmin(UserAdmin):
    parent_fieldsets = ('Parent Details',
                        {
            'fields': (
                'emergency_contact',
                'physician_contact',
                'parking_area',
                'parking_for_sitter',
                'fave_sitters',
                'parents_in_network',
                'sitters_in_network',
                'sitter_groups',
                )}

                        ),



    add_fieldsets = UserAdmin.add_fieldsets + parent_fieldsets
    fieldsets = UserAdmin.fieldsets + parent_fieldsets




    inlines = copy.copy(UserAdmin.inlines) + [SittersReviewedInline, ChildInline]
    form = ParentChangeForm
    add_form = ParentCreationForm


class SitterAdmin(UserAdmin):
    sitter_fieldsets = ('Sitter Details', {
            'fields': (    'biography',
                           'id_verified',
                           'live_zip',
                           'work_zip',
                           'dob',
                           'smoker',
                           'will_transport',
                           'total_exp',
                           'infant_exp',
                           'toddler_exp',
                           'preschool_exp',
                           'school_age_exp',
                           'pre_teen_exp',
                           'teen_exp',

                           'highest_education',
                           'last_school',
                           'current_student',

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
                           )}
                        ),



    add_fieldsets = UserAdmin.add_fieldsets + sitter_fieldsets
    fieldsets = UserAdmin.fieldsets + sitter_fieldsets
    inlines = copy.copy(UserAdmin.inlines) + [ReviewsInline]
    form = SitterChangeForm
    add_form = SitterCreationForm


class BookingAdmin(admin.ModelAdmin):
    list_per_page = 25
    search_fields = ('name', 'slug',)
    ordering = ('start_date_time',)
    list_filter = ('booking_status',)

    # prepopulated_fields = {'slug': ('name',)}
    # exclude = ('actions', 'creator')
    # list_display = ('name', 'slug', 'active', 'over',)
    # list_filter = ('over', 'active',)


admin.site.register(Parent, ParentAdmin)
admin.site.register(Sitter, SitterAdmin)

admin.site.register(Language)
admin.site.register(SitterReview)
admin.site.register(Booking, BookingAdmin)

admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Group)


#TODO: contact and general avaialbilty
