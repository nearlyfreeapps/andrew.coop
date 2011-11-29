from coop.models import Organization

def get_organizations(request):
    return {'organizations': Organization.objects.order_by('-term_number')}

