#!/usr/bin/env python3
# coding: utf-8

import rospy
import Arm_Lib
from math import pi
from sensor_msgs.msg import JointState

RA2DE = 180 / pi


def topic(msg): # Create a subscriber callback function

    if not isinstance(msg, JointState): return
    
    # Define the joint angle container, the last one is the angle of the gripper, 
    # the default gripper does not move is 0
    # The gripper does not participate in the positive and negative solution of the movement, 
    # it needs to be controlled separately. Do not set the No.6 servo to 0°
    joints = [0.0, 0.0, 0.0, 0.0, 0.0, 90.0]

    # Convert the received angle in radian [-1.57,1.57] to degree [0,180]
    for i in range(5): joints[i] = (msg.position[i] * RA2DE) + 90

    sbus.Arm_serial_servo_write6_array(joints, 100)


if __name__ == '__main__':
    sbus = Arm_Lib.Arm_Device()
    rospy.init_node("ros_dofbot")
    # Create a subscriber
    subscriber = rospy.Subscriber("/joint_states", JointState, topic)
    rate = rospy.Rate(2)
    rospy.spin()
