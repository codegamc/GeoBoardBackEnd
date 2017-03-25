'''

Back end for GeoBoards project

'''
#imports
from bottle import Bottle, request, run

from db import DB
from posts import Post
from data_fixer import normalize_lat,normalize_long
from data_fixer import dejsonify_posts

import json
#########################################################
api = Bottle()
database = DB()

#returns posts
@api.get('/getposts/<lat>/<long>')
def get_posts(lat,long):

    lat = normalize_lat(lat)
    long = normalize_long(long)

    print lat + ' ' + long

    #should return the posts at lat,long
    posts_ = database.find_at(lat,long)

    posts = []
    for post in posts_:
        p = dict()
        p['postContent'] = post.post_content
        p['postID'] = post.id
        p['dispName'] = post.owner_display_name
        p['userID'] = post.owner_display_id
        p['location'] = dict()
        p['location']['latitude'] = post.location.latitude
        p['location']['longitude'] = post.location.longitude
        p['location']['altitude'] = post.location.altitude
        posts.append(p)

    return_dict = {}
    return_dict['posts'] = posts
    return_dict['latitude'] = lat
    return_dict['longitude'] = long

    return json.dumps(return_dict)


@api.post('/newpost')
def new_post():
    #saves new post to db

    print request
    print request.json
    print ''
    post_dict = request.json
    #post_dict = dejsonify_posts(post_json)
    post_dict['location'] = dict()
    post_dict['location']['latitude'] = request.json['location']['latitude']
    post_dict['location']['longitude'] = request.json['location']['longitude']
    post_dict['location']['altitude'] = request.json['location']['altitude']
    #id,location,body,owner_disp,owner_id
    post = Post(database.gen_id(), \
                post_dict['location'], \
                post_dict['postContent'], \
                post_dict['dispName'], \
                post_dict['userID'])
    database.add(post.id,post)
    return 'added!'

@api.get('/dumpdb')
def dump():
    database.dump()
    return 'k'

run(api, host='192.241.134.224',port=80)