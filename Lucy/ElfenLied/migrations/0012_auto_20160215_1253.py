# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0011_auto_20160215_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitioninput',
            name='lawstring',
            field=models.CharField(choices=[('cubic', 'cubic'), ('square', 'square'), ('sign', 'sign'), ('ratio', 'ratio'), ('linear', 'linear'), ('current', 'current')], default='cubic', max_length=255),
        ),
        migrations.AlterField(
            model_name='requisitionoutput',
            name='action',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='requisitionoutput',
            name='object_type',
            field=models.CharField(max_length=255),
        ),
    ]
