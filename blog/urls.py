__author__ = 'max'
from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tag/(?P<tag_id>\d+)', views.tag, name='tag'),
    url(r'^theEdge/$', views.theEdge, name='theEdge'),
]
