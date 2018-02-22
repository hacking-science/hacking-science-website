from django.shortcuts import render

def events(request):
    """Generate the Events"""
    context = {}
    return render(request, "events/eventsTemp.html", context)