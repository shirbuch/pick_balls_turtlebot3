#!/usr/bin/env python3
from gazebo_msgs.srv import SpawnModel, DeleteModel, DeleteModelRequest
import rospy
from geometry_msgs.msg import Pose
from gazebo_msgs.msg import ModelStates, ModelState
import time

def initialize_environment():
    rospy.init_node('turtlebot3_ff', anonymous=True, log_level=rospy.WARN)

def spawn_model(name, file_location='/home/aos/.gazebo/models/objects/red_ball.sdf', spawn_location=[0.0,0.0,1.0]):
    #rospy.init_node('spawn_model', log_level=rospy.INFO)
    pose = Pose()
    pose.position.x = spawn_location[0]
    pose.position.y = spawn_location[1]
    pose.position.z = spawn_location[2]
    spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
    spawn_model_client(model_name=name,
                       model_xml=open(file_location, 'r').read(),
                       robot_namespace='/stuff', initial_pose=pose, reference_frame='world')

def delete_model(name):
    # delete model
    srv = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
    req = DeleteModelRequest()
    req.model_name = name
    resp = srv(req)


def create_scene():  
    delete_model('blue_cube') 
    time.sleep(1) 
    spawn_locations = [[1.25,0.9,0.2],[2.25,0.9,0.2],[-0.3,0,0.2],[3.0,-1.5,0.2]]      
    for n in range(len(spawn_locations)):
        delete_model('red_ball'+str(n)) 
        time.sleep(.5)
        spawn_model('red_ball'+str(n), '/home/aos/.gazebo/models/objects/red_ball.sdf', spawn_locations[n])
    spawn_model('blue_cube', '/home/aos/.gazebo/models/objects/blue_cube.sdf', [1.3,-0.5,1] ) 		
      
def goal_checker():
    pass
    #TODO: return if the goal was fulfilles (all red balls collected and placed at the blue cube)  		


if __name__ == '__main__':
	initialize_environment()
	create_scene()	

	

