'''

manual database to store data, real fast/hacky

'''
#imports
from posts import Post
from posts import Location
import time
import pickledb
import json

class DB(object):

    def __init__(self):
        self.data = dict()
        self.user_data = dict()
        self.db = pickledb.load('database.db',False)
        self.state = pickledb.load('state.db', False)
        self.last_gen = self.state.get('last_gen')

        print self.last_gen
        if not self.last_gen:
            self.last_gen = 0
            self.state.set('last_gen',0)
            print self.last_gen

        for post_key in self.db.getall():
            self.data[post_key]=self.db.get(post_key)

    def find_at(self,lat,long):
        ret = []
        loca = Location(lat,long,0,int(time.time()))
        model = Post(0,loca,'','','')
        for post in self.data.values():
            if(self.equal_enough(model,post)):
                ret.append(post)

        return ret

    #usef for finding "close enough to be the same general area" locations, ignore alt
    def equal_enough(self,a,b):
        return True

    def add(self,id,obj):
        self.data[id] = obj
        self.db.set(id,obj.to_dict())
        self.db.dump()

    def dump(self):
        self.db.dump()
        self.state.dump()
        for post in self.data.values():
            print post.id
            print post.owner_display_name
            print post.location.timestamp
            if len(post.post_content) > 40:
                str_out = post.post_content[0:39]
            else:
                str_out = post.post_content
            print str_out

    def gen_id(self):
        self.last_gen = int(self.last_gen) + 1
        self.state.set('last_gen',self.last_gen)
        self.state.dump()
        return self.last_gen

    def get_user(self,user):
        usr = self.user_data[user]
        return usr