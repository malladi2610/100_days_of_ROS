#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty

def arduino_publisher():
    rospy.init_node('arduino_publisher', anonymous = True)
    pub = rospy.Publisher('toggle_led', Empty, queue_size = 10)
    
    while not rospy.is_shutdown():
        rospy.loginfo("Trigger to turn ON/OFF the LED")
        pub.publish()
        
        rospy.sleep(5)
        
        
if __name__ == '__main__':
    try:
        arduino_publisher()
    except rospy.ServiceServiceException:
        pass
    
    
