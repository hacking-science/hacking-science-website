# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180303_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Post')),
                ('url', models.CharField(max_length=500)),
                ('cover_image', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.post',),
        ),
        migrations.AddField(
            model_name='feature',
            name='cover_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]