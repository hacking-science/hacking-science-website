# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 16:54
from __future__ import unicode_literals

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='content',
            field=martor.models.MartorField(),
        ),
    ]
