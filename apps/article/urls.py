from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    (r'^new/$', new_article), 
    url(r'^edit/(?P<id>\d+)/$', ArticleViews.update, name='article_edit'),
    
    url(r'^dele/(?P<id>\d+)/$', ArticleViews.delete, name='article_delete'), 

    url(r'^(?P<id>\d+)/(?P<title>.+)/$', ArticleViews.detail, name='article_detail'),
    url(r'^(?P<id>\d+)/$', ArticleViews.detail, name='article_detail'),    
    
    (r'^ajax/preview/(?P<id>\d+)/$', ajax_preview),
    (r'^ajax/save/(?P<id>\d+)/$', ajax_save),
    (r'^publish/(?P<id>\d+)/$', publish),
    (r'^unpublish/(?P<id>\d+)/$', unpublish),
    
    # list the articles
    url(r'^$', ArticleViews.list, name='article_list'), 
    url(r'^(?P<order>\w+)/$', ArticleViews.list,name='article_list' ), 
    )
