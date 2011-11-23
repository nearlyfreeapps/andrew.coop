from django.shortcuts import render_to_response

def index(request):
    return render_to_response('content/index.html', {
        'organization_name': 'Voice On The Go',
        'organization_id': 'voiceonthego'      
    })

