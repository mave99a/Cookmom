from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', list_user), 
    (r'^new/$', new_user), 
    (r'^(?P<id>\d+)/edit/$', edit_user),
    (r'^(?P<id>\d+)/dele/$', delete_user), 
    (r'^(?P<id>\d+)/(?P<obj>\w+)/$', show_user_detail), 
    (r'^(?P<id>\d+)/$', show_user), 
)