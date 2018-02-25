from django.shortcuts import render

def subscribe(request):
    """Generate Subscribe page"""
    context ={}
    return render(request, "subscribe.html", context)