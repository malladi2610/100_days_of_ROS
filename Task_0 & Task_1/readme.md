# Learning Objectives
## Task 0
1. Understanding the working of the publisher and subscriber 
2. Explanation by flowchart, rqt_graph and pblishing and subscribing the messages


## Task 1
1. Understanding the working of the turtlesim
2. nodes and topics which are running while the turtlesim is working
3. Publishing values to the /turtle1/cmd_vel topic to move the turtle in the desired direction or shape

# Tools Used
## Task 0
1. Terminal 

## Task 1
1. Turtlesim

# Procedure
## Task 0
1. In this one subscriber and publisher nodes X publisher and Y subscriber respectively
2. X publisher is publishing to the topic X channel
3. Y subscriber is subscribing to the X channel to see what X publisher is publishing
4. All this is controlled by  a rosmater which is started by roscore

## Task 1
1. The topic which is responsible to the motion of the turtle in turtlesim is /turtle1/cmd_vel, and it takes geometric msgs as input i.e geometry_msgs/Twist
2. Now a node needs to be created which publishes the  geometry_msgs/Twist to the /turtle1/cmd_vel
3. Once the above steps are done, run the node and turtle moves in your desired direction

# Result

1. https://youtu.be/FotZenL4pMA
