# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from users.models import User


class ProfileModelTest(TestCase):

    def test_profile_model_create(self):

        user1 = User.objects.create(
            username='test1',
            password='12345678',
            last_name='Any',
            first_name='Name1',
            birthday=date.today(),
            confirm_file='/any/path1/'
        )

        user2 = User.objects.create(
            username='test2',
            password='12345678',
            last_name='Any',
            first_name='Name2',
            birthday=date.today(),
            confirm_file='/any/path2/'
        )

        user1.save()

        user2.save()

        all_profile = User.objects.all()

        self.assertEqual(all_profile[0], user1)

        self.assertEqual(all_profile[1], user2)
