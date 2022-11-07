#!/usr/bin/env python

import rospy
from task7_custom_messages.msg import custommessage


def custommsgCallback(mymsg):
    rospy.loginfo('Distance reading from the %s is: %f',mymsg.name,mymsg.number)


def custommsgListner():

   
    rospy.init_node('custom_msg_subscriber', anonymous=False)

    rospy.Subscriber('custom_msg_info', custommessage, custommsgCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    custommsgListner()
