from models import Article
def manage_draft(request):
    drafts = request.current_user.article_set.filter('published =', False)
    return drafts

def manage_published(request):
    drafts = request.current_user.article_set.filter('published =', True)
    return drafts

def similar(request):
    return Article.all().fetch(5)

def featured(request):
    return Article.get_featured()

def top(request):
    return Article.get_top()