from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', list_user), 
    (r'^(?P<id>\d+)/(?P<obj>\w+)/$', show_user_detail), 
    (r'^(?P<id>\d+)/$', show_user), 
    # my 
    (r'^me/$', show_myhome), 
    (r'^me/edit/$', edit)
)