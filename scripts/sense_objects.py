#!/usr/bin/env python

from __future__ import print_function

import rospy
from pick_balls_turtlebot3.srv import SenseObjects,SenseObjectsResponse
from pick_balls_turtlebot3.msg import Object
from gazebo_msgs.msg import ModelStates, ModelState

def find_objects():
    # request from Gazebo the global pose of all objects
    rospy.loginfo("Requesting Global Object Poses from Gazebo")
    model_state = rospy.wait_for_message("gazebo/model_states", ModelStates)
    number_of_objects = len(model_state.pose) - 3 # ignore: [ground_plane, room1, turtlebot3_burger]    	  	   	
    print('I found ' + str(number_of_objects) +' Objects')
    names = model_state.name[3:]

    object_poses = []
    for n in range(number_of_objects):
      object_poses.append(model_state.pose[3+n])

    return names, object_poses

# Service logic
def sense_objects():
    print(f"sense_objects")
    names, poses = find_objects()
    
    objects = []
    for i in range(len(names)):
        objects.append(Object(names[i], poses[i].position.x, poses[i].position.y))

    return objects

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