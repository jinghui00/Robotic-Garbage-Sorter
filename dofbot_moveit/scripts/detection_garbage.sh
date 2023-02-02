#!/bin/bash
echo "start camera"
roslaunch usb_cam usb_cam-test.launch &
sleep 20
echo "start garbage detection"
roslaunch dofbot_moveit yolov5.launch &
sleep 60
echo "done garbage detection" &
rosnode kill detect &
rosnode kill usb_cam &
rosnode kill image_view &
echo "killed camera and garbage detection"
sleep 10
echo"start rviz"
roslaunch dofbot_config demo.launch &
sleep 270
echo "start arm to move downward"
rosrun dofbot_moveit arm_move_down.py &
sleep 30
pkill -f "arm_move_down.py"
echo "killed arm_move_down"
sleep 10
echo "start gripper"
rosrun dofbot_moveit gripper_subscriber.py &
rosrun dofbot_moveit gripper_publisher.py &
sleep 20
#echo "adjust arm position"
#rosrun dofbot_moveit arm_move_up.py &
#sleep 30
#pkill -f "arm_move_up.py"
#echo "killed arm_move_up"
#sleep 10
echo "start arm to move to bin"
rosrun dofbot_moveit arm_move_leftright.py &
sleep 20
echo "start publish result"
rosrun dofbot_moveit publish_result.py &
sleep 60
pkill -f "arm_move_leftright.py"
echo "killed arm_move_leftright"
pkill -f "publish_result.py"
echo "killed publish_result"
sleep 10
echo "start gripper"
rosrun dofbot_moveit gripper_subscriber.py &
rosrun dofbot_moveit gripper_publisher.py &
sleep 20
echo "done gripper"
echo "back to center"
rosrun dofbot_moveit arm_move_up.py &
sleep 20
killall --exact roslaunch
killall --exact rosrun
rosnode kill -a
echo "done garbage segmentation process"
