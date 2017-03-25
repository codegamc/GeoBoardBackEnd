'''
Posts class for backend
'''



class Post(object):
    def __init__(self,id,x,y,z,body,owner):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.body = body
        self.owner = owner