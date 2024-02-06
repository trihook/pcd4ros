#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import rospy
from sensor_msgs.msg import PointCloud2
from read_pcd import imgs2pcd
from pcd_pc2_cvt import *
import os

PJ_ABS_PATH = os.path.split(os.path.realpath(__file__))[0]


def main():
    pub = rospy.Publisher('pc2_topic', PointCloud2, queue_size=5)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)

    rgb = os.path.join(PJ_ABS_PATH, "resource", "0001.jpg")
    depth = os.path.join(PJ_ABS_PATH, "resource", "0001.png")
    f = (1124, 1134)
    c = (755, 555)
    pcd = imgs2pcd(rgb, depth, f, c)

    points = convert_cloud_from_o3d_to_ros(pcd, "cam1")

    while not rospy.is_shutdown():
        pub.publish(points)
        print("published...")
        rate.sleep()


if __name__ == '__main__':
    main()
