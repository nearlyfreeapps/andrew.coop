from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView

from blog.models import Blog

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(
        model = Blog,
        template_name = 'blog/index.html',
        paginate_by = 5,
    )),
    url(r'^(?P<object_id>\d+)$', 'blog_article'),
)

