#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

pi = 3.14592654
def motion():
    vel_msg = Twist()
    
    rospy.init_node('turtle_motion_square',anonymous = True)
    
    VELOCITY_PUBLISHER = rospy.Publisher('/turtlesim1/turtle1/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(1)
    
    rate.sleep()
    
    for i in range(0,4):
        rospy.loginfo("Moving in a square")
        
      
        
        vel_msg.linear.x = 3
        vel_msg.angular.z = 0
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
        vel_msg.linear.x = 0
        vel_msg.angular.z = 1.57
        VELOCITY_PUBLISHER.publish(vel_msg)
        rate.sleep()
        
    
        
if __name__ == '__main__':

    motion()

        