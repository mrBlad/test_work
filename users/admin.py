# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import User


class UserAdmin(admin.ModelAdmin):

    model = User
    extra = 1


admin.site.register(User, UserAdmin)

