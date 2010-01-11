from django.conf.urls.defaults import *
from views import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$',  direct_to_template, {'template': 'search/home.html'}), 
#    (r'^(?P<key>.+)/edit/$', edit_user),
#    (r'^(?P<key>.+)/dele/$', delete_user), 
#    (r'^(?P<key>.+)$', show_user), 
)