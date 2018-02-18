__author__ = 'max'
from django.conf.urls import url

from staticsite import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
]