from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'^search/', include('search.urls')),
)