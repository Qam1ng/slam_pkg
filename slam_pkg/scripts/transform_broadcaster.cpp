#include "ros/ros.h"
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <tf/transform_datatypes.h>

void NavCallback(const nav_msgs::Odometry &msg) {
  static tf::TransformBroadcaster br;
  tf::Transform transform;
  transform.setOrigin(tf::Vector3(msg.pose.pose.position.x, msg.pose.pose.position.y, 0.0));
  tf::Quaternion q;
  tf::quaternionMsgToTF(msg.pose.pose.orientation, q);
  transform.setRotation(q);
  br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "odom", "base_link"));
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "odom_to_base_link");
  ros::NodeHandle n;
  ros::Subscriber nav_sub = n.subscribe("/odometry/filtered", 1, NavCallback);
 ros::spin();
  
  return 0;
};