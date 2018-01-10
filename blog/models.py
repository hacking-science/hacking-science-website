# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class AbstractBaseClass(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Post(AbstractBaseClass):
    title = models.CharField(max_length=200)
    content = models.TextField()


class Tag(AbstractBaseClass):
    title = models.CharField(max_length=100)


class Location(AbstractBaseClass):
    title = models.CharField(max_length=100)


class PostTag(AbstractBaseClass):
    post = models.ForeignKey("Post")
    tag = models.ForeignKey("Tag")


class PostLocation(AbstractBaseClass):
    post = models.ForeignKey("Post")
    location = models.ForeignKey("Location")

class Comment(AbstractBaseClass):
    post = models.ForeignKey("Post")