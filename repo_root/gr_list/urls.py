from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^/groc$', views.post_list, name='post-list'),
    url(r'^/new$', views.post_new, name='post-new'),
    url(r'^$', views.spurs_blog, name='spurs'),
    )
