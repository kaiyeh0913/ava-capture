# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-28 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='take',
            name='sequence',
            field=models.IntegerField(default=0),
        ),
    ]
