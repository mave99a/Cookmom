from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', list_comment), 
    (r'^new/(?P<key>.+)$', new_comment), 
)