#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I read the %s tweet of X on tech", data.data)

def tweet_subscriber():

    
    rospy.init_node('Y-subscriber',anonymous = True)
    
    rospy.Subscriber("X-Channel",String,callback)
    
    rospy.spin()
    
if __name__ == '__main__':
    tweet_subscriber()
    