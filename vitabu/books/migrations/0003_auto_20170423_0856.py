# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-23 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170423_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Good', 'Good'), ('Old', 'Old')], default='', max_length=10, verbose_name='condition'),
        ),
    ]
