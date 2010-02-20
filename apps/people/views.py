# -*- coding: utf-8 -*-
from django import forms
from ragendja.forms import FormWithSets, FormSetField
from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import delete_object
from generic_view_patch.create_update import update_object
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import User
from auth.decorators import login_required

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

@login_required
def show_myhome(request):
    return render_to_response('people/my.html',
                              {'object': request.current_user},
                              context_instance=RequestContext(request))
@login_required
def edit(request):
    return update_object(request, object_id=request.current_user.id(), form_class=UserForm)

#def delete_user(request, id):
#    return delete_object(request, User, object_id=id,
#        post_delete_redirect=reverse(list_user))    