from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', list_article), 
    (r'^new/$', new_article), 
    (r'^(?P<slug>.+)/edit/$', edit_article),
    (r'^(?P<slug>.+)/dele/$', delete_article), 
    (r'^(?P<slug>.+)/$', show_article),
)
