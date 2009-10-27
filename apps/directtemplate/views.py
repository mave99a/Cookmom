from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound
from django.template import RequestContext

def directtemplate(request, template):
    """
        for debug only 
        all templates can directly be accessed from URL
        ".html" extension can be omitted.
    """
    if (len(template) > 0) :
        if (template[-1] == '/'):
            template = template[0:-1];

        if (len(template) > 5):
            if (template[-5:].lower() !='.html'):
                template = template + '.html'
        else:
            template = template + '.html'
    else:
        template = 'home.html'
        
    ####################################
    #  mock data
    
    mainrecipe = {'name':'Chinese Noodle',
                  'author_name': 'Robert Mao',
                  'big_img_url' : 'http://farm4.static.flickr.com/3583/3435647617_34783451df.jpg?v=0',
                  'comments' : 10}
              
    hotrecipes = [{'name':'Chinese Rice',
                  'author_name': 'Alice',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3498/3469250432_71abdaa701_m.jpg',
                  'comments' : 1}, 
                  {'name':'Pizza',
                  'author_name': 'Jobs',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3333/3471038299_1b8ee440d2_m.jpg',
                  'comments' : 2},
                  {'name':'Toast Potato',
                  'author_name': 'Bill Williams',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3578/3483228007_9ae89f2fa5_m.jpg',
                  'comments' : 12},
                  {'name':'Red lobster',
                  'author_name': 'Joyce',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3531/3457438178_6abdb721ff_m.jpg',
                  'comments' : 2},
                  {'name':'Cookie',
                  'author_name': 'Yan Zhong',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3631/3481151195_e84b29316c_m.jpg',
                  'comments' : 27},
                  {'name':'Egg pie',
                  'author_name': 'Sam Ganer',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3342/3484170126_34390e3899_m.jpg',
                  'comments' : 19},
                  ]
    
    activities = [{'templatename':'activity', 
                   'user': {'username': 'Robert', 'url': '/', 'img_url':''},
                   'time':'',
                   'content' :'',
                  }, 
                  {'templatename':'activity', 
                   'user': {'username': 'Robert', 'url': '/', 'img_url':''},
                   'time':'',
                   'content' :'',
                  }, 
                  {'templatename':'activity', 
                   'user': {'username': 'Robert', 'url': '/', 'img_url':''},
                   'time':'',
                   'content' :'',
                  } 
                 ]
    comments = [1,2,3]
    articles = [1,2,3,4]
       
    return render_to_response(template, locals(), RequestContext(request))    
