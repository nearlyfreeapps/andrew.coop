from django.shortcuts import render_to_response
from django.template import RequestContext

from coop.forms import ContactForm

def index(request):
    return render_to_response('coop/index.html')    

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

