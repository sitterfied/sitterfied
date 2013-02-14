from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *



admin.site.register(ComingSoonInterest)

admin.site.register(User, UserAdmin)
