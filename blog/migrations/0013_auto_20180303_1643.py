# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/images/%y/%m/%d'),
        ),
    ]