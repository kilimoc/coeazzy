# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelmanager', '0004_auto_20170624_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='rent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
