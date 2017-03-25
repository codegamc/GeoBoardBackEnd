'''

Back end for GeoBoards project

'''
#imports
from bottle import Bottle, request, run
from db import DB
from data_fixer import normalizeX,normalizeY,normalizeZ
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


run(api, host='127.0.0.1',port=3000)