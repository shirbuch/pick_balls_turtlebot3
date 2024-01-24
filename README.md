# pick_balls_turtlebot3 - Assignment 2 in Robotics Lab

### todo:
1. in src: grep -Rnw . -e '!!!'
  and update all changes here, currently all current configurations are in the 
2. search for todo in code

### Info:
Services:
1. Navigate(x, y, theta)->none		: Navigate to a point
2. SensePose()->(header, x, y)		: Sense current robot pose
3. SenseObjects()->[Object]	      : Return name and location of each object within the map
4. PickObject(Object)->none	      : Pick nearby object (delete it and spawn in the knapsack (outside the map))
5. PlaceObject(Object)->none	: Place the object (delete from knapsack and spawn it at the location)

Messages:
1. Object(name, x, y)

### Build:
1. Unzip pick_balls_turtlebot3.zip into ~/catkin_ws/src
2. Open terminal and cd into (unzipped) pick_balls_turtlebot3
3. chmod +x install.sh
4. ./install.sh (this is to compile and source the pick_balls_turtlebot3 package and chmod +x to all script files)
5. todo check relevance: Change in: \catkin_ws\src\turtlebot3\turtlebot3_navigation\param\dwa_local_planner_params_burger.yaml
    # Goal Tolerance Parameters
    xy_goal_tolerance: 0.2 # 0.05
    yaw_goal_tolerance: 0.3 # 0.17

// todo insert our_world launch and model to turtlebot3_gazebo
// todo save map files in root

### Run:
// todo put together after finish coding and wait for each to load before continuing
1. roslaunch turtlebot3_gazebo turtlebot3_our_world.launch
2. roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
3. roslaunch pick_balls_turtlebot3 control.launch

### todo Change Speed:
in: \catkin_ws\src\turtlebot3\turtlebot3_navigation\param\dwa_local_planner_params_burger.yaml
  max_vel_x: 5 # 0.22
  max_vel_trans: 5 # 0.22
  max_vel_theta: 9 # 2.75


### Notes to self:
# About changing speed:
## original dwa_local_planner_params_burger and changed base_local_planner_params is not working
## changed dwa_local_planner_params_burger and original base_local_planner_params is working!!!

# no need for having affect, but might do
\catkin_ws\src\turtlebot3\turtlebot3_navigation\param\base_local_planner_params.yaml
  sim_time: 6 # 0.8
  vx_samples: 50 # 18

# has no affect!
by https://github.com/ROBOTIS-GIT/turtlebot3/issues/897
\catkin_ws\src\turtlebot3_simulations\turtlebot3_gazebo\include\turtlebot3_gazebo\turtlebot3_drive.h
 define LINEAR_VELOCITY  0.44 //0.3
 define ANGULAR_VELOCITY 2.2  //1.5

# has no affect!
\catkin_ws\src\turtlebot3\turtlebot3_navigation\param\base_local_planner_params.yaml
  max_vel_x: 9 # 0.18
  min_vel_x: 0.08

  max_vel_theta:  3 # 1.0