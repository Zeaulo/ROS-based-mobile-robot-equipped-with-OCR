## Brief Introduction - some ros1 packages (uploading)
默认语言：英语<br/>切换语言：[中文](https://github.com/Zeaulo/jinghao_ros/blob/main/README_cn.md)<br/><br/>
**smart_extract** ：<br/>
    This package is applied to mobile visual robot.After startup, the camera can be called to capture specific text that appears in the screen (only supported in Chinese and English), with very high accuracy. The code file has provided interface settings for parameters, and the degree of freedom for secondary development is very high. Please ensure that the following Python dependency packages are installed before running:<br/>->`pip3 install cnstd`<br/>->`pip3 install torch torchvision`
<br/>
**vision_opencv** ：<br/>
    To address the lack of cv_bridge in Python 3, please refer to:https://github.com/ros-perception/vision_opencv.git
Clone the source code to any workspace and use Catkin build to compile. If the workspace has already been compiled, you need to first remove the build and devel:)<br/>->`catkin build`

|Tested environment:|
|------------------|
|Ubuntu 20.04|
|Ros1 Noetic|
|Python 3.8.10|
|torch 2.0 && cuda 11.7|
|cnstd 1.2.2|

Some personal developed ROS packages are for learning and open source purposes only, and should not be used for commercial purposes.

