from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('polarmobile.views',
    url(r'^$', 'index'),
    url(r'^job$', 'job'),
    url(r'^goals$', 'goals'),
    url(r'^experience$', 'experience'),
    url(r'^acknowledgments$', 'acknowledgments'),
)

