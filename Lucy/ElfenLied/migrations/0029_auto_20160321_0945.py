# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0028_auto_20160307_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitioninput',
            name='lawstring',
            field=models.CharField(choices=[('current', 'current'), ('linear', 'linear'), ('cubic', 'cubic'), ('ratio', 'ratio'), ('square', 'square'), ('sign', 'sign')], default='current', max_length=255),
        ),
    ]