# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20171024_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customers',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customers',
            name='surname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customers',
            name='telephone',
            field=models.CharField(default='', max_length=12),
        ),
    ]
