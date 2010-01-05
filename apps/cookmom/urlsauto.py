from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'', include('cookmom.urls')),
)