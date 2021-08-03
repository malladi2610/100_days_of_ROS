#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def motion():
    vel_msg = Twist()
    
    rospy.init_node('turtle_motion_triangle',anonymous = True)
    
    VELOCITY_PUBLISHER = rospy.Publisher('/turtlesim2/turtle1/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(1)
     
   
   
    
    rate.sleep()    
    for i in range(0,3):
        rospy.loginfo("Moving in a triangle")
        
        
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
        vel_msg.linear.x = 0
        vel_msg.angular.z = 3.14/3
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
        vel_msg.linear.x = 3
        vel_msg.angular.z = 0
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
        vel_msg.linear.x = 0
        vel_msg.angular.z = 3.14/3
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
       
        
if __name__ == '__main__':

    motion()