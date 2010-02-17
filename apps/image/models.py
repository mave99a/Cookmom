from flickrapi import FlickrAPI
from flickrsettings import *

def upload_to_flickr(filename, bits, type):
    flickr = FlickrAPI(api_key = FLICKR_API_KEY, secret = FLICKR_SECRET, token = FLICKR_TOKEN, cache=False)
    f = flickr.uploadbits(filename, bits, type)
    res = flickr.photos_getSizes(photo_id = f.photoid[0].text)
    return res.sizes[0].size[3].attrib['source']