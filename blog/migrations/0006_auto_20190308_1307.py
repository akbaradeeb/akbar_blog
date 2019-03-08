# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-08 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190305_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name=b'url'),
        ),
    ]
