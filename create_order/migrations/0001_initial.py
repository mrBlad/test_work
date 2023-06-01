# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-06-01 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_full_name', models.CharField(blank=True, max_length=90)),
                ('user_birthday', models.DateField(blank=True, null=True)),
                ('user_comment', models.CharField(blank=True, max_length=255)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_finish', models.DateTimeField(blank=True)),
                ('status', models.CharField(choices=[('0', 'pending'), ('1', 'rejected'), ('2', 'complete')], max_length=2)),
            ],
        ),
    ]
