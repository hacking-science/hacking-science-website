# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from hackfeed.models import Post, Tag


def tag(request, tag_id=None):
    if tag_id:
        tags = Tag.objects.exclude(id=tag_id)
        posts = Post.objects.filter(post_tag_set__tag__id=tag_id)
        reset = True
        context = {"posts": posts, "reset": reset, "tags": tags}

        return render(request, "home/feed.html", context)
    else:
        return HttpResponseRedirect(reverse(index))

#def search(request, tag_id=None):
    #"""Filter the news feed according to the user input in the search bar"""

    #tag_title = request.GET['searchbar']
    #tags = Tag.objects.filter(title=tag_title)

    #tags = Tag.objects.exclude(id=tag_id)
    #posts = Post.objects.filter(post_tag_set__tag__id=tags.tag_id)
    #reset = True
    #context = {"tags": tags}
    #return render(request, "home/feed.html", context)




def theEdge(request):

    """Generate the Edge Data"""

    context = {}
    return render(request, "hackfeed/workshops/theEdge.html", context)


def brigdeAcademy(request):

    """Generate the Bridge-Academy Data"""

    context = {}
    return render(request, "hackfeed/workshops/bridgeAcademy.html", context)


def dalstonLibrary(request):

    """Generate the Dalston Library Data"""

    context = {}
    return render(request, "hackfeed/workshops/dalstonLibrary.html", context)

def feed(request):
    """Generate hackingScience main feed"""

    #tag_search = request.GET['searchbar']
    if 'searchbar' in request.GET:
        tag_search = request.GET['searchbar']
        tags = Tag.objects.filter(title=tag_search)


    else:
        tags = Tag.objects.all()

    posts = Post.objects.all()
    reset = False



    context = {"posts": posts, "reset": reset, "tags": tags}
    return render(request, "hackfeed/feed.html", context)


def post(request, post_id):
    """Generate Feed post page"""
    post = Post.objects.get(id=post_id)


    context = {"post": post}
    return render(request, "hackfeed/post/single.html", context)
  
