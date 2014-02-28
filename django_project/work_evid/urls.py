from django.conf.urls import patterns, include, url
import django.contrib.auth.views

from work_evid import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^overviews/$', views.overviews, name='overviews'),
    url(r'firm_edit/$', views.firm_edit, name='firm_edit'),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout'),
)
