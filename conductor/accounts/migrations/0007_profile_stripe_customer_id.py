# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-20 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0006_profile_postal_code")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="stripe_customer_id",
            field=models.CharField(default="", max_length=32),
            preserve_default=False,
        )
    ]
