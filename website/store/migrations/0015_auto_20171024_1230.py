# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20171024_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='isRegistered',
            field=models.BooleanField(),
        ),
    ]