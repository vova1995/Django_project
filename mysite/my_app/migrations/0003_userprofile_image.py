# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-08 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=0, upload_to='app_images'),
            preserve_default=False,
        ),
    ]