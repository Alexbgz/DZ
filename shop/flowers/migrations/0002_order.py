# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('iduser', models.IntegerField()),
                ('idproduct', models.IntegerField()),
                ('quantity', models.CharField(max_length=255)),
                ('summ', models.CharField(max_length=255)),
            ],
        ),
    ]