# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-06-07 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('client', '\u043a\u043b\u0438\u0435\u043d\u0442'), ('worker', '\u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a')], default='client', max_length=7),
        ),
    ]
