# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180302_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Post')),
                ('url', models.TextField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.post',),
        ),
    ]