# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    """Generate Home Page"""
    context = {}
    return render(request, "index.html", context)

def about(request):
    """Generate About Page"""
    context={}
    return render(request, "about.html", context)
