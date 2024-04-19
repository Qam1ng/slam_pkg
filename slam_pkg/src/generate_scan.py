#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import numpy as np

def publish_scan():
    rospy.init_node('laser_scan_publisher')
    scan_pub = rospy.Publisher('/scan', LaserScan, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        scan = LaserScan()
        scan.header.stamp = current_time
        scan.header.frame_id = 'laser_frame'
        scan.angle_min = -np.pi / 2
        scan.angle_max = np.pi / 2
        scan.angle_increment = np.pi / 180
        scan.time_increment = (1 / 40) / 360
        scan.range_min = 0.12
        scan.range_max = 10.0
        scan.ranges = np.random.uniform(low=0.12, high=10.0, size=180).tolist()
        scan.intensities = [0] * 180  # not used here

        scan_pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_scan()
    except rospy.ROSInterruptException:
        pass
