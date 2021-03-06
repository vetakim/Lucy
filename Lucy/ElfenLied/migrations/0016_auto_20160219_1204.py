# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0015_auto_20160216_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisitionoutput',
            old_name='numinbarrier',
            new_name='direction',
        ),
        migrations.AlterField(
            model_name='requisitioninput',
            name='lawstring',
            field=models.CharField(choices=[('linear', 'linear'), ('sign', 'sign'), ('ratio', 'ratio'), ('cubic', 'cubic'), ('current', 'current'), ('square', 'square')], default='linear', max_length=255),
        ),
    ]
