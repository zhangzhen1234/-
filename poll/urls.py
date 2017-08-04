from django.conf.urls import include, url
from django.contrib import admin
from views import index,show,showaction

urlpatterns=[
    url(r'index/',index,name="index"),
    url(r'show/(?P<id>[0-9])',show,name="show"),
    url(r'showaction/(?P<id>[0-9])',showaction,name="showaction")
]