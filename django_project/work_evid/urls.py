from django.conf.urls import patterns, include, url
import django.contrib.auth.views

from work_evid import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^overviews/$', views.overviews, name='overviews'),
    url(r'^delete_work/$', views.delete_work, name='delete_work'),
    url(r'^firm/$', views.FirmList.as_view(), name='firm_list'),
    url(r'^firm/add/$', views.FirmCreate.as_view(), name='firm_create'),
    url(r'^firm/detail/(?P<pk>\d+)/$', views.FirmDetail.as_view(), name='firm_detail'),
    url(r'^firm/update/(?P<pk>\d+)/$', views.FirmUpdate.as_view(), name='firm_update'),
    url(r'^firm/delete/(?P<pk>\d+)/$', views.FirmDelete.as_view(), name='firm_delete'),
    url(r'^todo/$', views.TodoList.as_view(), name='todo_list'),
    url(r'^todo/add/$', views.TodoCreate.as_view(), name='todo_create'),
    url(r'^todo/detail/(?P<pk>\d+)/$', views.TodoDetail.as_view(), name='todo_detail'),
    url(r'^todo/update/(?P<pk>\d+)/$', views.TodoUpdate.as_view(), name='todo_update'),
    url(r'^todo/delete/(?P<pk>\d+)/$', views.TodoDelete.as_view(), name='todo_delete'),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout'),
)
