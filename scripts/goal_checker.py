#!/usr/bin/env python3

import rospy
from pick_balls_turtlebot3.srv import GoalChecker, GoalCheckerResponse
from pick_balls_turtlebot3.srv import *

def goal_checker(x, y):
    rospy.wait_for_service('sense_objects')
    sense_objects_srv = rospy.ServiceProxy('sense_objects', SenseObjects)
    objects = sense_objects_srv().objects
    for o in objects:
        if o.x != x or o.y != y:
            return False
    return True

def handle_goal_checker(req):
    try:
        met = goal_checker(req.x, req.y)
        return GoalCheckerResponse(met)
    except rospy.ROSInterruptException as e:
        print(f"Error: {e}")

def goal_checker_server():
    rospy.init_node('goal_checker_server')
    s = rospy.Service('goal_checker', GoalChecker, handle_goal_checker)
    print("=====================================")
    print("====  CHECKING IF GOAL COMPLETED  ====")
    print("=====================================")
    rospy.spin()

if __name__ == "__main__":
    goal_checker_server()