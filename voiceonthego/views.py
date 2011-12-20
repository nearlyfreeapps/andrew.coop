from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('voiceonthego/index.html', {
        'organization_name': 'Voice On The Go',
        'organization_id': 'voiceonthego'      
    }, context_instance = RequestContext(request))

def job(request):
    return render_to_response('voiceonthego/job.html', {
        'organization_name': 'Voice On The Go',
        'organization_id': 'voiceonthego'         
    }, context_instance = RequestContext(request))

def goals(request):
    return render_to_response('voiceonthego/goals.html', {
        'organization_name': 'Voice On The Go',
        'organization_id': 'voiceonthego'         
    }, context_instance = RequestContext(request))

def experience(request):
    return render_to_response('voiceonthego/experience.html', {
        'organization_name': 'Voice On The Go',
        'organization_id': 'voiceonthego'         
    }, context_instance = RequestContext(request))

def acknowledgments(request):
    return render_to_response('voiceonthego/acknowledgments.html', {
        'organization_name': 'Voice On The Go',
        'organization_id': 'voiceonthego'         
    }, context_instance = RequestContext(request))

