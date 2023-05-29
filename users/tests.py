# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from users.models import Profile


class ProfileModelTest(TestCase):

    def test_profile_model_create(self):

        profile = Profile.objects.create(
            user=User.objects.create_user(username="test1", password="123456"),
            full_name='Any Name',
            birthday=date.today(),
            confirm_file=''
        )

        profile.save()

        all_profile = Profile.objects.all()

        self.assertEqual(all_profile[0], profile)
