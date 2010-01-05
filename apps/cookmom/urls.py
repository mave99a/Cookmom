from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    (r'^$', homepage), 
    (r'^toprecipes/', toprecipes),
    (r'^about/', direct_to_template, {'template': 'cookmom/about.html'})
)