

# Function
- get pcd from RGB(jpg) and Depth(png) file
- convert pcd to ros PointCloud2 format to pub
- using rviz to visualization

# usage
- put pcd4ros into ros_workspace/src as package
- catkin_make package
```shell
roslaunch pcd4ros demo.launch
```
- using rviz to observe
```shell
rviz
```
- rviz config under ./resource/demo.rviz


# image
<p align="center">
  <img src="https://gitee.com/trihook/pcd4ros/raw/master/scripts/resource/screenshot.png" align="middle" width = "800" />
</p>
