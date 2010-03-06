# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import delete_object, update_object
from generic_view_patch.create_update import create_object
from renderhelpers.renderblock import direct_block_to_template
from renderhelpers.decorators import AutoResponse

from models import Article, ArticleForm
from auth.decorators import login_required
from people.models import User


def list_article(request, order=None):
    if order is None: 
        queryset = Article.get_latest()
        extracontext = {'latest':True}
    elif order == 'discuss':
        queryset = Article.get_most_discussed()
        extracontext = {'discuss':True}
    elif order == 'favorite':
        queryset = Article.get_most_favorited()
        extracontext = {'favorite':True}
    else:
       raise Http404('Sort order not found: %s' % order) 
    return object_list(request, queryset, paginate_by = 10, extra_context= extracontext)


@AutoResponse(template='article/article_detail.html', autoAjax=False, redirectBack=False)
def show_article(request, id, title=None):
    object = Article.get_by_id(int(id))
    return locals()

@login_required
def new_article(request):
    drafts_count = Article.all().filter('author =', request.current_user).filter('published =', False).count()
    MAX_ALLOW_DRAFTS = 5
    if drafts_count < MAX_ALLOW_DRAFTS : 
        new_draft = Article(published=False, author=request.current_user)
        new_draft.put()
        return edit_article(request, new_draft.id())

@login_required
def edit_article(request, id):
    return update_object(request, object_id=id, form_class=ArticleForm, template_name='article/edit.html')

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