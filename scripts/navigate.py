#!/usr/bin/env python

from __future__ import print_function

import rospy
from pick_balls_turtlebot3.srv import Navigate,NavigateResponse

# Service logic
def navigate(x, y, theta):
    print(f"navigate: {x}, {y}, {theta}")

def handle_navigate(req):
    try:
        navigate(req.x, req.y, req.theta)
        return NavigateResponse()
    except rospy.ROSInterruptException as e:
        print(f"Error: {e}")

def navigate_server():
    rospy.init_node('navigate_server')
    s = rospy.Service('navigate', Navigate, handle_navigate)
    print("Ready to navigate.")
    rospy.spin()

if __name__ == "__main__":
    navigate_server()