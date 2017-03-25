'''

manual database to store data, real fast/hacky

'''
#imports
from posts import Post

class DB(object):
    def __init__(self):
        self.data = dict()
        self.last_gen = 0

    def find_at(self,x,y,z):
        ret = []
        model = Post(0,x,y,z,'','')
        for post in self.data.values():
            if(self.equal_enough(model,post)):
                ret.append(post)
        return ret

    #usef for finding "close enough to be the same general area" locations
    def equal_enough(self,a,b):
        return True

    def add(self,id,obj):
        self.data[id] = obj

    def dump(self):
        for post in self.data.values():
            print post.id
            print post.body
            print post.x

    def gen_id(self):
        self.last_gen = 1 + self.last_gen
        return self.last_gen
