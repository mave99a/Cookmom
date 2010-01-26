from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    (r'^$', list_article), 
    (r'^new/$', new_article), 
    (r'^edit/', direct_to_template, {'template': 'article/edit.html'}),
    (r'^(?P<slug>.+)/edit/$', edit_article),
    (r'^(?P<slug>.+)/dele/$', delete_article), 
    (r'^(?P<slug>.+)/$', show_article),
)
