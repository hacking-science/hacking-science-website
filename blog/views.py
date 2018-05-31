# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from blog.models import Post, Tag
from django.db.models import Q

from bs4 import BeautifulSoup

def index(request):
    """Generate Home Page"""
    posts = Post.objects.filter(tags__title='news')

    context = {
        "news_posts": posts
    }
    return render(request, "nova/page/homepage.html", context)


def tag(request, tag_id=None):
    if tag_id:
        tags = Tag.objects.exclude(id=tag_id)
        posts = Post.objects.filter(tags=tag_id)
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


def scienceHackfeed(request):
    """Returns hackFeed filtered with science/workshops tagged posts"""

    posts = Post.objects.filter(Q(tags__title__icontains='dalston') | Q(tags__title__icontains='edge')| Q(tags__title__icontains='science')| Q(tags__title__icontains='workshop')).distinct()
    tags = Tag.objects.all()
    reset = False


    context={"posts": posts, "reset": reset, "tags": tags}
    return render(request, "home/feed.html", context)


def codingHackfeed(request):
    """Returns hackFeed filtered with programming tagged posts"""
    posts = Post.objects.filter(Q(tags__title__icontains='coding') | Q(tags__title__icontains='programming')| Q(tags__title__icontains='code')).distinct()
    tags = Tag.objects.all()
    reset = False

    context = {"posts": posts, "reset": reset, "tags": tags}
    return render(request, "home/feed.html", context)


def environmentHackfeed(request):
    """Returns hackFeed filtered with environment/maptobreathe/air"""

    posts = Post.objects.filter(Q(tags__title__icontains='environment') | Q(tags__title__icontains='maptobreathe')).distinct()
    tags = Tag.objects.all()
    reset = False


    context={"posts": posts, "reset": reset, "tags": tags}
    return render(request, "home/feed.html", context)


def creativespaces(request):
    """Generate creativespaces page"""
    context={}
    return render(request, "home/creativespaces.html", context)


def historyHackfeed(request):
    """Returns hackFeed filtered with history and/or race tagged posts"""

    posts = Post.objects.filter(Q(tags__title__icontains='race') | Q(tags__title__icontains='history')).distinct()
    tags = Tag.objects.all()
    reset = False


    context={"posts": posts, "reset": reset, "tags": tags}
    return render(request, "home/feed.html", context)


def magazine(request):
    """Returns hackFeed filtered with magazine tagged posts"""
    posts = Post.objects.filter(Q(tags__title__icontains='magazine') | Q(tags__title__icontains='posterbook')).distinct()
    tags = Tag.objects.all()
    reset = False

    context = {"posts": posts, "reset": reset, "tags": tags}
    return render(request, "home/feed.html", context)

def bridge(request):
    """Returns hackFeed filtered with bridge tagged posts"""
    posts = Post.objects.filter(tags__title__icontains='dalston')
    tags = Tag.objects.all()
    reset = False

    context = {"posts": posts, "reset": reset, "tags": tags}
    return render(request, "home/feed.html", context)

def edge(request):
    """Returns hackFeed filtered with edge tagged posts"""
    posts = Post.objects.filter(tags__title__icontains='edge')
    tags = Tag.objects.all()
    reset = False

    context = {"posts": posts, "reset": reset, "tags": tags}
    return render(request, "home/feed.html", context)




