# -*- coding: utf-8 -*-
from django.contrib import admin

from sitterfied.utils.models import Certification, Group, Language, OtherService, SpecialNeed


admin.site.register(Certification)
admin.site.register(Group)
admin.site.register(Language)
admin.site.register(OtherService)
admin.site.register(SpecialNeed)
