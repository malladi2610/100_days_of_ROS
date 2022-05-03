#!/usr/bin/env python

import rospy
from task7_custom_messages.msg import custommessage


def custommsgCallback(mymsg):
    rospy.loginfo('Distance reading from the %s is: %f',mymsg.name,mymsg.number)


def custommsgListner():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'sensorInfoListener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('custom_msg_subscriber', anonymous=False)

    rospy.Subscriber('custom_msg_info', custommessage, custommsgCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    custommsgListner()
