from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    (r'^new/$', new_article), 
    (r'^edit/', direct_to_template, {'template': 'article/edit.html'}),
    (r'^(?P<id>\d+)/edit/$', edit_article),
    (r'^(?P<id>\d+)/dele/$', delete_article), 
    (r'^(?P<id>\d+)/(?P<title>.+)/$', show_article),
    (r'^(?P<id>\d+)/$', show_article),    
    (r'^ajax/preview/(?P<id>\d+)/$', ajax_preview),
    (r'^ajax/save/(?P<id>\d+)/$', ajax_save),
    (r'^publish/(?P<id>\d+)/$', publish),
    (r'^unpublish/(?P<id>\d+)/$', unpublish),
    (r'^$', list_article), 
    (r'^(?P<order>\w+)/$', list_article), 
    )
