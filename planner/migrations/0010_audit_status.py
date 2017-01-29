# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0009_audit'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete')], default='pending', max_length=8),
        ),
    ]
