# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from model_utils.managers import InheritanceManager
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class AbstractBaseClass(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Tag(AbstractBaseClass):
    title = models.CharField(max_length=100, unique=True)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title


class Post(AbstractBaseClass):
    # objects = InheritanceManager()

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    summary = models.TextField(max_length=280)
    tags = models.ManyToManyField(Tag, null=True, related_name="post_tag_set")
    # tags = models.ForeignKey(Tag, null=True, related_name="post_tag_set")

    def __str__(self):
        return self.title

    def get_tags(self):
        return self.tags.all()

    # Is there a better way of writing this?
    def get_content_type(self):
        return self.__class__.__name__.lower()


class Feature(Post):
    content = models.TextField(blank=True)
    image_url = models.URLField(blank=True, default="")


class Video(Post):
    video_id = models.CharField(max_length=500)


class Link(Post):
    url = models.CharField(max_length=500)
    image_url = models.CharField(max_length=512)


# class Location(AbstractBaseClass):
#     title = models.CharField(max_length=100)


# class PostTag(AbstractBaseClass):
#     feature = models.ForeignKey("Feature", related_name="post_tag_set")
#     tag = models.ForeignKey("Tag", related_name="post_tag_set")


# class PostLocation(AbstractBaseClass):
#     post = models.ForeignKey("Post")
#     location = models.ForeignKey("Location")


# class Comment(AbstractBaseClass):
#     post = models.ForeignKey("Post")
