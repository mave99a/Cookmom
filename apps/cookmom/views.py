from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime

def homepage(request):
   ####################################
    #  mock data
    
    mainrecipe = {'name':'Chinese Noodle',
                  'templatename':'mainrecipe',
                  'author_name': 'Robert Mao',
                  'big_img_url' : 'http://farm4.static.flickr.com/3583/3435647617_34783451df.jpg?v=0',
                  'comments' : 10}
              
    hotrecipes = [{'name':'Chinese Rice',
                   'templatename':'hotrecipe', 
                  'author_name': 'Alice',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3498/3469250432_71abdaa701_m.jpg',
                  'comments' : 1}, 
                  {'name':'Pizza',
                   'templatename':'hotrecipe',
                  'author_name': 'Jobs',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3333/3471038299_1b8ee440d2_m.jpg',
                  'comments' : 2},
                  {'name':'Toast Potato',
                   'templatename':'hotrecipe',
                  'author_name': 'Bill Williams',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3578/3483228007_9ae89f2fa5_m.jpg',
                  'comments' : 12},
                  {'name':'Red lobster',
                   'templatename':'hotrecipe',
                  'author_name': 'Joyce',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3531/3457438178_6abdb721ff_m.jpg',
                  'comments' : 2},
                  {'name':'Cookie',
                   'templatename':'hotrecipe',
                  'author_name': 'Yan Zhong',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3631/3481151195_e84b29316c_m.jpg',
                  'comments' : 27},
                  {'name':'Egg pie',
                   'templatename':'hotrecipe',
                  'author_name': 'Sam Ganer',
                  'medium_img_url' : 'http://farm4.static.flickr.com/3342/3484170126_34390e3899_m.jpg',
                  'comments' : 19},
                  ]
    
#    now = datetime.now()
#    activities = [{'templatename':'activity', 
#                   'user': {'name': 'Robert Mao', 'url': '/', 'img_url':'http://a1.twimg.com/profile_images/205153778/Suzie_0001s_normal.jpg', 'templatename':'user'},
#                   'time': now,
#                   'content' :'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc congue ipsum vestibulum libero. Aenean vitae justo. Nam eget tellus. Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus',
#                  }, 
#                  {'templatename':'activity', 
#                   'user': {'name': 'Robert', 'url': '/', 'img_url':'http://a3.twimg.com/profile_images/82806383/remysharp_normal.jpg', 'templatename':'user'},
#                   'time':now,
#                   'content' :'Lsectetuer adipiscing elit Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc congue ipsum vestibulum libero. Aenean vitae justo. Nam eget tellus. Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus. Nunc congue ipsum vestibulum libero. Aenean vitae justo. Nam eget tellus. Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus',
#                  }, 
#                  {'templatename':'activity', 
#                   'user': {'name': 'Mary Penston', 'url': '/', 'img_url':'http://a3.twimg.com/profile_images/374652761/IMG_6122_2_bigger.JPG', 'templatename':'user'},
#                   'time':now,
#                   'content' :'Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus',
#                  } 
#                 ]
#    comments = [{'templatename':'comment',
#                   'user': {'name': 'Robert Mao', 'url': '/', 'img_url':'http://a1.twimg.com/profile_images/205153778/Suzie_0001s_normal.jpg', 'templatename':'user'},
#                   'time': now,
#                    'content' :'Lsectetuer adipiscing elit Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc congue ipsum vestibulum libero. Aenean vitae justo. Nam eget tellus. Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus. Nunc congue ipsum vestibulum libero. Aenean vitae justo. Nam eget tellus. Etiam convallis, est eu lobortis mattis, lectus tellus tempus felis, a ultricies erat ipsum at metus',
#               }
#                ]
#    article =  {'templatename':'article',
#                'title' : 'How to cook noodle in 1 days',
#                'content' : 'hold on...',
#                'attachments': {
#                                'ingredients': [
#                                     {'templatename':'ingredient', 'name':'Pork', 'uniqname':'pork', 'volume': 10, 'unit':'lbs',  } ,          
#                                     {'templatename':'ingredient', 'name':'Sugar', 'uniqname':'pork', 'volume': 10, 'unit':'lbs',  } ,          
#                                     {'templatename':'ingredient', 'name':'Water', 'uniqname':'pork', 'volume': 10, 'unit':'lbs',  } ,          
#                                     {'templatename':'ingredient', 'name':'Green beans', 'uniqname':'pork', 'volume': 10, 'unit':'lbs',  } ,          
#                                     {'templatename':'ingredient', 'name':'Donkey', 'uniqname':'pork', 'volume': 10, 'unit':'lbs',  },           
#                                                ],
#                                'photos': {},
#                                'links': {},
#                                'video': {},
#                                'books': {}
#                                },
#                'author': {
#                'templatename':'author',
#                'user': {'name': 'Robert Mao', 'url': '/', 'img_url':'http://a1.twimg.com/profile_images/205153778/Suzie_0001s_normal.jpg', 'templatename':'user'},
#                 }
#                }

#    a = User(name='James Bond')
#    a.put()
#    x = Article(title='007 rocking recipes!', content='Bond, james bond! I just love it!!! yesyesyes!!! comen on man !', author = a)
#    x.put()
#    c = Comment(target=x, author=a, content="haha, this is comment")
#    c.put()
    
#    currentuser =  {'name': 'Robert Mao', 'url': '/', 'img_url':'http://a1.twimg.com/profile_images/205153778/Suzie_0001s_normal.jpg', 'templatename':'user'}; 
#    vote = {
#                'templatename':'vote',
#            }   
#    
    return render_to_response('cookmom/home.html', locals(), 
                              context_instance=RequestContext(request))

def toprecipes(request):
    return render_to_response('cookmom/toprecipes.html', locals(), 
                              context_instance=RequestContext(request)  )