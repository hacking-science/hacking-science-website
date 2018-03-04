# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from blog.models import Feature, Video, Link, Tag


class TagInline(GenericTabularInline):
    model = Tag
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = (TagInline,)
    readonly_fields = ['date_created']

class FeatureAdmin(PostAdmin):
    model = Feature

class VideoAdmin(PostAdmin):
    model = Video

class LinkAdmin(PostAdmin):
    model = Link

class TagAdmin(PostAdmin):
    model = Tag

admin.site.register(Feature, FeatureAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Tag, TagAdmin)
