from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatgrafico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^permit/$', error_permisos),
)