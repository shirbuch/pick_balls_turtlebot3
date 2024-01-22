# pick_balls_turtlebot3 - Assignment 2 in Robotics Lab

### Info:
Services:
1. Navigate(x, y, theta)->none		: Navigate to a point
2. SensePose()->(x, y, header)		: Sense current robot pose
3. SenseObjects()->[Object]	: Return name and location of each object within the map
4. PickObject(Object)->none	: Pick nearby object (delete and spawn in the knapsack (outside the map))
5. PlaceObject(Object)->none	: Place the object (delete from knapsack and spawn it at the location)

Messages:
1. Object(name, x, y)

### Build:
1. Unzip pick_balls_turtlebot3.zip into ~/catkin_ws/src
2. open terminal and cd into (unzipped) pick_balls_turtlebot3
3. chmod +x install.sh
4. ./install.sh (this is to compile and source the pick_balls_turtlebot3 package and chmod +x to all script files)

### Run:
1. roslaunch pick_balls_turtlebot3 control.launch
