#!/usr/bin/env python

import rospy
import tf
from nav_msgs.msg import Odometry

def nav_callback(msg):
    broadcaster = tf.TransformBroadcaster()
    # Extracting position and orientation from the message
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = 0.0  # Setting z to 0 as it's 2D
    orientation = msg.pose.pose.orientation
    
    # Broadcasting the transform
    broadcaster.sendTransform((x, y, z),
                              (orientation.x, orientation.y, orientation.z, orientation.w),
                              rospy.Time.now(),
                              "base_link",
                              "odom")

def main():
    rospy.init_node('odom_to_base_link')
    # Subscribing to the odometry topic
    rospy.Subscriber("/odometry/filtered", Odometry, nav_callback)
    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    main()
