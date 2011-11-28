from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseBadRequest

from blog.models import Blog

def blog(request):
    return render_to_response('blog/index.html', {

    }, RequestContext(request))

def blog_article(request, object_id):
    try:
        article = Blog.objects.filter(pk = object_id)
    except:
        return HttpResponseBadRequest('Article %s does not exist' % object_id)

    return render_to_response('blog/article.html'), {

    }, RequestContext(request))

