from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('coop.views',
    url(r'^$', 'index'),
    url(r'^contact$', 'contact'),
)

