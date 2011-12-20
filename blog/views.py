from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseBadRequest

from blog.models import Blog

def blog_article(request, object_id):
    try:
        article = Blog.objects.get(pk = object_id)
    except Blog.DoesNotExist:
        return HttpResponseBadRequest('Article %s does not exist' % object_id)

    return render_to_response('blog/article.html', {
        'article': article
    }, RequestContext(request))

