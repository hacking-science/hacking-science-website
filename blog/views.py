# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from blog.models import Post, Tag

def index(request):
    """Generate Home Page"""
    context = {}
    return render(request, "home/index.html", context)

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
    return render(request, "home/theEdge.html", context)


def brigdeAcademy(request):

    """Generate the Bridge-Academy Data"""

    context = {}
    return render(request, "home/bridgeAcademy.html", context)


def dalstonLibrary(request):

    """Generate the Dalston Library Data"""

    context = {}
    return render(request, "home/dalstonLibrary.html", context)


def events(request):
    """Generate the Dalston Library Data"""
    context = {}
    return render(request, "home/eventsTemp.html", context)


def subscribe(request):
    """Generate Subscribe page"""
    context ={}
    return render(request, "home/subscribe.html", context)


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
    return render(request, "home/feed.html", context)


def mapToBreathe(request):
    """Generate A Map to Breathe Page"""
    context={}
    return render(request, "home/mapToBreathe.html", context)

def post(request, post_id):
    """Generate Feed post page"""
    post = Post.objects.get(id=post_id)


    context = {"post": post}
    return render(request, "post/single.html", context)


def about(request):
    """Generate About Page"""
    context={}
    return render(request, "home/about.html", context)


def informalsci(request):
    """Generate informal science page"""
    context={}
    return render(request, "home/informalsci.html", context)


def coding(request):
    """Generate coding page"""
    context={}
    return render(request, "home/coding.html", context)


def environment(request):
    """Generate environment page"""
    context={}
    return render(request, "home/environment.html", context)


def creativespaces(request):
    """Generate creativespaces page"""
    context={}
    return render(request, "home/creativespaces.html", context)


def history(request):
    """Generate history page"""
    context={}
    return render(request, "home/history.html", context)


def magazine(request):
    """Generate magazine page"""
    context={}
    return render(request, "home/magazine.html", context)



