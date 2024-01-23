#!/usr/bin/env python

from __future__ import print_function

import rospy
from pick_balls_turtlebot3.srv import *
from pick_balls_turtlebot3.msg import Object

OBJECT = Object("ball", 0, 0)

class Object:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

def navigate(x, y, theta):
    try:
        navigate_srv = rospy.ServiceProxy('navigate', Navigate)
        resp = navigate_srv(x, y, theta)
        return
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def pick_object(object):
    try:
        pick_object_srv = rospy.ServiceProxy('pick_object', PickObject)
        resp = pick_object_srv(object)
        return
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def place_object(object):
    try:
        place_object_srv = rospy.ServiceProxy('place_object', PlaceObject)
        resp = place_object_srv(object)
        return
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def sense_pose():
    try:
        sense_pose_srv = rospy.ServiceProxy('sense_pose', SensePose)
        resp = sense_pose_srv()
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def sense_objects():
    try:
        sense_objects_srv = rospy.ServiceProxy('sense_objects', SenseObjects)
        resp = sense_objects_srv()
        return
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

# Service logic
if __name__ == "__main__":
    rospy.wait_for_service('navigate')
    rospy.wait_for_service('pick_object')
    rospy.wait_for_service('place_object')
    rospy.wait_for_service('sense_pose')
    rospy.wait_for_service('sense_objects')

    print("=====================================")
    print("============  CONTROL  ===============")
    print("=====================================")

    print(f"=== Pose: {sense_pose()}\n===")
    navigate(1, 1, 1.0)
    print(f"=== Pose: {sense_pose()}\n===")
    navigate(0, 0, 3.0)
    print(f"=== Pose: {sense_pose()}\n===")
    # pick_object(OBJECT)
    # place_object(OBJECT)
    # sense_objects()
