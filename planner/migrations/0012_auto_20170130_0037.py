# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0011_auto_20170129_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='milestone',
            name='category',
            field=models.CharField(choices=[('ED', 'Early Decision'), ('ED1', 'Early Decision 1'), ('ED2', 'Early Decision 2'), ('EA', 'Early Action'), ('RD', 'Regular Decision')], default='RD', max_length=8),
        ),
        migrations.AddField(
            model_name='milestone',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planner.School'),
            preserve_default=False,
        ),
    ]
