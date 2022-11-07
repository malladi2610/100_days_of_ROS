#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I read the message %s from arduino", data.data)

def arduino_subscriber():
    
    rospy.init_node('arduino_subscriber', anonymous = True)
    
    rospy.Subscriber("chatter", String, callback)
    
    rospy.spin()
    
if __name__ == '__main__':
    arduino_subscriber()