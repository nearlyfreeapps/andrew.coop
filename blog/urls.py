from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'blog'),
    url(r'^(?P<object_id>\d+)$', 'blog_article'),
)

