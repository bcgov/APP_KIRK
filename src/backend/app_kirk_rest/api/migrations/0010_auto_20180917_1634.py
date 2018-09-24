# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-17 23:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180914_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformers',
            name='whoCreated',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercreated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transformers',
            name='whoUpdated',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userupdated', to=settings.AUTH_USER_MODEL),
        ),
    ]
