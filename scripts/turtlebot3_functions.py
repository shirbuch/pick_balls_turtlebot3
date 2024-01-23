#!/usr/bin/env python3
import rospy
import numpy as np
import random
import copy
import time
from geometry_msgs.msg import Point, Pose
from gazebo_msgs.msg import ModelStates, ModelState
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from environment_functions import spawn_model, delete_model, initialize_environment, create_scene


def distance(x1, y1, x2, y2):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
    return dist


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


def find_objects():
    # request from Gazebo the global pose of all objects
    rospy.loginfo("Requesting Global Object Poses from Gazebo")
    model_state = rospy.wait_for_message("gazebo/model_states", ModelStates)
    number_of_objects = len(model_state.pose)  - 3 # ignore: [ground_plane, room1, turtlebot3_burger]    	  	   	
    print('I found ' +str(number_of_objects) +' Objects')
    print(model_state.name[3:])
    #print('They are at: ')
    #object_pose = []
    #for n in range(number_of_objects):
    #   object_pose.append(model_state.pose[3+n])
    #print(object_pose)
    return model_state.name[3:], model_state.pose[3:]


def pick_object(object_name, object_position):
	print('Trying to pick up: ' + object_name)
	me_pose = gps_location()
	object_x = object_position[0]
	object_y = object_position[1]	
	dist = distance(me_pose[0],me_pose[1],object_x,object_y)
	# TODO isEmpty = fcn_that_checks_that_nothing_is_in_the_knapsack() 
	if dist <.35 and isEmpty:
		delete_model(object_name)
		time.sleep(1)
		spawn_model(name=object_name, spawn_location=[0.0, -0.7, 1.0]) #put in knapsack
		time.sleep(1)
		print('...successfully.')
		
	else: 
		print('...unsuccessfully. Need to be closer to the object to pick it')
		


def place_object(object_name, place_location):
	# delete selected object from bag and place it in gazebo
	me_pose = gps_location()
	dist2 = distance(me_pose[0], me_pose[1], place_location[0], place_location[1])
	# TODO: isPicked = fcn_that_checks_if_object_is_picked(object_name)
	if not isPicked: 
		print('Object is not with me...')
		return False
	if dist2<.35:
		delete_model(object_name)
		spawn_model(name=object_name, spawn_location=place_location)
		print('Placed the object')
		return True
	else: 
		print('Need to be closer to the location to place the object (and NOT on it!)') 
		return False




if __name__ == '__main__':
    # example script that picks one of the balls and places it
    # set up environment
    initialize_environment()  
    #create_scene(True) # delete old env. if exists
    #create_scene(False) # set new environment
    
    # sense
    my_pose = gps_location()
    object_names, object_poses = find_objects()
    
    # navigate to pickup
    pick_object_name = 'red_ball0'
    print('I navigate to '+ pick_object_name)
    idx = object_names.index(pick_object_name) # find object pose by index
    pick_object_position = [object_poses[idx].position.x, object_poses[idx].position.y]
    pick_navigation_goal = [pick_object_position[0]-0.15,pick_object_position[1]-0.15]
    result = movebase_client(pick_navigation_goal[0],pick_navigation_goal[1],1.0)
    if result:
        rospy.loginfo("Goal execution done!")

    # pick
    pick_object(pick_object_name,pick_object_position)

    # navigate to dropoff 
    idx = object_names.index('blue_cube') # find blue_cube pose by index
    goal_object_position = [object_poses[idx].position.x, object_poses[idx].position.y]
    place_navigation_goal = [goal_object_position[0]+0.15,goal_object_position[1]+0.15]
    result = movebase_client(place_navigation_goal[0],place_navigation_goal[1],1.0)
    if result:
        rospy.loginfo("Goal execution done!")
        
    # place
    success = place_object(pick_object_name, [goal_object_position[0],goal_object_position[1],0.3])
    if success: print("Successfully moved the object")

