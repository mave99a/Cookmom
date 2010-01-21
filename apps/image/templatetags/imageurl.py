'''
    generate the URL of uploaded images
'''

import logging
from django import template

register = template.Library()

mock_images = {
    '0': {'small':'http://farm4.static.flickr.com/3269/2406169080_1e1cd8b94c.jpg_m.jpg', 
          'square':'http://farm4.static.flickr.com/3269/2406169080_1e1cd8b94c.jpg_s.jpg',
          'medium':'http://farm4.static.flickr.com/3269/2406169080_1e1cd8b94c.jpg'}, 
    '1': {'small':'http://farm4.static.flickr.com/3280/2638831430_afc0b9108f_m.jpg', 
          'square':'http://farm4.static.flickr.com/3280/2638831430_afc0b9108f_s.jpg',
          'medium':'http://farm4.static.flickr.com/3280/2638831430_afc0b9108f.jpg'}, 
    '2': {'small':'http://farm4.static.flickr.com/3205/2649428782_395e0f2ce4_m.jpg',
          'square':'http://farm4.static.flickr.com/3205/2649428782_395e0f2ce4_s.jpg',
          'medium':'http://farm4.static.flickr.com/3205/2649428782_395e0f2ce4.jpg'},
    '3':{'small':'http://farm4.static.flickr.com/3120/2648597373_3632591cd2_m.jpg',
         'square':'http://farm4.static.flickr.com/3120/2648597373_3632591cd2_s.jpg',
         'medium':'http://farm4.static.flickr.com/3120/2648597373_3632591cd2.jpg'},
    '4':{'small':'http://farm4.static.flickr.com/3050/2648597531_e06b09b06b_m.jpg',
         'square':'http://farm4.static.flickr.com/3050/2648597531_e06b09b06b_s.jpg',
         'medium':'http://farm4.static.flickr.com/3050/2648597531_e06b09b06b.jpg'},
    '5':{'small':'http://farm4.static.flickr.com/3099/2609817549_44bc45ec35_m.jpg',
         'square':'http://farm4.static.flickr.com/3099/2609817549_44bc45ec35_s.jpg',
         'medium':'http://farm4.static.flickr.com/3099/2609817549_44bc45ec35.jpg'},
    '6':{'small':'http://farm4.static.flickr.com/3112/2573385064_f7536c53d8_m.jpg',
         'square':'http://farm4.static.flickr.com/3112/2573385064_f7536c53d8_s.jpg',
         'medium':'http://farm4.static.flickr.com/3112/2573385064_f7536c53d8.jpg'},
    '7':{'small':'http://farm3.static.flickr.com/2578/4128683519_79620197e1_m.jpg',
         'square':'http://farm3.static.flickr.com/2578/4128683519_79620197e1_s.jpg',
         'medium':'http://farm3.static.flickr.com/2578/4128683519_79620197e1.jpg'},
    '8':{'small':'http://farm5.static.flickr.com/4020/4292238132_e71222b2dc_m.jpg',
         'square':'http://farm5.static.flickr.com/4020/4292238132_e71222b2dc_s.jpg',
         'medium':'http://farm5.static.flickr.com/4020/4292238132_e71222b2dc.jpg'},
    '9':{'small':'http://farm3.static.flickr.com/2525/4290021187_a8f9aecd02_m.jpg',
         'square':'http://farm3.static.flickr.com/2525/4290021187_a8f9aecd02_s.jpg',
         'medium':'http://farm3.static.flickr.com/2525/4290021187_a8f9aecd02.jpg'},
    '10':{'small':'http://farm3.static.flickr.com/2788/4275019793_5ae0ba27cf_m.jpg',
         'square':'http://farm3.static.flickr.com/2788/4275019793_5ae0ba27cf_s.jpg',
         'medium':'http://farm3.static.flickr.com/2788/4275019793_5ae0ba27cf.jpg'},
    '11':{'small':'http://farm5.static.flickr.com/4062/4268079021_616362af89_m.jpg',
         'square':'http://farm5.static.flickr.com/4062/4268079021_616362af89_s.jpg',
         'medium':'http://farm5.static.flickr.com/4062/4268079021_616362af89.jpg'},
    '12':{'small':'http://farm1.static.flickr.com/177/397671997_444c036cb1_m.jpg',
         'square':'http://farm1.static.flickr.com/177/397671997_444c036cb1_s.jpg',
         'medium':'http://farm1.static.flickr.com/177/397671997_444c036cb1.jpg'},
}

class ImageURLNode(template.Node):
    def __init__(self, image_ref, size):
        self.image_ref = template.Variable(image_ref)
        self.size = size
        
    def render(self, context):
        imageid = self.image_ref.resolve(context)
        try: 
            if imageid is not None:
                # TBD, query DB to generate the URL of image 
                return mock_images[imageid][self.size]
        except:
            return mock_images['0'][self.size]

def do_imageurl_tags(parser, token):
    tokens = token.contents.split()
    params_len = len(tokens)
    if params_len < 2:
        raise template.TemplateSyntaxError("%r tag usage: { show_tags  object}" % tokens[0])
    if (params_len > 2):
        size = tokens[2]
    else:
        size = 'small'
    return ImageURLNode(tokens[1], size)

register.tag('imageurl', do_imageurl_tags)