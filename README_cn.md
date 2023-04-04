## 简介 - 一些ROS1的功能包(持续开发)

**smart_extract** 功能包介绍：<br/>
&emsp;应用于移动视觉机器人，启动后可以调用摄像头抓取画面内出现的特定文字（仅支持中英文），准确度非常高。该ROS功能已为参数提供接口设置，二次开发的自由度很高。请在运行前确保以下的python依赖包已被安装：<br/>
->`pip3 install cnstd`<br/>->`pip3 install torch torchvision`


**vision_opencv** 功能包介绍：<br/>
&emsp;为解决python3中没有cv_bridge而加载，详细参见：https://github.com/ros-perception/vision_opencv.git
&emsp;将源码克隆到任意一个工作空间后使用catkin build编译，若工作空间已编译，则需要先删除build和devel:)<br/>->`catkin build`

|我的环境:|
|------------------|
|Ubuntu 20.04|
|Ros1 Noetic|
|Python 3.8.10|
|torch 2.0 && cuda 11.7|
|cnstd 1.2.2|

一些个人开发的ROS包，仅供学习开源，请勿用于商业用途。
