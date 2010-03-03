from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'cookmom/home.html'}), 
    (r'^toprecipes/', direct_to_template, {'template': 'cookmom/toprecipes.html'}),
    (r'^about/', direct_to_template, {'template': 'cookmom/about.html'})
)