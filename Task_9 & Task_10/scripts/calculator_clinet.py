#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from task8_ros_services.srv import *

def cal_two_ints_client(x,y,s):
    rospy.wait_for_service('calculator_two_ints')
    try:
        srv = rospy.ServiceProxy('calculator_two_ints',calculator_two_ints)
        resp1 = srv(x,y,s)
        return resp1.sol
    except rospy.ServiceException as e:
        print("Services call failed : %s" %e)

def usage():
    return "%s [x y s]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
       x = int(sys.argv[1])
       y = int(sys.argv[2])
       print("THe valid operation:")
       print("For addition: a")
       print("For multiplication: m")
       print("For substraction: s")
       print("For division: d")
       s = str(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    if(s == 'a'):
        print("Requesting %s+%s"%(x,y))
        print("%s + %s = %s"%(x, y, cal_two_ints_client(x,y,s)))
    if(s == 's'):
        print("Requesting %s-%s"%(x,y))
        print("%s - %s = %s"%(x, y, cal_two_ints_client(x,y,s)))
    if(s == 'm'):
        print("Requesting %s*%s"%(x,y))
        print("%s * %s = %s"%(x, y, cal_two_ints_client(x,y,s)))
    if(s == 'd'):
        print("Requesting %s/%s"%(x,y))
        print("%s / %s = %s"%(x, y, cal_two_ints_client(x,y,s)))
    

    


    
    


