# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-12 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190311_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default=b' ', upload_to=b'images/'),
        ),
    ]