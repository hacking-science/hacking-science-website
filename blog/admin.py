# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Post, Tag, PostTag
from django_markdown.admin import MarkdownModelAdmin
from django.contrib import admin

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

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(MyModel, MarkdownModelAdmin)
