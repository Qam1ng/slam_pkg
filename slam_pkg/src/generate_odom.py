#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Quaternion, Twist

def publish_odometry():
    rospy.init_node('odometry_publisher')
    odom_pub = rospy.Publisher('/odom', Odometry, queue_size=50)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        odom = Odometry()
        odom.header.stamp = rospy.Time.now()
        odom.header.frame_id = 'odom'
        odom.child_frame_id = 'base_link'

        # Simulate movement: (x, y, theta)
        odom.pose.pose = Pose(position=Point(x=1.0, y=0.5, z=0.0),
                              orientation=Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0.1)))
        odom.twist.twist = Twist(linear=Vector3(0.1, 0, 0),
                                 angular=Vector3(0, 0, 0.1))

        odom_pub.publish(odom)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_odometry()
    except rospy.ROSInterruptException:
        pass
