# Robotic-Garbage-Sorter

**About**

This project is to develop a garbage collector and sorter robot.
It implements YOLOv5 deep learning model for garbage classification and using robotic arm to grasp and throw the garbage to the corresponding bin.
Garbage is put one by one in front of the camera for classification and grasping.


**Requirements**

Yahboom Dofbot Raspberry Pi 4B
Ubuntu 20.04
ROS noetic
Python 3.8.10

**Usage**

1. Download all the files and move them according to the directory. For example,
	* Go to dofbot_ws/src/dofbot_moveit.
	* Add yolov5.launch and yolov5_d435.launch to dofbot_ws/src/dofbot_moveit/launch.
	* Same goes to other files in other directories.

2. Ensure all files are executable.
	chmod +x <file_name>

3. To run the whole program, open a new terminal.
	cd dofbot_ws/src/dofbot_moveit/scripts
	./run.sh
	* This will run the bin detection and garbage classification on paper and plastic.




