from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^portfolio/', include('coop.urls')),
    url(r'^portfolio/voiceonthego/', include('voiceonthego.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

