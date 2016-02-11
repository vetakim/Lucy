# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-11 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0007_requisitionmodel_maxtact'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisitionmodel',
            name='dispersion',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisitionmodel',
            name='free_resource',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisitionmodel',
            name='lawstring',
            field=models.CharField(default='current', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisitionmodel',
            name='medium',
            field=models.FloatField(default=11),
            preserve_default=False,
        ),
    ]
