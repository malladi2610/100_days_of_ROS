#!/usr/bin/env python

from __future__ import print_function 
import rospy
#Change the package name accorrdingly
from task8_ros_services.srv import calculator_two_ints,calculator_two_intsResponse

def handle_cal_two_ints(req):
    if(req.s == "a"):
        print("Returning [%s + %s = %s]"%(req.a,req.b,(req.a + req.b)))
        return calculator_two_intsResponse(req.a+req.b)
    if(req.s == "s"):
        # if(req.a > req.b):
        print("Returning [%s - %s = %s]"%(req.a,req.b,(req.a - req.b)))
        return calculator_two_intsResponse(req.a-req.b)
        # else:
        #     req.a = req.a + req.b
        #     req.b = req.a - req.b
        #     req.a = req.a - req.b
        #     print("Returning [%s - %s = -%s]"%(req.a,req.b,(req.b - req.a)))
        #     return calculator_two_intsResponse(req.a - req.b)
    if(req.s == "d"):
        print("Returning [%s / %s = %s]"%(req.a,req.b,(req.a / req.b)))
        return calculator_two_intsResponse(req.a/req.b)
    if(req.s == "m"):
        print("Returning [%s * %s = %s]"%(req.a,req.b,(req.a * req.b)))
        return calculator_two_intsResponse(req.a*req.b)
    
def cal_two_ints_server():
    rospy.init_node('calculator_two_ints_server')
    s = rospy.Service('calculator_two_ints',calculator_two_ints,handle_cal_two_ints)
    print("Ready to perform the calculator operation")
    rospy.spin()
    
#Main function
if __name__ == "__main__":
    cal_two_ints_server()