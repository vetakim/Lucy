# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElfenLied', '0002_point_noise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.FloatField()),
                ('lifetime', models.FloatField()),
                ('duration', models.FloatField()),
                ('action', models.TextField()),
                ('object_type', models.TextField()),
                ('distance', models.FloatField()),
                ('azimuth', models.FloatField()),
                ('row', models.FloatField()),
                ('tact', models.FloatField()),
            ],
        ),
    ]
