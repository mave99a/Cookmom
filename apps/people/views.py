# -*- coding: utf-8 -*-
from django import forms
from ragendja.forms import FormWithSets, FormSetField
from django.core.urlresolvers import reverse

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, update_object
from models import User

class UserForm(forms.ModelForm):    
    class Meta:
        model = User
UserForm = FormWithSets(UserForm)


def list_user(request):
    return object_list(request, User.all(), paginate_by=10)

def show_user(request, id):
    return object_detail(request, User.all(), object_id=id )

def show_user_detail(request, id, obj):
    template='people/user_detail_' + obj + '.html'
    return object_detail(request, User.all(), object_id=id, template_name=template)

def new_user(request):
    return create_object(request, form_class=UserForm)

def edit_user(request, id):
    return update_object(request, object_id=id, form_class=UserForm)

def delete_user(request, id):
    return delete_object(request, User, object_id=id,
        post_delete_redirect=reverse(list_user))    