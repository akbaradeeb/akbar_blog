# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-11 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author_id',
            new_name='author',
        ),
    ]