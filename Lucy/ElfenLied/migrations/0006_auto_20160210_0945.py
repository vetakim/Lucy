# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0005_requisitionmodel_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisitionmodel',
            name='catastrophe',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisitionmodel',
            name='precedence',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisitionmodel',
            name='start_time',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
