# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from renderhelpers.renderblock import direct_block_to_template

from renderhelpers.decorators import AutoResponse
from models import Article, ArticleForm
from auth.decorators import login_required
from people.models import User
from GAEGenericViews.genericviews import *
from renderhelpers.decorators import method_adapter

class ArticleViews(GenericViews):
    model = Article
    form = ArticleForm
    
    @classmethod
    @GenericViews.response_as_list
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
        
        return queryset

    @classmethod
    @method_adapter(login_required)
    @method_adapter(AutoResponse(autoAjax=True, redirectBack=True))
    def publish(cls, request, id):
        object = cls.get_object_or_404(id)
        object.published = True
        object.put()
        return {'success':True}

    @classmethod
    @method_adapter(login_required)
    @method_adapter(AutoResponse(autoAjax=True, redirectBack=True))
    def unpublish(cls, request, id):
        object = cls.get_object_or_404(int(id))
        object.published = False
        object.put()
        return {'success':True}


    @classmethod
    @method_adapter(login_required)
    def new_article(cls, request):
        drafts_count = Article.all().filter('author =', request.current_user).filter('published =', False).count()
        MAX_ALLOW_DRAFTS = 5
        if drafts_count < MAX_ALLOW_DRAFTS : 
            new_draft = Article(title='Untitled', content='', published=False, author=request.current_user)
            new_draft.put()
            return cls.update(request, new_draft.id())
    
    @classmethod
    @method_adapter(login_required)
    def ajax_save(cls, request, id):
        return update_object(request, object_id=id, form_class=ArticleForm)


    @classmethod    
    @method_adapter(login_required)
    def ajax_preview(cls, request, id):
        object = cls.get_object_or_404(id)
        return direct_block_to_template(request, 'article/article_detail.html', 'article', {'object': object})   