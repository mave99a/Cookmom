# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import delete_object, update_object
from generic_view_patch.create_update import create_object
from renderblock.renderblock import direct_block_to_template
from renderhelpers.decorators import AutoResponse

from models import Article, ArticleForm
from auth.decorators import login_required
from people.models import User


def list_article(request):
    return object_list(request, Article.all(), paginate_by = 10)

def show_article(request, id, title):
    return object_detail(request, Article.all(), object_id=id, extra_context={'isowner': True})

#@requirelogin
#@requireFullProfile
#@requireAccess
@login_required
def new_article(request):
    return create_object(request, form_class=ArticleForm,
        extra_fields = {'author': request.current_user})

@login_required
def edit_article(request, id):
    return update_object(request, object_id=id, form_class=ArticleForm)

@login_required
def delete_article(request, id):
    return delete_object(request, Article, object_id=id,
        post_delete_redirect=reverse(list_article)) 
    
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