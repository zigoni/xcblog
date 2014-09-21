from django.conf.urls import patterns, url

urlpatterns = patterns('xcblog.views',
    url(r'^$', 'homepage', name='xc-homepage'),
    url(r'^b(?P<pk>\d+)/$', 'show_blogpost', name='xc-show-blogpost'),
    url(r'^c(?P<pk>\d+)/$', 'show_category', name='xc-show-category'),
    url(r'^a(?P<year>\d{4})(?P<month>\d{2})/$', 'show_archive', name='xc-show-archive'),
)