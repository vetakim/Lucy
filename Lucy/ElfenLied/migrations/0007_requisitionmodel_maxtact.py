# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-11 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0006_auto_20160210_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisitionmodel',
            name='maxtact',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
