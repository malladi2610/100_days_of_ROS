//Task 5: To Control the turtle in simulator by using a joystick module
//Goal : To understand the geometry_msgs and their manipulation to get the desired results


#include <ros.h>
#include <geometry_msgs/Twist.h>  //This is the type of message which is accepted by the turtle1/cmd_vel which is subscribed by turtlesim

//Variable Declarations
#define joyX A0     
#define joyY A1
int xpos = 0;
int ypos = 0;
int xValue = 0;
int yValue = 0;

ros::NodeHandle nh;

//Creation of "twist"publisher which can be used to publish the msgs to the required topic i.e "/turtle1/cmd_vel"
geometry_msgs::Twist twist_msgs;
ros::Publisher twist("/turtle1/cmd_vel",&twist_msgs);

void setup(){
  Serial.begin(9600);
  nh.initNode();
  nh.advertise(twist);
}

void loop() {
 //Getting the raw data from the joystick
  int xValue = analogRead(joyX);
  int yValue = analogRead(joyY);
 //Mapping the raw data to the desired range for simplicity
  int mapX = map(xValue,0,1023, -512,512);
  int mapY = map(yValue,0,1023, -512,512);

//Commands which control the movement of the robot

//Right direction
  if(mapX == -512 && mapX >= -512){
     xpos = xpos + 1;
     twist_msgs.linear.x = xpos;
     twist_msgs.linear.y = 0; 
  }

//Left direction
  if(mapX == 512 && mapX <= 512){
     xpos = xpos - 1;
     twist_msgs.linear.x = xpos;
     twist_msgs.linear.y = 0; 
  }

//Upward direction 
  if(mapY == -512 && mapY >= -512){
     ypos = ypos + 1;
     twist_msgs.linear.x = 0;
     twist_msgs.linear.y = ypos;

  }

//Downward direction  
  if(mapY == 512 && mapY <= 512){
     ypos = ypos - 1;
     twist_msgs.linear.x = 0;
     twist_msgs.linear.y = ypos; 
  }
  twist.publish(&twist_msgs);
  nh.spinOnce();
  
  delay(500);

  //To prevent the continous addition of the velocity
  xpos = 0;
  ypos = 0;
  twist_msgs.linear.x = xpos;
  twist_msgs.linear.y = ypos;
  twist.publish(&twist_msgs);
  nh.spinOnce();
}
