from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', list_user), 
    (r'^new/$', new_user), 
    (r'^(?P<key>.+)/edit/$', edit_user),
    (r'^(?P<key>.+)/dele/$', delete_user), 
    (r'^(?P<key>.+)/(?P<obj>\w+)/$', show_user_detail), 
    (r'^(?P<key>.+)$', show_user), 
)