# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0020_auto_20160301_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calcandclear',
            name='toclear',
        ),
        migrations.AlterField(
            model_name='requisitioninput',
            name='lawstring',
            field=models.CharField(choices=[('sign', 'sign'), ('linear', 'linear'), ('square', 'square'), ('current', 'current'), ('ratio', 'ratio'), ('cubic', 'cubic')], default='sign', max_length=255),
        ),
    ]
