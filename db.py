'''

manual database to store data, real fast/hacky

'''
#imports
from posts import Post, parse_dict
from posts import Location
import time
import pickledb
import json
import sys

class DB(object):

    def __init__(self):
        self.data = dict()
        self.user_data = dict()
        self.db = pickledb.load('database.db',True)
        self.state = pickledb.load('state.db', True)
        self.last_gen = self.state.get('last_gen')

        print self.last_gen
        if not self.last_gen:
            self.last_gen = 0
            self.state.set('last_gen',0)
            print self.last_gen

        #load up old data
        d = open('data.db')
        data_ = d.read()
        d.close()
        data = json.loads(data_)
        #print data
        #data is a dict
        posts_as_dicts = data['array']
        for post_ in posts_as_dicts:
            print post_
            post = parse_dict(post_)
            self.data[post.id] = post



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
        if hasattr(b,'to_dict'):
            return True
        else:
            return False

    def add(self,id,obj):
        self.data[id] = obj
        self.db.set(id,obj.to_dict())
        self.db.dump()

    def dump(self):
        self.db.dump()
        self.state.dump()
        for post in self.data.values():
            if hasattr(post,'id'):
                print post.id
                print post.owner_display_name
                print post.location.timestamp
                if len(post.post_content) > 40:
                    str_out = post.post_content[0:39]
                else:
                    str_out = post.post_content
                print str_out

        dict_arr = []
        for post in self.data.values():
            dict_arr.append(post.to_dict())

        save = dict()
        save['array'] = dict_arr
        save_ = json.dumps(save)

        f = open('data.db', 'r+')
        f.seek(0)
        f.write(save_)
        f.truncate()
        f.close()

    def gen_id(self):
        self.last_gen = int(self.last_gen) + 1
        self.state.set('last_gen',self.last_gen)
        self.state.dump()
        return self.last_gen

    def get_user(self,user):
        usr = self.user_data[user]
        return usr

    def rm(self,id):
        self.data.pop(id)
        self.db.rem(id)