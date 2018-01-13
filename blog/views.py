# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from blog.models import Post, Tag


# Create your views here.
def index(request):
    posts = Post.objects.all()
    reset = False
    tags = Tag.objects.all()
    context = {"posts": posts, "reset": reset, "tags": tags}
    return render(request, "./home/index.html", context)


def tag(request, tag_id=None):
    if tag_id:
        tags = Tag.objects.exclude(id=tag_id)
        posts = Post.objects.filter(post_tag_set__tag__id=tag_id)
        reset = True
        context = {"posts": posts, "reset": reset, "tags": tags}

        return render(request, "./home/index.html", context)
    else:
        return HttpResponseRedirect(reverse(index))


def theEdge(request):

    """Generate the Edge Data"""

    context = {}
    return render(request, "./home/theEdge.html", context)
