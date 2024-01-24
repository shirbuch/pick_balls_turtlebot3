#!/usr/bin/env python

from __future__ import print_function
from time import sleep

import rospy
import subprocess
from pick_balls_turtlebot3.srv import *
from pick_balls_turtlebot3.msg import Object
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import SpawnModel, DeleteModel, DeleteModelRequest

# todo make it work on installed env, fix duplicate from pick_object
GAZEBO_PATH = subprocess.getoutput("rospack find turtlebot3_gazebo")
BLUE_CUBE_NAME = "blue_cube"
SAFTY_DISTANCE = 0.05

class Object:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

def navigate(x, y, theta=1.0):
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
        return sense_pose_srv()
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def sense_objects():
    try:
        sense_objects_srv = rospy.ServiceProxy('sense_objects', SenseObjects)
        return sense_objects_srv()
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

# Init environment
# todo fix duplicate from pick_object and place_object
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

def create_scene():  
    spawn_locations = [[1.25,0.9,0.2],[2.25,0.9,0.2],[2.5,-1.5,0.2],[3.0,-1.5,0.2]] # todo make reachable random    
    for n in range(len(spawn_locations)):
        spawn_model('red_ball'+str(n), GAZEBO_PATH+'/models/objects/red_ball.sdf', spawn_locations[n])
    spawn_model(BLUE_CUBE_NAME, GAZEBO_PATH+'/models/objects/blue_cube.sdf', [1.3,-0.5,1] ) 		

# todo fix duplicate from pick_object and place_object
def delete_model(name):
    # delete model
    srv = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
    req = DeleteModelRequest()
    req.model_name = name
    resp = srv(req)

def clear_scene():
    # delete all models
    objects = sense_objects()
    for o in objects.objects:
        delete_model(o.name)

def reset_scene():
    clear_scene()
    navigate(0, 0, 1)

def pick_balls_main():
    reset_scene()
    create_scene()
    sleep(5)
    objects = sense_objects()
    
    blue_cube = None
    for i, o in enumerate(objects.objects):
        if o.name == BLUE_CUBE_NAME:
            blue_cube = objects.objects.pop(i)
            break
    
    if blue_cube is not None:
        for o in objects.objects:
            navigate(o.x-SAFTY_DISTANCE, o.y-SAFTY_DISTANCE)
            pick_object(o)
            navigate(blue_cube.x+SAFTY_DISTANCE, blue_cube.y+SAFTY_DISTANCE)
            place_object(Object(o.name, blue_cube.x, blue_cube.y))
    else:
        print("No blue cube found!")
        return
    
    navigate(0, 0, 1)

# todo: implement, return if the goal was fulfilles (all red balls collected and placed at the blue cube)
def goal_checker():
    pass

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

    pick_balls_main()
