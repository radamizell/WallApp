# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 03:28
from __future__ import unicode_literals

import constrainedfilefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='sound',
            field=constrainedfilefield.fields.ConstrainedFileField(content_types=['audio/mpeg', 'audio/mp4', 'audio/ogg'], mime_lookup_length=4096, upload_to=''),
        ),
    ]
