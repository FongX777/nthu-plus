# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
