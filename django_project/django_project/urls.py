from django.conf.urls import patterns, include, url
import django.contrib.auth.views


urlpatterns = patterns('',
    url(r'^work_evid/', include('work_evid.urls', namespace='work_evid')),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout'),
)

