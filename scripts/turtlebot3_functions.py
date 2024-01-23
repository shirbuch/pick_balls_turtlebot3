#!/usr/bin/env python3
import rospy
import numpy as np
import random
import copy
import time

from environment_functions import spawn_model, delete_model, initialize_environment, create_scene




	


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

