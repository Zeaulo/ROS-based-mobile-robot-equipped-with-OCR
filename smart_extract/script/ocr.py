#!/usr/bin/env python3

# all_codes: jinghao
# github: zeaulo
# email: psymhmch@outlook.com
# source: AI department lab from Guangdong University of Petrochemical Technology

# Execution site: PC

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import time
import sys
import os

rosrun_root_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(rosrun_root_path)
from cn_ocr import CnOcr

class config(object):
    def __init__(self):
        # 图片识别存储路径 (默认) - Recognized picture files path (default)
        self.pic_path = rosrun_root_path + f"/../saved_data/{time.strftime('%Y-%m-%d_%H:%M:%S')}.jpg"

        # 检测结果存储路径（默认） - Result file's path (default)
        self.log_path = rosrun_root_path + '/../record.log'
        
        # 所需检测的全部字 - Needed recongized characters
        self.characters = '0123456789.'

def detect(img, chars):
    # 图片预处理 - Picture Preprocessing
    img = cv2.GaussianBlur(img, (3,3), 1,2)

    # 第一次运行需要下载模型文件 - Downloading Model Files
    model = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3', cand_alphabet=chars)
    detecting = model.ocr(img)
    whether_re = [i for i in detecting]
    content = ''
    if whether_re :
        # 检测数据存储 - DATA Saved
        cv2.imwrite(config().pic_path, img)
        for item in detecting:
            content += item['text'] + ' '
        content =  f"时间:\t{time.strftime('%Y-%m-%d %H:%M:%S')}\n检测到的结果:\t{content.strip()}\n\n"

    return content

def callback(img):
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(img, 'bgr8')

    add_content = detect(img, config().characters)

    # 日志记录 - Log Recording
    record = open(config().log_path, 'r', encoding='utf8').read()
    
    # 打印结果 - Result Printing
    if add_content:
        print(add_content)
    
    # 日志重写 - Log Rewriting
    rewrite = open(config().log_path, 'w', encoding='utf8')
    rewrite.write(record + add_content)
    rewrite.close()

def ocr():
    rospy.init_node('ocr', anonymous=False)
    rospy.Subscriber('smart_eyes_topic1', Image, callback)
    rospy.spin()
    
if __name__ == '__main__':
    try:
        ocr()
    except rospy.ROSInterruptException:
        pass
