# -*- coding: utf-8 -*-
from google.appengine.ext import db

from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import delete_object, update_object
from generic_view_patch.create_update import create_object
from models import Comment, CommentForm
from people.models import User

def list_comment(request):
    return object_list(request, Comment.all(), paginate_by = 10)

def new_comment(request, key):
    target = db.get(key)
    return create_object(request, 
                         form_class=CommentForm, 
                         extra_fields = {'author': User.get_current_user(), 'target': target},
                         extra_context = locals()
                        )
    
def show_comment(request, key):
    return object_detail(request, Comment.all(), key)