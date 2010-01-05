from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    
    return render_to_response('cookmom/home.html',
                              context_instance=RequestContext(request))

def toprecipes(request):
    return render_to_response('cookmom/toprecipes.html', 
                              context_instance=RequestContext(request))