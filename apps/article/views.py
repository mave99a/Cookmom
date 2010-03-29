# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from renderhelpers.renderblock import direct_block_to_template

from renderhelpers.decorators import AutoResponse
from models import Article, ArticleForm
from auth.decorators import login_required
from people.models import User
from GAEGenericViews.genericviews import *

class ArticleViews(GenericViews):
    model = Article
    form = ArticleForm
    
    @classmethod
    def list(cls, request, order=None):
        if order is None: 
            queryset = Article.get_latest()
            latest = True
        elif order == 'discuss':
            queryset = Article.get_most_discussed()
            discuss = True
        elif order == 'favorite':
            queryset = Article.get_most_favorited()
            favorite = True
        else:
           raise Http404('Sort order not found: %s' % order) 
        
        return GenericViews.list(request, queryset)

@login_required
def new_article(request):
    drafts_count = Article.all().filter('author =', request.current_user).filter('published =', False).count()
    MAX_ALLOW_DRAFTS = 5
    if drafts_count < MAX_ALLOW_DRAFTS : 
        new_draft = Article(title='Untitled', content='', published=False, author=request.current_user)
        new_draft.put()
        return edit_article(request, new_draft.id())
    
@login_required
def ajax_save(request, id):
    return update_object(request, object_id=id, form_class=ArticleForm)

@login_required
@AutoResponse(autoAjax=True, redirectBack=True)
def publish(request, id):
    object = Article.get_by_id(int(id))
    object.published = True
    object.put()
    return {'success':True}

@login_required
@AutoResponse(autoAjax=True, redirectBack=True)
def unpublish(request, id):
    object = Article.get_by_id(int(id))
    object.published = False
    object.put()
    return {'success':True}
    
@login_required
def ajax_preview(request, id):
    object = Article.get_by_id(int(id))
    return direct_block_to_template(request, 'article/article_detail.html', 'article', {'object': object})   