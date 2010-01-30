from flickrapi import FlickrAPI

api_key='c315443b47446ac457add5a7130e90e2'
secret = '371d3d6c8b5db9c5'
token = '72157609015697950-4c07f7d7e8286b60'

def upload_to_flickr(filename, bits, type):
    flickr = FlickrAPI(api_key = api_key, secret = secret, token = token, cache=False)
    f = flickr.uploadbits(filename, bits, type)
    res = flickr.photos_getSizes(photo_id = f.photoid[0].text)
    return res.sizes[0].size[3].attrib['source']