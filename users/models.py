# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


# file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
def _user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    confirm_file = models.FileField(blank=True, upload_to=_user_directory_path)
