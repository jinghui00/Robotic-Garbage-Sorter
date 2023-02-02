#!/bin/bash
echo "start rviz"
roslaunch dofbot_config demo.launch &
sleep 270
echo "run bin detection"
rosrun dofbot_moveit bin_detect.py &
sleep 60
echo "move left"
rosrun dofbot_moveit arm_move_left.py &
sleep 60
echo "move right"
rosrun dofbot_moveit arm_move_right.py &
sleep 60
echo "done detection for two bins"
echo "back to center"
rosrun dofbot_moveit arm_move_up.py &
sleep 30
killall --exact roslaunch
killall --exact rosrun
rosnode kill -a
sleep 30
echo "done bin detection process"