# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='foto',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/', verbose_name='Ссылка картинки'),
        ),
    ]
