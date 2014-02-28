from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^work_evid/', include('work_evid.urls', namespace='work_evid')),
)

