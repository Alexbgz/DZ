# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0003_auto_20161222_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='foto',
            field=models.CharField(max_length=255),
        ),
    ]