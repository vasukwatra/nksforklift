# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nks',
            name='cell_phone',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='nks',
            name='other',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='nks',
            name='postal_code',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='nks',
            name='residential_phone',
            field=models.IntegerField(max_length=11),
        ),
    ]
