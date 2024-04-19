#include "ros/ros.h"
#include <tf/transform_broadcaster.h>
#include <tf2_ros/static_transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <tf/transform_datatypes.h>
#include <geometry_msgs/TransformStamped.h>

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
  ros::init(argc, argv, "tf_broadcaster");
  ros::NodeHandle n;

  // Static Transform Broadcaster for base_link to laser and camera_imu_optical_frame
  static tf2_ros::StaticTransformBroadcaster static_broadcaster;
  
  // Broadcast the transform from base_link to laser
  geometry_msgs::TransformStamped base_to_laser;
  base_to_laser.header.stamp = ros::Time::now();
  base_to_laser.header.frame_id = "base_link";
  base_to_laser.child_frame_id = "laser";
  base_to_laser.transform.translation.x = 0.1; // Replace with actual value
  base_to_laser.transform.translation.y = 0.0; // Replace with actual value
  base_to_laser.transform.translation.z = 0.2; // Replace with actual value
  tf2::Quaternion laser_quat;
  laser_quat.setRPY(0, 0, 0); // Replace with actual rotation in radians
  base_to_laser.transform.rotation.x = laser_quat.x();
  base_to_laser.transform.rotation.y = laser_quat.y();
  base_to_laser.transform.rotation.z = laser_quat.z();
  base_to_laser.transform.rotation.w = laser_quat.w();
  static_broadcaster.sendTransform(base_to_laser);

  // Broadcast the transform from base_link to camera_imu_optical_frame
  geometry_msgs::TransformStamped base_to_camera_imu;
  base_to_camera_imu.header.stamp = ros::Time::now();
  base_to_camera_imu.header.frame_id = "base_link";
  base_to_camera_imu.child_frame_id = "camera_imu_optical_frame";
  base_to_camera_imu.transform.translation.x = 0.0; // Replace with actual value
  base_to_camera_imu.transform.translation.y = 0.0; // Replace with actual value
  base_to_camera_imu.transform.translation.z = 0.0; // Replace with actual value
  tf2::Quaternion camera_imu_quat;
  camera_imu_quat.setRPY(0, 0, 0); // Replace with actual rotation in radians
  base_to_camera_imu.transform.rotation.x = camera_imu_quat.x();
  base_to_camera_imu.transform.rotation.y = camera_imu_quat.y();
  base_to_camera_imu.transform.rotation.z = camera_imu_quat.z();
  base_to_camera_imu.transform.rotation.w = camera_imu_quat.w();
  static_broadcaster.sendTransform(base_to_camera_imu);

  // Dynamic Transform Broadcaster for odom to base_link
  ros::Subscriber nav_sub = n.subscribe("/odom", 1, NavCallback);

  ros::spin();

  return 0;
}
