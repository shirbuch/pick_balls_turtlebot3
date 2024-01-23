#!/usr/bin/env python3
from gazebo_msgs.srv import SpawnModel, DeleteModel, DeleteModelRequest
import rospy
from gazebo_msgs.msg import ModelStates, ModelState
import time

def initialize_environment():
    rospy.init_node('turtlebot3_ff', anonymous=True, log_level=rospy.WARN)

def delete_model(name):
    # delete model
    srv = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
    req = DeleteModelRequest()
    req.model_name = name
    resp = srv(req)

  
def goal_checker():
    pass
    #TODO: return if the goal was fulfilles (all red balls collected and placed at the blue cube)  		


if __name__ == '__main__':
	initialize_environment()
	create_scene()	

	

