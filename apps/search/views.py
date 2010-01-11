from django.shortcuts import render_to_response
from django.template import RequestContext

def tagcloud(request):
    return render_to_response('tagging/tagcloud.html', locals(), 
                              context_instance=RequestContext(request))