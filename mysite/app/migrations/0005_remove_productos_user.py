# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 04:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_productos_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='user',
        ),
    ]
