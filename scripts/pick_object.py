#!/usr/bin/env python

from __future__ import print_function

import rospy
from pick_balls_turtlebot3.srv import PickObject,PickObjectResponse

# Service logic
def pick_object(object):
    print(f"pick_object: {object}")

def handle_pick_object(req):
    try:
        pick_object(req.object)
        return PickObjectResponse()
    except rospy.ROSInterruptException as e:
        print(f"Error: {e}")

def pick_object_server():
    rospy.init_node('pick_object_server')
    s = rospy.Service('pick_object', PickObject, handle_pick_object)
    print("Ready to pick_object.")
    rospy.spin()

if __name__ == "__main__":
    pick_object_server()