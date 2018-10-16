# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-16 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_sources_sourceprojection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sources',
            name='jobid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='api.ReplicationJobs'),
        ),
    ]