#!/usr/bin/env python
 
import rospy
import time
from std_msgs.msg import String
 
def tweet_publisher():
    count = 0
    rospy.init_node('X_publisher',anonymous = True)
    pub = rospy.Publisher('X_channel',String, queue_size=10)
    rate = rospy.Rate(10) #10hz
    
    while not rospy.is_shutdown():
        count = count + 1
        tweet_published_msg = "X has %s tweet about tech" % count
        rospy.loginfo(tweet_published_msg)
        pub.publish(str(count))
        
        time.sleep(1)
    
if __name__ == '__main__':
    try:
        tweet_publisher()
    except rospy.ROSInterruptException:
        pass