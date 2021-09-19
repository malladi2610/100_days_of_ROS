# Learning Objectives

**Task 2**

1. Making the Connection of Arduino with PC
2. Installing rosserial and ros lib
3. Trying the hello world example from the ROSSERIAL library

**Task 3**

1. Trying the blinking led example

# Tools Used

1. Arduino IDE
2. Arduino UNO
3. LED

# Procedure

**Task 2: Printing Hello world**

1. Installing the Arduino IDE from the official Arduino website: [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)
2. Following the steps in roswiki to setup Arduino and install the required libraries: [http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino IDE Setup](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup)
3. Then install the ros_lib into the Arduino environment, this is done by running the following commands. 

    **Note**: This needs to be done in your sketchbook folder. (It is found from file → preference → sketchbook location)

    ```arduino
    cd <sketchbook>/libraries
    rm -rf ros_lib
    rosrun rosserial_arduino make_libraries.py
    ```

4. This installs all the required dependencies required for ROS to work in the Arduino
5. Now select the example code: HelloWorld (This is a publisher node example), Follow this link to understand the HelloWorld code [http://wiki.ros.org/rosserial_arduino/Tutorials/Hello World](http://wiki.ros.org/rosserial_arduino/Tutorials/Hello%20World)
6. Upload it to the Arduino
7. It won't start working right away. You need to run the node
8. Run these commands

    ```arduino
    roscore
    ```

    ```arduino
    rosrun rosserial_python serial_node.py <Enter_your_port
    _name>
    ```

This port name can be found in the Arduino IDE, Tools→port. 

And **Voila!**

The message from the Arduino will be sent to the pc. This can be seen by running the command

```arduino
rostopic echo /chatter
```

![Screenshot from 2021-09-15 22-33-28.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/501839c5-6359-4976-af97-f79ee6779056/Screenshot_from_2021-09-15_22-33-28.png)

                                                             This is the final result

**Task 3: Blinking LED**

1. Upload the blink example code from examples tab
2. Run these commands

    ```arduino
    roscore
    ```

    ```arduino
    rosrun rosserial_python serial_node.py <Enter_your_port
    _name>
    ```

This port name can be found in the Arduino IDE, Tools→port. 

Run this command which will toggle the state of the led

```arduino
rostopic pub toggle_led std_msgs/Empty --once
```

On running it once LED will turn on

![led_on] (https://github.com/malladi2610/100_days_of_ROS/blob/7e2ae831be7bfb31daaac54591a41a2fcab3c107/Day%202/images/led_on.jpeg)

And to turn it off run the same command again

![WhatsApp Image 2021-09-18 at 21.33.46.jpeg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/06b5dd7a-a01c-4d29-960b-fb6dc3093cc8/WhatsApp_Image_2021-09-18_at_21.33.46.jpeg)

This is how the terminal window looks 

![Screenshot from 2021-09-17 23-24-03.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1160c30c-7c86-4a1a-a5be-a86a999e42b7/Screenshot_from_2021-09-17_23-24-03.png)

# Result

1. video link