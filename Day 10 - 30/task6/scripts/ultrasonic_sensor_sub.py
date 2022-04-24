#!/usr/bin/env python
import rospy

from task6_ultrasonicsensor.msg import ultrasonicmessage
from sensor_msgs.msg import Range

def sensorInfoCallback(data):
    rospy.loginfo('Distance reading from the sensor is : %f', data.range)
    
def sensorInfoListener():
    rospy.init_node('sensor_info_listener', anonymous = False)
    rospy.Subscriber('ultrasound_sensor',Range, sensorInfoCallback)
    
    rospy.spin()
    
if __name__ == '__main__':
    sensorInfoListener()
    
    