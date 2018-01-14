from django.conf.urls import include, url
from breathe import views


urlpatterns = [
    url(r"^", views.index),
]
