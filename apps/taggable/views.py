# -*- coding: utf-8 -*-
from google.appengine.ext import db
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from renderblock.renderblock import direct_block_to_template
from models import *
from sys import maxint

def tagcloud(request):
    object_list = Tag.cloud(100).fetch(100)
    min = 1
    max = maxint
    
    # find out the max and min of the tag count
    for item in object_list:
        if item.count > max:
            max = item.count 
        if item.count < min:
            min = item.count
    
    step = (max - min)/6
    # calculate the size
    for item in object_list:
        item.cloudsize = (item.count - min) % step
        
    return render_to_response('taggable/tag_list.html', locals(), context_instance=RequestContext(request) )
    
def show_by_tag(request, tag):
    return object_list(request, Taggable.get_by_tag(tag), paginate_by = 10, 
                       extra_context={'tag':tag})

@login_required
def add_tags(request):
    key = request.REQUEST["target"]
    tags = request.REQUEST["tags"].split(',')
    obj = db.get(key)
    taggable = Taggable.add_tags(obj, tags)
    if taggable is not None:
        json = simplejson.dumps(taggable.tags)
    else:
        json='[]'
    return HttpResponse(json)

@login_required
def add_tags_form(request):
    try: 
        isAjax = request.REQUEST['isAjax']
        returnurl = None
    except: 
        try: 
            returnurl = request.REQUEST['returnurl']
        except: 
            returnurl = None
            
    key = request.REQUEST["target"]
    tags = request.REQUEST["tags"].split(',')
    obj = db.get(key)
    taggable = Taggable.add_tags(obj, tags)
    
    if returnurl is None: 
        return direct_block_to_template(request, 'taggable/tags.html', 'tags', {'taggable': taggable, 'isowner': True})
    else: 
        return HttpResponseRedirect(returnurl)
 
@login_required
def remove_tags(request):
    key = request.REQUEST["target"]
    tags = request.REQUEST["tags"].split(',')
    obj = db.get(key)
    taggable = Taggable.remove_tags(obj, tags)
    if taggable is not None:
        json = simplejson.dumps(taggable.tags)
    else:
        json='[]'
    return HttpResponse(json)


@login_required
def my_tags(request):
   return  HttpResponse('ok')