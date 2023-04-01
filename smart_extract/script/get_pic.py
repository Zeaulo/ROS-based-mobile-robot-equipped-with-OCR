#!/usr/bin/env python3

# all_codes: jinghao
# github: zeaulo
# email: psymhmch@outlook.com
# source: AI department lab from Guangdong University of Petrochemical Technology

# Execution site: Robot

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import time

def end_sign(int_num):
    if  int_num.data == 1:
        exit()

def get_pic():
    rospy.init_node("get_pic", anonymous=False)
    publisher = rospy.Publisher('smart_eyes_topic1', Image, queue_size=2)
    # Topic2: Subscribe when main task over, and get_pic over as well.
    rospy.Subscriber('smart_eyes_topic2', String, end_sign)
    rate = rospy.Rate(2) # rate = 1 / t(s) → 0.5 senconds
    
    bridge = CvBridge()
    while not rospy.is_shutdown():
        rospy.loginfo(f"Cheese at time:{time.strftime('%Y-%m-%d %H:%M:%S')} !")
        pic = cv2.VideoCapture(0)
        _, pic = pic.read()
        pic = bridge.cv2_to_imgmsg(pic, 'bgr8')
        # Topic1: Publish that here finish the get_pic task, and you there can extract the information.
        publisher.publish(pic)
        rate.sleep()
    rospy.loginfo("Smart eyes notied that Node get_pic had exited :)")

if __name__ == '__main__':
    try:
        get_pic()
    except rospy.ROSInterruptException:
        pass