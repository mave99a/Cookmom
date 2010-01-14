from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', tagcloud), 
    (r'^_add_$', add_tags),
    (r'^_remove_$', remove_tags), 
    (r'^(?P<tag>.+)/$', show_by_tag), 
#    (r'^(?P<key>.+)/edit/$', edit_user),
#    (r'^(?P<key>.+)/dele/$', delete_user), 
#    (r'^(?P<key>.+)$', show_user), 
)