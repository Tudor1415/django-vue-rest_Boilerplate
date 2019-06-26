from django.conf.urls import url
from django.contrib import admin

app_name='posts'

from .views import (
    PostListApiView,
    PostDetailApiView,
    PostDeleteApiView,
    PostUpdateApiView,
    PostCreateApiView,
	)

urlpatterns = [
	url(r'^$', PostListApiView.as_view(), name='list'),
    url(r'^create/$', PostCreateApiView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', PostDetailApiView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateApiView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteApiView.as_view()),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
