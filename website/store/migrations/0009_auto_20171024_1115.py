# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 09:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20171021_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customerID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
