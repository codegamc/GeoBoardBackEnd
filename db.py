'''

manual database to store data, real fast/hacky

'''
#imports
from posts import Post

class DB(object):
    def __init__(self):
        self.data = dict()

    def find_at(self,x,y,z):
        ret = []
        model = Post(0,x,y,z,'')
        for post in self.data:
            if(self.equal_enough(model,post)):
                ret.append(post)
        return ret

    #usef for finding "close enough to be the same general area" locations
    def equal_enough(self,a,b):
        return True

    def add(self,id,obj):
        self.data[id] = obj
