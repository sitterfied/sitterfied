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

    class Meta:
        model = User
        fields = ("username",)

class SitterUserChangeForm(UserChangeForm):
    class Meta:
        model = User

class EmailSettingsInline(admin.TabularInline):
    model = EmailSettings

class MobileSettingsInline(admin.TabularInline):
    model = MobileSettings


class PhoneInline(admin.TabularInline):
    model = Phone

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
    form = SitterUserChangeForm
    add_form = SitterUserCreationForm
    inlines = [
        MobileSettingsInline,
        EmailSettingsInline,
        AddressInline,
        BookingInline,
        PhoneInline,
    ]


class ParentAdmin(UserAdmin):
    inlines = copy.copy(UserAdmin.inlines) + [SittersReviewedInline, ChildInline]

class SitterAdmin(UserAdmin):
    inlines = copy.copy(UserAdmin.inlines) + [ReviewsInline]


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


#TODO: contact and general avaialbilty
