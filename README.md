## Brief Introduction:some ros1 packages
----------------------
|Tested environment:|
----------------------
|Ubuntu 20.04|
|Ros1 Noetic|
|Python 3.8.10|
|torch 2.0 && cuda 11.7|
|cnstd 1.2.2|
----------------------
**smart_extract** 介绍：
  应用于移动机器人，启动后可以调用摄像头抓取画面内出现的特定文字（仅支持中英文），准确度非常高。该ROS功能已为参数提供接口设置，二次开发的自由度很高。请在运行前，确保以下的python依赖包已安装：

->`pip3 install cnstd`<br/>->`pip3 install torch torchvision`


**vision_opencv** 介绍：
  为解决python3中没有cv_bridge而加载，详细参见：https://github.com/ros-perception/vision_opencv.git

将源码克隆到任意一个工作空间后使用catkin build编译，若工作空间已编译，则需要先删除build和devel:)<br/>->`catkin build`

一些个人开发的ROS包，仅供学习开源，请勿用于商业用途。
