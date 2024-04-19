#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist, Vector3
import tf

rospy.init_node('odometry_publisher')

odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)

rate = rospy.Rate(20)  # 20 Hz
while not rospy.is_shutdown():
    # Example data - replace these with your actual sensor readings
    x = 0.0
    y = 0.0
    theta = 0.0  # Orientation in radians
    vx = 0.1  # Linear velocity x
    vy = 0.0  # Linear velocity y
    vth = 0.1  # Angular velocity z

    # Current time
    current_time = rospy.Time.now()

    # Create and fill the odometry message
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # Set the position
    odom.pose.pose.position = Point(x, y, 0)
    odom.pose.pose.orientation = tf.transformations.quaternion_from_euler(0, 0, theta)

    # Set the velocity
    odom.twist.twist.linear = Vector3(vx, vy, 0)
    odom.twist.twist.angular = Vector3(0, 0, vth)

    # Publish the message
    odom_pub.publish(odom)

    rate.sleep()