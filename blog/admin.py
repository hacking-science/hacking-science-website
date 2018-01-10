# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model= Post



admin.site.register(Post, PostAdmin)