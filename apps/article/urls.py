from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', list_article), 
    (r'^new/$', new_article), 
    (r'^(?P<key>.+)/edit/$', edit_article),
    (r'^(?P<key>.+)/dele/$', delete_article), 
    (r'^(?P<key>.+)$', show_article),
)
