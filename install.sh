#!/bin/bash

original_dir=$(pwd)

echo ~/catkin_ws
cd ~/catkin_ws

echo catkin_make
catkin_make

echo cd "$original_dir/scripts"
cd "$original_dir/scripts"

for file in *; do
    if [ -f "$file" ]; then
        chmod +x "$file"
        echo "chmod +x $file"
    fi
done

cd "$original_dir/map"
for file in *; do
    if [ -f "$file" ]; then
        cp "$file" ~/
        echo "cp $file ~/"
    fi
done

echo export TURTLEBOT3_MODEL=burger
export TURTLEBOT3_MODEL=burger

echo source ~/catkin_ws/devel/setup.bash
source ~/catkin_ws/devel/setup.bash

cd "$original_dir"
