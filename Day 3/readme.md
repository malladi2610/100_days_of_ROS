# Learning Objectives

**Task 3**

1. Reading the Hello world message by using a python script

**Task 4**

1. Toggling the led with python code instead of running the command from the terminal

# Tools Used

1. Arduino IDE
2. Arduino UNO
3. LED

# Procedure

**Task 3: Reading hello world with python script**

1. To read the hello world message being published by the arduino we need to subscribe to the topic to which it is publishing i.e chatter
2. Now we write a simple subscriber node which listens to the topic and prints the message it is reading in the terminal
3. The snippet of the subscriber node is as follows

```python
def callback(data):
    rospy.loginfo("I read the message %s from arduino", data.data)

def arduino_subscriber():
    
    rospy.init_node('arduino_subscriber', anonymous = True)
    
    rospy.Subscriber("chatter", String, callback)
    
    rospy.spin()
```

1. Run these commands

```arduino
roscore
```

```arduino
rosrun rosserial_python serial_node.py <Enter_your_port
_name>
```

This port name can be found in the Arduino IDE, Tools→port. 

Now run the subscriber node by the following the command

```arduino
rosrun <package_name> <python_file_name>

//For Example
rosrun day3 arduino_subscriber_hello_world.py //This is the command used in my case
```

![terminal_output](/Publisher_helloworld/Python_script/arduino_subscriber_hello_world.py)


This is the final result

**Task 4: Blinking LED with python script**

