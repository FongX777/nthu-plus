# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_comment', '0011_comment_custom_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]
