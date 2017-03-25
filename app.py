'''

Back end for GeoBoards project

'''
#imports
from bottle import Bottle, request, run

from db import DB
from posts import Post
from data_fixer import normalize_lat,normalize_long,normalize_alt
from data_fixer import dejsonify_posts

import json
#########################################################
api = Bottle()
database = DB()

#returns posts
@api.get('/getposts/<lat>/<long>/<alt>')
def get_posts(lat,long,alt):

    lat = normalize_lat(lat)
    long = normalize_long(long)
    alt = normalize_alt(alt)

    print lat + ' ' + long + ' ' + alt

    #should return the posts at lat,long
    posts_ = database.find_at(lat,long,alt)

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
    return_dict['altitude'] = alt

    return json.dumps(return_dict)


@api.post('/newpost')
def new_post():
    #saves new post to db

    print request
    print request.json
    print ''
    post_dict = request.json
    #post_dict = dejsonify_posts(post_json)
    post = Post(database.gen_id(),post_dict['x'],post_dict['y'],post_dict['z'],post_dict['body'], post_dict['owner'])
    database.add(post.id,post)
    return 'added!'

@api.get('/dumpdb')
def dump():
    database.dump()
    return 'k'

run(api, host='127.0.0.1',port=3000)