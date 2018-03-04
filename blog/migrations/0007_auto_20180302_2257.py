# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_youtube'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Youtube',
            new_name='Video',
        ),
        migrations.AddField(
            model_name='posttag',
            name='Video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_tag_set', to='blog.Video'),
            preserve_default=False,
        ),
    ]