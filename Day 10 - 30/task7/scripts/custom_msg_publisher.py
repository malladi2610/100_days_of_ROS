#!/usr/bin/env python

import rospy
from task7_custom_messages.msg import custommessage

def custommsgPublisher():
    cm_publisher = rospy.Publisher('custom_msg_info', custommessage, queue_size=10)
    rospy.init_node('custom_msg_publisher', anonymous=False)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = custommessage()
        msg.name = "sensor1"
        msg.number = 1.0
        cm_publisher.publish(msg)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        custommsgPublisher()
    except rospy.ROSInterruptException:
        pass
