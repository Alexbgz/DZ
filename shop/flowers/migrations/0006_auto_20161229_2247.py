# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0005_auto_20161229_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='summ',
            field=models.IntegerField(),
        ),
    ]
