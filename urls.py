from django.conf.urls import patterns, url

urlpatterns = patterns('xcblog.views',
    url(r'^$', 'homepage', name='xc-homepage'),
    url(r'^b(?P<pk>\d+)/$', 'show_blogpost', name='xc-show-blogpost'),
)