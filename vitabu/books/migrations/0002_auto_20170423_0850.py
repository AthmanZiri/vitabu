# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-23 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='shelf_location',
            field=models.CharField(choices=[('1A', '1A'), ('1B', '1B'), ('1C', '1C')], default='', max_length=10, verbose_name='shelf_location'),
        ),
    ]
