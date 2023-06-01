# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


# file will be uploaded to MEDIA_ROOT/<id>/<filename>
def _user_directory_path(instance, filename):
    print(instance)
    return '{0}/{1}'.format(instance.user.id, filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    birthday = models.DateField(null=True, blank=True)
    middle_name = models.CharField(blank=True, max_length=30, verbose_name='middle name')

    def __str__(self):
        return self.username


class File(models.Model):
    confirm_file = models.FileField(blank=True, upload_to=_user_directory_path)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
