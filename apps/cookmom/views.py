from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    
    return render_to_response('cookmom/home.html', locals(), 
                              context_instance=RequestContext(request))

def toprecipes(request):
    return render_to_response('cookmom/toprecipes.html', locals(), 
                              context_instance=RequestContext(request)  )