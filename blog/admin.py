# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Post, Tag, PostTag

# Register your models here.


class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model= Post
    inlines = (PostTagInline,)


class TagAdmin(admin.ModelAdmin):
    model = Tag
    inlines = (PostTagInline,)




admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
