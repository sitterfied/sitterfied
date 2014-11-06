# -*- coding: utf-8 -*-
from django.contrib import admin

from sitterfied.bookings.models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_filter = ('booking_status',)
    list_per_page = 25
    ordering = ('start_date_time',)
    search_fields = ('name', 'slug',)


admin.site.register(Booking, BookingAdmin)
