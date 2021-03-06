__author__ = 'max'
from django.conf.urls import url, include

from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^informalsci/$', views.informalsci, name='informalsci'),
    #url(r'^coding/$', views.coding, name='coding'),
    #url(r'^environment/$', views.environment, name='environment'),
    #url(r'^creativespaces/$', views.creativespaces, name='creativespaces'),
    #url(r'^history/$', views.history, name='history'),
    url(r'^magazine/$', views.magazine, name='magazine'),
    url(r'^hackfeed/$', views.feed, name='hackfeed'),
    url(r'^hackfeed/historyrace$', views.historyHackfeed, name='historyHackfeed'),
    url(r'^hackfeed/science$', views.scienceHackfeed, name='scienceHackfeed'),
    url(r'^hackfeed/programming', views.codingHackfeed, name='codingHackfeed'),
    url(r'^hackfeed/environment', views.environmentHackfeed, name='environmentHackfeed'),
    url(r'^tag/(?P<tag_id>\d+)', views.tag, name='tag'),
    url(r'^theEdge/$', views.theEdge, name='theEdge'),
    url(r'^bridgeAcademy/$', views.brigdeAcademy, name='bridgeAcademy'),
    url(r'^dalstonLibrary/$', views.dalstonLibrary, name='dalstonLibrary'),
    url(r'^events/$', views.events, name='events'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^mapToBreathe/$', views.mapToBreathe, name='mapToBreathe'),
    url(r'about/$', views.about, name='about'),
    #url(r'hackingEducationHome/other/$', views.hackingEducationOtherPage, name='hackingEducationOtherPage'),
    #url(r'^search/$', views.search, name='search')
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^martor/', include('martor.urls'))
]
