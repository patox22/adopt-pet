# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 01:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20170716_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2)]),
        ),
    ]
