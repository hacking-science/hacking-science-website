__author__ = 'max'
from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.feed, name='feed'),
    url(r'^tag/(?P<tag_id>\d+)', views.tag, name='tag'),
    url(r'^theEdge/$', views.theEdge, name='theEdge'),
    url(r'^bridgeAcademy/$', views.brigdeAcademy, name='bridgeAcademy'),
    url(r'^dalstonLibrary/$', views.dalstonLibrary, name='dalstonLibrary'),
    url(r'^events/$', views.events, name='events'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^mapToBreathe/$', views.mapToBreathe, name='mapToBreathe'),
    url(r'about/$', views.about, name='about'),
    #url(r'^search/$', views.search, name='search')
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post')
]
