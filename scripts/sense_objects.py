#!/usr/bin/env python

from __future__ import print_function

import rospy
from pick_balls_turtlebot3.srv import SenseObjects,SenseObjectsResponse
from pick_balls_turtlebot3.msg import Object

# Service logic
def sense_objects():
    print(f"sense_objects")
    return [Object("ball1", 1, 1), Object("ball2", 2, 2)]

def handle_sense_objects(req):
    try:
        objects = sense_objects()
        return SenseObjectsResponse(objects)
    except rospy.ROSInterruptException as e:
        print(f"Error: {e}")

def sense_objects_server():
    rospy.init_node('sense_objects_server')
    s = rospy.Service('sense_objects', SenseObjects, handle_sense_objects)
    print("Ready to sense objects.")
    rospy.spin()

if __name__ == "__main__":
    sense_objects_server()