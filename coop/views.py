from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import Blog
from coop.models import Organization
from coop.forms import ContactForm

def index(request):
    return render_to_response('coop/index.html', {
        'blog_posts': Blog.objects.order_by('-date')[:3]
    }, RequestContext(request))    

def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sent = True
            form.send()
            form = ContactForm()
    else:
        form = ContactForm()
    return render_to_response('coop/contact.html', {
        'form': form,
        'sent': sent       
    }, RequestContext(request))

