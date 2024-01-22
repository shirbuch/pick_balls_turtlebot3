#!/usr/bin/env python

from __future__ import print_function

import rospy
from pick_balls_turtlebot3.srv import PlaceObject,PlaceObjectResponse

# Service logic
def place_object(object):
    print(f"place_object: {object}")

def handle_place_object(req):
    try:
        place_object(req.object)
        return PlaceObjectResponse()
    except rospy.ROSInterruptException as e:
        print(f"Error: {e}")

def place_object_server():
    rospy.init_node('place_object_server')
    s = rospy.Service('place_object', PlaceObject, handle_place_object)
    print("Ready to place object.")
    rospy.spin()

if __name__ == "__main__":
    place_object_server()