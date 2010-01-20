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
    '7':{'small':'',
         'square':'',
         'medium':''},
    '8':{'small':'',
         'square':'',
         'medium':''},
    '9':{'small':'',
         'square':'',
         'medium':''},
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