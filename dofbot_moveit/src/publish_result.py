#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def read_result_from_file():
    # Read the result from the text file
    result_file = open("/home/dofbot/dofbot_ws/src/dofbot_moveit/src/garbage_result.txt", "r")
    result = result_file.read()
    result_file.close()
    txt = result.split(" ")
    garbage_type = txt[0].lower()
    # score = txt[1]
    return garbage_type

def garbage_node():
    # Initialize the ROS node
    rospy.init_node("garbage_node", anonymous=False)

    # Create a publisher for the arm node
    pub = rospy.Publisher("arm_node", String, queue_size=10)

    # Read the result from the file and publish it to the arm node
    garbage_type = read_result_from_file()
    rospy.sleep(10) # to enable the subscriber (arm_node) has enough time to start the program and receive the message
    pub.publish(garbage_type)
    rospy.loginfo("Detected " + garbage_type)


if __name__ == "__main__":
    try:
        garbage_node()
    except rospy.ROSInterruptException:
        pass
