from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'^tag/', include('tagging.urls')),
)