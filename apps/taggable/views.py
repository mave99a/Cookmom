from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from models import *

def tagcloud(request):
    return render_to_response('taggable/tagcloud.html', locals(), 
                              context_instance=RequestContext(request))
    
def show_by_tag(request, tag):
    return object_list(request, Taggable.get_by_tag(tag), paginate_by = 10)
