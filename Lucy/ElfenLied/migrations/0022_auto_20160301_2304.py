# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0021_auto_20160301_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitioninput',
            name='lawstring',
            field=models.CharField(choices=[('ratio', 'ratio'), ('sign', 'sign'), ('square', 'square'), ('linear', 'linear'), ('current', 'current'), ('cubic', 'cubic')], default='ratio', max_length=255),
        ),
    ]
