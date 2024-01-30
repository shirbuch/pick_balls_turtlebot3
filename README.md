# pick_balls_turtlebot3 - Assignment 2 in Robotics Lab

### Important:
For each configuration change please add "!!!" nearby so we will find it later
Read build last todo

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
4. . install.sh (this is to compile and source the pick_balls_turtlebot3 package and chmod +x to all script files)
// todo insert our_world launch and model to turtlebot3_gazebo
// todo save map files in root
// todo Update necesary configurations (speed - no, distance error - maybe):
  in src: grep -Rnw . -e '!!!'
  and update all changes here, currently all current configurations are in the configurtion_changes.txt (run command and paste in the file for each change)

### Run:
1. roslaunch pick_balls_turtlebot3 control.launch
// todo put together after finish coding and wait for each to load before continuing

### Notes to self:
# About changing speed:
# change max_vel_x, max_vel_trans, max_vel_theta in dwa_local_planner_params_burger

# no need for speed change, but has bad affect
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
