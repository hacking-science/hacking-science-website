__author__ = 'max'
from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tag/(?P<tag_id>\d+)', views.tag, name='tag'),
    url(r'^theEdge/$', views.theEdge, name='theEdge'),
    url(r'^bridgeAcademy/$', views.brigdeAcademy, name='bridgeAcademy'),
    url(r'^dalstonLibrary/$', views.dalstonLibrary, name='dalstonLibrary'),
    url(r'^events/$', views.events, name='events'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^mapToBreathe/$', views.mapToBreathe, name='mapToBreathe'),
    #url(r'^search/$', views.search, name='search')
]
