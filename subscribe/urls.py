__author__ = 'max'
from django.conf.urls import url

from subscribe import views


urlpatterns = [
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
]