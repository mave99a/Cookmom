from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'^article/', include('article.urls')),
)