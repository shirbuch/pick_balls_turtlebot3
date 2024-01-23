#!/usr/bin/env python

from __future__ import print_function

import rospy
import actionlib
from pick_balls_turtlebot3.srv import Navigate,NavigateResponse
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client(x, y, w=1.0):
    # moves the robot collision free to a x,y,theta pose (must be valid/reachable in the map)
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.w = w
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

# Service logic
def navigate(x, y, theta):
    print(f"navigate: {x}, {y}, {theta}")
    movebase_client(x, y, theta)

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
