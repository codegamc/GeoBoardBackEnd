'''

Back end for GeoBoards project

'''
#imports
from bottle import Bottle, request


#########################################################
api = Bottle()

@api.get('/getposts')
def get_posts():
    #returns posts
    print request

@api.post('/newpost'):
def new_post():
    #saves new post to db
    print request

@