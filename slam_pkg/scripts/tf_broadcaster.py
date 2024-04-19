#!/usr/bin/env python
import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped

def broadcast_transforms():
    rospy.init_node('tf2_broadcaster')

    # specify rostopic publisher
    pub = rospy.Publisher('tf', TransformStamped, queue_size=10)

    # Create a broadcaster
    br = tf2_ros.StaticTransformBroadcaster()

    # List to store all transformations
    transforms = []

    # Transform from odom to base_link (dynamic and usually handled by odometry node but can be static for demonstration)
    odom_to_base_link = TransformStamped()
    odom_to_base_link.header.stamp = rospy.Time.now()
    odom_to_base_link.header.frame_id = "odom"
    odom_to_base_link.child_frame_id = "base_link"
    odom_to_base_link.transform.translation.x = 0.0
    odom_to_base_link.transform.translation.y = 0.0
    odom_to_base_link.transform.translation.z = 0.0
    odom_to_base_link.transform.rotation.x = 0.0
    odom_to_base_link.transform.rotation.y = 0.0
    odom_to_base_link.transform.rotation.z = 0.0
    odom_to_base_link.transform.rotation.w = 1.0
    transforms.append(odom_to_base_link)

    # Transform from base_link to base_footprint
    base_link_to_base_footprint = TransformStamped()
    base_link_to_base_footprint.header.stamp = rospy.Time.now()
    base_link_to_base_footprint.header.frame_id = "base_link"
    base_link_to_base_footprint.child_frame_id = "base_footprint"
    base_link_to_base_footprint.transform.translation.x = 0.0
    base_link_to_base_footprint.transform.translation.y = 0.0
    base_link_to_base_footprint.transform.translation.z = 0.0
    base_link_to_base_footprint.transform.rotation.x = 0.0
    base_link_to_base_footprint.transform.rotation.y = 0.0
    base_link_to_base_footprint.transform.rotation.z = 0.0
    base_link_to_base_footprint.transform.rotation.w = 1.0
    transforms.append(base_link_to_base_footprint)

    # Broadcast all transforms at once
    br.sendTransform(transforms)

    # Keep the node alive
    rospy.spin()

if __name__ == '__main__':
    broadcast_transforms()
