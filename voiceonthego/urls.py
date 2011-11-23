from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('voiceonthego.views',
    url(r'^$', 'index'),
)

