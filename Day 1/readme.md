# Learning Objectives

1. Understanding the working of the turtlesim
2. nodes and topics which are running while the turtlesim is working
3. Publishing values to the /turtle1/cmd_vel topic to move the turtle in the desired direction or shape

# Tools Used

1. Turtlesim

# Procedure

1. The topic which is responsible to the motion of the turtle in turtlesim is /turtle1/cmd_vel, and it takes geometric msgs as input i.e geometry_msgs/Twist
2. Now a node needs to be created which publishes the  geometry_msgs/Twist to the /turtle1/cmd_vel
3. Once the above steps are done, run the node and turtle moves in your desired direction

# Result

1. video link