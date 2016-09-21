#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oppoVideoAppsOnline.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^jizzdr_video/video_crawler','VideoCrawler.views.video_crawler'),
)
