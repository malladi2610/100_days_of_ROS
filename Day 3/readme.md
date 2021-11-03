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

![terminal_output](images/terminal_output_publisher.png)


This is the final result

Video link : 

**Task 4: Blinking LED with python script**

1. Upload the blinking LED code in the Arduino examples provided in the ros_lib library
2. Now write a simple publisher node using python which will publish the Empty message on to the /toggleled topic which is being subscribed by the node which is running in the Arduino
3. The python snippet is as follows

```def arduino_publisher():
    rospy.init_node('arduino_publisher', anonymous = True)
    pub = rospy.Publisher('toggle_led', Empty, queue_size = 10)
    
    while not rospy.is_shutdown():
        rospy.loginfo("Trigger to turn ON/OFF the LED")
        pub.publish()
        
        rospy.sleep(5)
```

The code is ran by the same set of commands used in the above example

The terminal output is as follows

![terminal_output](images/terminal_output_subscriber.png)


