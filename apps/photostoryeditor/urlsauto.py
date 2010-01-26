from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'^edit/', include('photostoryeditor.urls')),
)