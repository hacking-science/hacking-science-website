# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)
