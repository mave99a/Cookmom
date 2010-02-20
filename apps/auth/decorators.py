from django.http import HttpResponseRedirect
from functools import update_wrapper, wraps
from django.utils.http import urlquote

def login_required(view_function):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    def login_required_wrapper(request, *args, **kw):
        if request.authuser.is_authenticated():
            return view_function(request, *args, **kw)
        else:
            from django.conf  import settings
            login_url = settings.LOGIN_URL
            path = urlquote(request.get_full_path())
            return HttpResponseRedirect('%s?returnpath=%s' % (login_url, path))
            
    return wraps(view_function)(login_required_wrapper)
    