# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-17 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Universidade',
            new_name='Universidad',
        ),
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name': 'Campus', 'verbose_name_plural': 'Campus'},
        ),
    ]