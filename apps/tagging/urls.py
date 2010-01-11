from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', tagcloud), 
#    (r'^(?P<key>.+)/edit/$', edit_user),
#    (r'^(?P<key>.+)/dele/$', delete_user), 
#    (r'^(?P<key>.+)$', show_user), 
)