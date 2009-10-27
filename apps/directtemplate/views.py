from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound
from django.template import RequestContext
from datetime import datetime

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
    
    now = datetime.now()
    activities = [{'templatename':'activity', 
                   'user': {'name': 'Robert Mao', 'url': '/', 'img_url':'http://a1.twimg.com/profile_images/205153778/Suzie_0001s_normal.jpg', 'templatename':'user'},
                   'time': now,
                   'content' :'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc congue ipsum vestibulum libero. Aenean vitae justo. Nam eget tellus. Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus',
                  }, 
                  {'templatename':'activity', 
                   'user': {'name': 'Robert', 'url': '/', 'img_url':'http://a3.twimg.com/profile_images/82806383/remysharp_normal.jpg', 'templatename':'user'},
                   'time':now,
                   'content' :'Lsectetuer adipiscing elit Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc congue ipsum vestibulum libero. Aenean vitae justo. Nam eget tellus. Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus. Nunc congue ipsum vestibulum libero. Aenean vitae justo. Nam eget tellus. Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus',
                  }, 
                  {'templatename':'activity', 
                   'user': {'name': 'Mary Penston', 'url': '/', 'img_url':'http://a3.twimg.com/profile_images/374652761/IMG_6122_2_bigger.JPG', 'templatename':'user'},
                   'time':now,
                   'content' :'Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus',
                  } 
                 ]
    comments = [1,2,3]
    articles = [1,2,3,4]
       
    return render_to_response(template, locals(), RequestContext(request))    
