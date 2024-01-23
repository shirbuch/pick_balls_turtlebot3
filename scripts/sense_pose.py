#!/usr/bin/env python

from __future__ import print_function

import rospy
import std_msgs.msg
from pick_balls_turtlebot3.srv import SensePose,SensePoseResponse
from geometry_msgs.msg import Point, Pose
from gazebo_msgs.msg import ModelStates, ModelState
from tf.transformations import quaternion_from_euler, euler_from_quaternion

# todo fix duplicate from pick_object
def gps_location():
    # request a GPS like pose information from the Gazebo server
    rospy.loginfo("Requesting Global Robot Pose from Gazebo")
    model_state = rospy.wait_for_message("gazebo/model_states", ModelStates)
    me_pose = Pose()
    me_pose = model_state.pose[2]
    me_pose_angles = euler_from_quaternion([me_pose.orientation.x, me_pose.orientation.y, me_pose.orientation.z, me_pose.orientation.w])
    print('My pose is (x,y,theta): ')
    print(me_pose.position.x, me_pose.position.y, me_pose_angles[2])
    return me_pose.position.x, me_pose.position.y, me_pose_angles[2]

# Service logic
def sense_pose():
    print(f"sense_pose")
    x, y, theta = gps_location()
    h = std_msgs.msg.Header()
    h.stamp = rospy.Time.now() 
    return h, x, y

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