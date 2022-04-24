#include <NewPing.h> //Used with ultrasonic sensor to calculate the distance
#include <ros.h>     //ROS library
#include <ros/time.h>
#include <sensor_msgs/Range.h> //Used to advertise the output of a single ultrasonic sensor

//Ultrasonic sensor declaration
const int TriggerPin = 11; 
const int EchoPin = 12;
 

NewPing sonar(TriggerPin, EchoPin, 100);
  
 
ros::NodeHandle nh; //create an object which represents the ROS node.
 

 
void sensor_msg_init(sensor_msgs::Range &range_name, char *frame_id_name)
{
  range_name.radiation_type = sensor_msgs::Range::ULTRASOUND;
  range_name.header.frame_id = frame_id_name;
  range_name.field_of_view = 0.26;
  range_name.min_range = 0.0;
  range_name.max_range = 2.0;
}
 
//Create three instances for range messages.

sensor_msgs::Range range_msg;

 
//Create publisher onjects for all sensors

ros::Publisher pub_range("/ultrasound_sensor", &range_msg);

 
void setup() {
  Serial.begin(9600);
 
  nh.initNode();

  nh.advertise(pub_range);

  sensor_msg_init(range_msg, "/ultrasound_sensor"); 
}
 
void loop() {
 int cm = sonar.ping_cm(); 
 Serial.println(cm); 
 delay(250); 
  range_msg.range = cm;

  range_msg.header.stamp = nh.now();
  
  pub_range.publish(&range_msg);

  nh.spinOnce();//Handle ROS events
  delay(250);
}
