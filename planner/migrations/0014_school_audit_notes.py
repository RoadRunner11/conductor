# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0013_auto_20170220_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='audit_notes',
            field=models.TextField(blank=True, help_text='Notes to make performing audits easier', null=True),
        ),
    ]
