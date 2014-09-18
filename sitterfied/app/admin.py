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
class ScheduleInline(admin.TabularInline):
    model = Schedule

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
#        BookingInline,
        PhoneInline,
    ]





class ParentAdmin(UserAdmin):
    parent_fieldsets = ('Parent Details',
                        {
                            'fields': (
                                'avatar',
                                'emergency_contact_one_name',
                                'emergency_contact_one_phone',
                                'emergency_contact_two_name',
                                'emergency_contact_two_phone',
                                'promo_code',
                                'sitter_teams',
                                'users_in_network',
                                'friends',
                                'zip',
                                'cell',
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

                           'users_in_network',
                           'friends',



                           )}
                        ),



    add_fieldsets = UserAdmin.add_fieldsets + sitter_fieldsets
    fieldsets = UserAdmin.fieldsets + sitter_fieldsets
    inlines = copy.copy(UserAdmin.inlines) + [ReviewsInline, ScheduleInline,]
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


class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode

    parents = forms.ModelMultipleChoiceField(required=False, help_text='Hold down "Control", or "Command" on a Mac, to select more than one.', queryset=Parent.objects.all())
    bookings = forms.ModelMultipleChoiceField(required=False, help_text='Hold down "Control", or "Command" on a Mac, to select more than one.', queryset=Booking.objects.all())

    def __init__(self, *args, **kwargs):
        super(PromoCodeForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['parents'].initial = self.instance.parent_set.all()
            self.fields['bookings'].initial = self.instance.booking_set.all()

    def save(self, *args, **kwargs):
        instance = super(PromoCodeForm, self).save(commit=False)
        self.fields['parents'].initial.update(promo_code=None)
        self.fields['bookings'].initial.update(promo_code=None)
        self.cleaned_data['parents'].update(promo_code=instance)
        self.cleaned_data['bookings'].update(promo_code=instance)
        return instance


class PromoCodeAdmin(admin.ModelAdmin):
    form = PromoCodeForm

admin.site.register(Parent, ParentAdmin)
admin.site.register(Sitter, SitterAdmin)

admin.site.register(Language)
admin.site.register(OtherService)
admin.site.register(Certification)
admin.site.register(SitterReview)
admin.site.register(Booking, BookingAdmin)

admin.site.register(PromoCode, PromoCodeAdmin)

admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Group)


#TODO: contact and general avaialbilty
