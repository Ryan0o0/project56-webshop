# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 10:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Customers',
        ),
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
        migrations.RenameModel(
            old_name='WhishList',
            new_name='WishList',
        ),
    ]