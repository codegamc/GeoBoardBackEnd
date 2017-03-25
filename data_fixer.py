'''
normalizes data and does other things. messy, hcky but so what
'''

#import
import json

def normalizeX(coordinate):
    return coordinate

def normalizeY(coordinate):
    return coordinate

def normalizeZ(coordinate):
    return coordinate

def jsonify_post_arr(posts):
    posts_dict = {}
    posts_dict["posts"] = []
    for post in posts:
        post_dict = dict()

        post_dict['id'] = post.id

        post_dict['x'] = post.x
        post_dict['y'] = post.y
        post_dict['z'] = post.z

        post_dict['body'] = post.body

        posts_dict["posts"].append(post_dict)

    json_str = json.dumps(posts_dict)
    return json_str

def dejsonify_posts(post_json):
    print type(post_json)
    post_ = json.loads(post_json)
    return post_

