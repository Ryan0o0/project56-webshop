# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=25)),
                ('postalcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=12)),
                ('isRegistered', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderNum', models.IntegerField(primary_key=True, serialize=False)),
                ('orderDate', models.DateField()),
                ('orderStatus', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('orderNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('totalPages', models.IntegerField()),
                ('language', models.CharField(max_length=25)),
                ('rating', models.IntegerField()),
                ('author', models.CharField(max_length=50)),
                ('desc', models.CharField()),
                ('imageLink', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('prodNum', models.IntegerField(primary_key=True, serialize=False)),
                ('prodName', models.CharField(max_length=50)),
                ('prodPrice', models.FloatField()),
                ('prodStock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WhishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer')),
                ('productNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Products')),
            ],
        ),
        migrations.AddField(
            model_name='productdetails',
            name='prodNum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Products'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='productNum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Products'),
        ),
        migrations.AddField(
            model_name='address',
            name='customerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer'),
        ),
        migrations.AlterUniqueTogether(
            name='whishlist',
            unique_together=set([('custId', 'productNum')]),
        ),
        migrations.AlterUniqueTogether(
            name='orderdetails',
            unique_together=set([('orderNum', 'productNum')]),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('customerID', 'address')]),
        ),
    ]
