# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from users.models import User


PENDING = 'pd'
REJECTED = 'rj'
COMPLETE = 'cp'

ORDER_STATUS = [
    (PENDING, 'в ожиданнии'),
    (REJECTED, 'отклонен'),
    (COMPLETE, 'завершен'),
]


def get_choices_label(min_label):

    for item in ORDER_STATUS:
        if min_label == item[0]:
            return item[1]

    return None


class Order(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    user_full_name = models.CharField(max_length=100)
    user_birthday = models.DateField(null=True)
    user_comment = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=ORDER_STATUS, default=PENDING)
    confirm_file = models.CharField(max_length=255)

