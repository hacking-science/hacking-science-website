__author__ = 'max'
from django.conf.urls import url, include

from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^informalsci/$', views.informalsci, name='informalsci'),
    url(r'^coding/$', views.coding, name='coding'),
    url(r'^environment/$', views.environment, name='environment'),
    url(r'^creativespaces/$', views.creativespaces, name='creativespaces'),
    url(r'^history/$', views.history, name='history'),
    url(r'^magazine/$', views.magazine, name='magazine'),
    url(r'^blog/$', views.feed, name='feed'),
    url(r'^tag/(?P<tag_id>\d+)', views.tag, name='tag'),
    url(r'^theEdge/$', views.theEdge, name='theEdge'),
    url(r'^bridgeAcademy/$', views.brigdeAcademy, name='bridgeAcademy'),
    url(r'^dalstonLibrary/$', views.dalstonLibrary, name='dalstonLibrary'),
    url(r'^events/$', views.events, name='events'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^mapToBreathe/$', views.mapToBreathe, name='mapToBreathe'),
    url(r'about/$', views.about, name='about'),
    url(r'hackingEducationHome/$', views.hackingEducationHome, name='nova'),
    #url(r'^search/$', views.search, name='search')
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^martor/', include('martor.urls'))
]
