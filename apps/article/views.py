from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, update_object
from models import Article

def list_article(request):
    return object_list(request, Article.all(), paginate_by=10)

def show_article(request, key):
    return object_detail(request, Article.all(), key)