'''

Back end for GeoBoards project

'''
#imports
from bottle import Bottle, request, run

from db import DB
from posts import Post
from data_fixer import normalizeX,normalizeY,normalizeZ
from data_fixer import dejsonify_posts

import json
#########################################################
api = Bottle()
database = DB()

#returns posts
@api.get('/getposts/<x>/<y>/<z>')
def get_posts(x,y,z):

    x = normalizeX(x)
    y = normalizeY(y)
    z = normalizeZ(z)

    print x + ' ' + y + ' ' + z

    #should return the posts at x,y,z
    posts = database.find_at(x,y,z)

    return_dict = json.loads(posts)
    return_dict['x'] = x
    return_dict['y'] = y
    return_dict['z'] = z

    return_dict['is_empty'] = 'false'

    return json.dump(return_dict)


@api.post('/newpost')
def new_post():
    #saves new post to db

    print request
    print request.json
    print ''
    post_dict = request.json
    #post_dict = dejsonify_posts(post_json)
    post = Post(database.gen_id(),post_dict['x'],post_dict['y'],post_dict['z'],post_dict['body'])
    database.add(post.id,post)
    return 'added!'

@api.get('/dumpdb')
def dump():
    database.dump()
    return 'k'

run(api, host='127.0.0.1',port=3040)