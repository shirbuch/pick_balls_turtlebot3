#!/usr/bin/env python

from __future__ import print_function

import rospy
from pick_balls_turtlebot3.srv import SensePose,SensePoseResponse

# Service logic
def sense_pose():
    print(f"sense_pose")
    return 0, 0, 0

def handle_sense_pose(req):
    try:
        header, x, y = sense_pose()
        return SensePoseResponse(header, x, y)
    except rospy.ROSInterruptException as e:
        print(f"Error: {e}")

def sense_pose_server():
    rospy.init_node('sense_pose_server')
    s = rospy.Service('sense_pose', SensePose, handle_sense_pose)
    print("Ready to sense pose.")
    rospy.spin()

if __name__ == "__main__":
    sense_pose_server()