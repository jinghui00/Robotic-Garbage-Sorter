#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import cv2
import pytesseract

def bin_node():
    # Set the Tesseract path
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

    # Capture the main image
    capture = cv2.VideoCapture(0)

    # Create the publisher node
    pub = rospy.Publisher("arm_bin", String, queue_size=10)

    # Initialize the node
    rospy.init_node('bin_node', anonymous=True)
    
    # Set the rate at which to publish the result
    rate = rospy.Rate(10) # 10 Hz

    while True and not rospy.is_shutdown():
        # Read a frame from the video
        _, frame = capture.read()

        # Pre-process the frame (optional)
        frame = cv2.resize(frame, (640, 480))
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Run Tesseract OCR on the frame
        text = pytesseract.image_to_string(frame_gray)

        # Check for the keywords "paper" and "plastic"
        # Publish the result to the arm node
        if "paper" in text.lower():
            cv2.putText(frame, "Word \"Paper\" detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            pub.publish("Paper bin")
        elif "plastic" in text.lower():
            cv2.putText(frame, "Word \"Plastic\" detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            pub.publish("Plastic bin")

        # Display the results
        cv2.imshow("Frame", frame)
        
        rate.sleep()

        # Check if the user pressed "q" to quit
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    # Release the capture and destroy the windows
    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        bin_node()
    except rospy.ROSInterruptException:
        pass
