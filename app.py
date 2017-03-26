'''

Back end for GeoBoards project

'''
#imports
from bottle import Bottle, request, run

from db import DB
from posts import Post, Location
from data_fixer import clean_lat,clean_long
from data_fixer import dejsonify_posts

import json
#########################################################
api = Bottle()
database = DB()

#returns posts
@api.get('/getposts/<lat>/<long>')
def get_posts(lat,long):

    lat = clean_lat(lat)
    long = clean_long(long)

    print str(lat) + ' ' + str(long)

    #should return the posts at lat,long
    posts_ = database.find_at(lat,long)

    posts = []
    for post in posts_:
        p = dict()
        p['postContent'] = post.post_content
        p['postID'] = post.id
        p['dispName'] = post.owner_display_name
        p['userID'] = post.owner_display_id
        p['timeRemaining'] = post.time_left
        p['location'] = dict()
        p['location']['latitude'] = post.location.latitude
        p['location']['longitude'] = post.location.longitude
        p['location']['altitude'] = post.location.altitude
        p['location']['timestamp'] = post.location.timestamp
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
    post_dict = request.json
    #post_dict = dejsonify_posts(post_json)
    #id,location,body,owner_disp,owner_id
    lat = post_dict['location']['latitude']
    long = post_dict['location']['longitude']
    alt = post_dict['location']['altitude']
    timestamp = post_dict['location']['timestamp']
    post = Post(database.gen_id(), \
                Location(lat,long,alt,timestamp), \
                post_dict['postContent'], \
                post_dict['dispName'], \
                post_dict['userID'])
    database.add(post.id,post)
    return 'added!'

@api.get('/dumpdb')
def dump():
    database.dump()
    return 'k'

@api.get('/user/<user>')
def get_user(user):
    usr = database.get_user(user)

run(api, host='192.241.134.224',port=80)