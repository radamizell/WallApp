# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 23:32
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(27, -38), null=True, srid=4326)),
                ('sound', models.FileField(upload_to='')),
                ('prefered_radius', models.IntegerField(default=5, help_text='in kilometers')),
                ('rating', models.IntegerField(default=1)),
            ],
        ),
    ]
