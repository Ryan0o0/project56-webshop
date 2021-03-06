# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20171030_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='imageLink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='language',
            field=models.CharField(default='Engels', max_length=25),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='type',
            field=models.CharField(default='Comic', max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='prodPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
