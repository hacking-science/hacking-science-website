# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=280)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Post')),
                ('content', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.post',),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Post')),
                ('url', models.CharField(max_length=500)),
                ('image_url', models.CharField(max_length=512)),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.post',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Post')),
                ('video_id', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.post',),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='post_tag_set', to='blog.Tag'),
        ),
    ]
