# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slicer', '0003_auto_20170313_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='pngimage',
            name='series',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='slicer.ImageSeries'),
        ),
        migrations.AlterField(
            model_name='imageseries',
            name='images',
            field=models.ManyToManyField(blank=True, to='slicer.PNGImage'),
        ),
    ]
