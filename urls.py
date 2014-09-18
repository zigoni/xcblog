from django.conf.urls import patterns, url

urlpatterns = patterns('xcblog.views',
    url(r'^$', 'homepage', name='xc-homepage'),
)