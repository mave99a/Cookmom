from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'^image/', include('image.urls')),
)