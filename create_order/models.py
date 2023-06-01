# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from users.models import User, File


class Order(models.Model):
    ORDER_STATUS = [
        ('0', 'pending'),
        ('1', 'rejected'),
        ('2', 'complete'),
    ]

    user_id = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    user_full_name = models.CharField(max_length=90, blank=True)
    user_birthday = models.DateField(null=True, blank=True)
    user_comment = models.CharField(max_length=255, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(blank=True)
    status = models.CharField(max_length=2, choices=ORDER_STATUS)
    confirm_file = models.ForeignKey(
        File,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
