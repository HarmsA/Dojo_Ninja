# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-01 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_auto_20181201_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
