'''
Posts class for backend
'''



class Post(object):
    def __init__(self,id,location,body,owner_disp,owner_id):
        self.id = id #postID
        self.location = location #location
        self.post_content = body #postContent
        self.owner_display_name = owner_disp #dispName
        self.owner_display_id = owner_id #userID
        self.time_left = 3600 #timeRemaining

class Location(object):
    def __init__(self,lat,long,alt):
        self.latitude = lat #longitude
        self.longitude = long #latitiude
        self.altitude = alt #altitude

