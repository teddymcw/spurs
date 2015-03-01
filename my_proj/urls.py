from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/', include('gr_list.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('gr_list.urls')),
)