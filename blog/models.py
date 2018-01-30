# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AbstractBaseClass(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.date_created


class Post(AbstractBaseClass):
    FEATURE = 'FEAT'
    LINK = 'LINK'
    POST_TYPES = (
        (FEATURE, 'feature'),
        (LINK, 'link'),
    )

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=4, choices=POST_TYPES, default=FEATURE)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_tags(self):
        return Tag.objects.filter(post_tag_set__post=self)


class Tag(AbstractBaseClass):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Location(AbstractBaseClass):
    title = models.CharField(max_length=100)


class PostTag(AbstractBaseClass):
    post = models.ForeignKey("Post", related_name="post_tag_set")
    tag = models.ForeignKey("Tag", related_name="post_tag_set")


class PostLocation(AbstractBaseClass):
    post = models.ForeignKey("Post")
    location = models.ForeignKey("Location")


class Comment(AbstractBaseClass):
    post = models.ForeignKey("Post")


class Subscribe(AbstractBaseClass):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=70)
