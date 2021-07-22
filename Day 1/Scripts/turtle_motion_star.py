#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
pi = 3.14592654
def motion():
    vel_msg = Twist()
    
    rospy.init_node('turtle_motion_star',anonymous = True)
    
    VELOCITY_PUBLISHER = rospy.Publisher('/turtlesim3/turtle1/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(1)
     
    rate.sleep()
    
    for i in range(0,5):
        rospy.loginfo("Moving in a star")
        
        #Move
        vel_msg.linear.x = 3
        vel_msg.angular.z = 0
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
        #Stop
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
        
        #Rotate by 144 degrees
        vel_msg.linear.x = 0
        vel_msg.angular.z = (-4*pi)/5  
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()





       
       
        
if __name__ == '__main__':

    motion()