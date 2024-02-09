#!/usr/bin/env python3

from __future__ import print_function

import rospy
import time
import subprocess
from pick_balls_turtlebot3.srv import *
from pick_balls_turtlebot3.srv import PickObject,PickObjectResponse
from pick_balls_turtlebot3.msg import Object
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import SpawnModel, DeleteModel, DeleteModelRequest
from pick_balls_turtlebot3.srv import SensePose,SensePoseResponse
from gazebo_msgs.msg import ModelStates, ModelState
from tf.transformations import quaternion_from_euler, euler_from_quaternion

KNAPSACK_LOCATION = [0.0, -0.7, 1.0]

# todo make it work on installed env, fix duplicate from control
GAZEBO_PATH = subprocess.getoutput("rospack find turtlebot3_gazebo")

# todo fix duplicate from sense_pose or use sense_pose service
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

# todo fix duplicate from control and place_object
def spawn_model(name, file_location=GAZEBO_PATH+'/models/objects/red_ball.sdf', spawn_location=[0.0,0.0,1.0]):
    #rospy.init_node('spawn_model', log_level=rospy.INFO)
    pose = Pose()
    pose.position.x = spawn_location[0]
    pose.position.y = spawn_location[1]
    pose.position.z = spawn_location[2]
    spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
    spawn_model_client(model_name=name,
                       model_xml=open(file_location, 'r').read(),
                       robot_namespace='/stuff', initial_pose=pose, reference_frame='world')

# todo fix duplicate from control and place_object
def delete_model(name):
    # delete model
    srv = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
    req = DeleteModelRequest()
    req.model_name = name
    resp = srv(req)

# todo fix duplicate from place_object
def distance(x1, y1, x2, y2):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
    return dist

def nearby(x1, y1, x2, y2):
    dist = distance(x1, y1, x2, y2)
    return dist <.35

# todo fix duplicate from place_object
def knapsack_is_empty():
    print(f"Checking if knapsack is empty")
    rospy.wait_for_service('sense_objects')
    sense_objects_srv = rospy.ServiceProxy('sense_objects', SenseObjects)
    objects = sense_objects_srv().objects
    for o in objects:
        if nearby(KNAPSACK_LOCATION[0], KNAPSACK_LOCATION[1], o.x, o.y):
            return False
    
    return True

# Given code
def pick_object(object_name, object_x, object_y):
	print('Trying to pick up: ' + object_name)
	me_pose = gps_location()
	if nearby(me_pose[0], me_pose[1], object_x, object_y) and knapsack_is_empty():
		delete_model(object_name)
		time.sleep(1)
        # note that it will always spawn a red ball, if needed pass other model path
		spawn_model(name=object_name, spawn_location=KNAPSACK_LOCATION) # put in knapsack
		time.sleep(1)
		print('...successfully.')
		
	else: 
		print('...unsuccessfully. Need to be closer to the object to pick it or knapsack is full.')

# Service logic
def handle_pick_object(req):
    try:
        object = req.object
        print(f"pick_object: {object}")
        pick_object(object.name, object.x, object.y)
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