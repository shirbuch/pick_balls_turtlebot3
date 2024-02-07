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

### Gazebo installation:
1. https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/ - Choose Noetic and install 3.1.3, 3.1.4
2. https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/ - Choose Noetic and install 6.1.1

### Build:
0. ASUMMING THAT ROS / GAZEBO IS INSTALLED IN ~/catkin_ws , IF NOT PLEASE CHANGE IN INSTALL.SH
1. Unzip pick_balls_turtlebot3.zip into ~/catkin_ws/src
2. Open terminal and cd into (unzipped) pick_balls_turtlebot3
3. chmod +x install.sh
4. . install.sh (this is to compile and source the pick_balls_turtlebot3 package and chmod +x to all script files)
5. copy assignment2_env 2/assignment2_env/models into ~/catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models
6. copy assignment2_env 2/assignment2_env/worlds into ~/catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/worlds
7. copy assignment2_env 2/assignment2_env/launch into ~/catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/launch

### Run:
1. roslaunch pick_balls_turtlebot3 control.launch

