from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    url(r'^new/$', ArticleViews.new_article, name='article_new'), 
    
    url(r'^edit/(?P<id>\d+)/$', ArticleViews.update, name='article_edit'),
    
    url(r'^dele/(?P<id>\d+)/$', ArticleViews.delete, name='article_delete'), 

    url(r'^(?P<id>\d+)/(?P<title>.+)/$', ArticleViews.detail, name='article_detail'),
    url(r'^(?P<id>\d+)/$', ArticleViews.detail, name='article_detail'),    
    
    url(r'^ajax/preview/(?P<id>\d+)/$', ArticleViews.ajax_preview, name='article_preview'),
    url(r'^ajax/save/(?P<id>\d+)/$', ArticleViews.ajax_save, name='article_save'),
    
    url(r'^publish/(?P<id>\d+)/$', ArticleViews.publish, name='article_publish'),
    url(r'^unpublish/(?P<id>\d+)/$', ArticleViews.publish, name='article_unpublish'),
    
    # list the articles
    url(r'^$', ArticleViews.list, name='article_list'), 
    url(r'^(?P<order>\w+)/$', ArticleViews.list,name='article_list' ), 
    )
