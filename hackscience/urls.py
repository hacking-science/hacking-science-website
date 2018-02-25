"""hackscience URL Configuration"""
__author__ = 'max'

from django.conf.urls import url, include
from django.contrib import admin

from staticsite.views import index, about
from hackfeed import views as feedviews
from subscribe.views import subscribe

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'about/$', about, name="about"),
    url(r'^hackfeed/$', feedviews.feed, name='feed'),
    url(r'^tag/(?P<tag_id>\d+)', feedviews.tag, name='tag'),
    url(r'^post/(?P<post_id>\d+)/$', feedviews.post, name='post'),
    url(r'^theEdge/$', feedviews.theEdge, name='theEdge'),
    url(r'^bridgeAcademy/$', feedviews.brigdeAcademy, name='bridgeAcademy'),
    url(r'^dalstonLibrary/$', feedviews.dalstonLibrary, name='dalstonLibrary'),
    url(r'^events/$', feedviews.events, name="events"),
    url(r'^subscribe/$', subscribe, name='subscribe'),
    url(r"^breathe", include("breathe.urls", namespace="breathe")),
]
