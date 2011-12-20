from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('polarmobile/index.html', {
        'organization_name': 'Polar Mobile',
        'organization_id': 'polarmobile'      
    }, context_instance = RequestContext(request))

def job(request):
    return render_to_response('polarmobile/job.html', {
        'organization_name': 'Polar Mobile',
        'organization_id': 'polarmobile'         
    }, context_instance = RequestContext(request))

def goals(request):
    return render_to_response('polarmobile/goals.html', {
        'organization_name': 'Polar Mobile',
        'organization_id': 'polarmobile'         
    }, context_instance = RequestContext(request))

def technology(request):
    return render_to_response('polarmobile/technology.html', {
        'organization_name': 'Polar Mobile',
        'organization_id': 'polarmobile'         
    }, context_instance = RequestContext(request))

def acknowledgments(request):
    return render_to_response('polarmobile/acknowledgments.html', {
        'organization_name': 'Polar Mobile',
        'organization_id': 'polarmobile'         
    }, context_instance = RequestContext(request))

