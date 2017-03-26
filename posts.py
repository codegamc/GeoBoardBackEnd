'''
Posts class for backend
'''
import json


class Post(object):
    def __init__(self,id,location,body,owner_disp,owner_id):
        self.id = id #postID
        self.location = location #location
        self.post_content = body #postContent
        self.owner_display_name = owner_disp #dispName
        self.owner_display_id = owner_id #userID
        self.time_left = 3600 #timeRemaining

    def to_dict(self):
        p = dict()
        p['postContent'] = self.post_content
        p['postID'] = self.id
        p['dispName'] = self.owner_display_name
        p['userID'] = self.owner_display_id
        p['timeRemaining'] = self.time_left
        p['location'] = dict()
        p['location']['latitude'] = self.location.latitude
        p['location']['longitude'] = self.location.longitude
        p['location']['altitude'] = self.location.altitude
        p['location']['timestamp'] = self.location.timestamp
        return p

def parse_dict(p):
        l = Location(0, 0, 0, 1)
        p_ = Post(0, l, '', '', '')

        try:


            p_.post_content = p['postContent']
            p_.id = p['postID']
            p_.owner_display_name = p['dispName']
            p_.owner_display_id = p['userID']
            p_.time_left = p['timeRemaining']

            p_.location.latitude = p['location']['latitude']
            p_.location.longitude = p['location']['longitude']
            p_.location.altitude = p['location']['altitude']
            p_.location.timestamp = p['location']['timestamp']

            return p_
        except:
            return p_


class Location(object):
    def __init__(self,lat,long,alt,timestamp):
        self.latitude = float(lat) #longitude
        self.longitude = float(long) #latitiude
        self.altitude = float(alt) #altitude
        self.timestamp = timestamp # altitude

class User(object):
    def __init__(self,uid, dispName):
        self.userID = uid
        self.display_name = dispName