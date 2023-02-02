#!/usr/bin/env python3
# coding: utf-8
import time 
from time import sleep
import rospy
from moveit_commander.move_group import MoveGroupCommander
from Arm_Lib import Arm_Device
from signal import pthread_kill, SIGTSTP
from math import pi
from sensor_msgs.msg import JointState
from std_msgs.msg import String, Float64
import threading, time

RA2DE = 180 / pi


def topic(msg):
   
    if not isinstance(msg, JointState): return
    # 30 is open, 140 is close
    joints = [0.0, 0.0, 0.0, 0.0, 0.0, 140.0]
   
    for i in range(5): joints[i] = (msg.position[i] * RA2DE) + 90
  
    # Set joints position
    sbus.Arm_serial_servo_write6_array(joints, 1000)

def move_left(): # Arm at left side
    print("move to left")
      
    # Set new joints position: arm upwards
    dofbot.set_joint_value_target([0.00, 0.00, 0.00, -1.57, -0.00]) 
    dofbot.go() # Perform action
    sleep(0.5)
      
    # Set new joints position: arm turn left
    dofbot.set_joint_value_target([-1.49, 0.00, 0.00, -1.57, -0.00]) 
    dofbot.go() # Perform action
    sleep(0.5)
    
def move_right(): # Arm at right side
    print("move to right")
      
    # Set new joints position: arm upwards
    dofbot.set_joint_value_target([0.00, 0.00, 0.00, -1.57, -0.00]) 
    dofbot.go() # Perform action
    sleep(0.5)
      
    # Set new joints position: arm turn right
    dofbot.set_joint_value_target([1.49, 0.00, 0.00, -1.57, -0.00]) 
    dofbot.go() # Perform action
    sleep(0.5)
    
def callback(data): # Receive the message
    if data.data == "paper":
        print("Subscribed paper")
        move_left()
         
    elif data.data == "plastic":
        print("Subscribed plastic")
        move_right()
        
         
if __name__ == '__main__':

    rospy.init_node("dofbot_set_move_side")
    
    dofbot = MoveGroupCommander("dofbot")
    
    dofbot.allow_replanning(True)
    
    dofbot.set_planning_time(5)
   
    dofbot.set_num_planning_attempts(10)
  
    dofbot.set_goal_position_tolerance(0.01)
  
    dofbot.set_goal_orientation_tolerance(0.01)
  
    dofbot.set_goal_tolerance(0.01)
    
    dofbot.set_max_velocity_scaling_factor(1)
  
    dofbot.set_max_acceleration_scaling_factor(1)
    
    sbus = Arm_Device()
    time.sleep(.1)
    rospy.Subscriber("/joint_states", JointState, topic)
    # Create another subscriber object to receive the garbage classification result
    rospy.Subscriber("arm_node", String, callback)
    rospy.spin()
