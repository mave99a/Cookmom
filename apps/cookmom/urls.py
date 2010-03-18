from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'home.html'}), 
    (r'^toprecipes/', direct_to_template, {'template': 'toprecipes.html'}),
    (r'^about/', direct_to_template, {'template': 'about.html'})
)