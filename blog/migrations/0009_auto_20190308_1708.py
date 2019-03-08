# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-08 11:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20190308_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.AddField(
            model_name='blog',
            name='author_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
