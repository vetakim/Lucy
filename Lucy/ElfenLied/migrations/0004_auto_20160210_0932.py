# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0003_requisitions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requisitions',
            new_name='RequisitionModel',
        ),
    ]
