from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^blog$', 'blog'),
    url(r'^blog/(?<object_id>)$', 'blog_article'),
)

