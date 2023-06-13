cd ~/catkin/carla
make launch

cd ~/catkin/carla-ros-bridge
colcon build（修改src之后）
ros2 launch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch.py
ros2 launch carla_ros_bridge carla_rviz2.launch.py（非必要）

cd ~/catkin/carla/PythonAPI/examples
python spawn_npc.py -n (car_num) -w (ped_num)

ros2 bag record /carla/ego_vehicle/fmcw_lidar

改雷达参数在~/a_ros2pkg/carla-ros-bridge/src/ros-bridge/carla_spawn_objects/config/objects.json
改之前看下同一文件夹下的readme，有一些小tips




# ROS/ROS2 bridge for CARLA simulator

[![Actions Status](https://github.com/carla-simulator/ros-bridge/workflows/CI/badge.svg)](https://github.com/carla-simulator/ros-bridge)
[![Documentation](https://readthedocs.org/projects/carla/badge/?version=latest)](http://carla.readthedocs.io)
[![GitHub](https://img.shields.io/github/license/carla-simulator/ros-bridge)](https://github.com/carla-simulator/ros-bridge/blob/master/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/carla-simulator/ros-bridge)](https://github.com/carla-simulator/ros-bridge/releases/latest)

 This ROS package is a bridge that enables two-way communication between ROS and CARLA. The information from the CARLA server is translated to ROS topics. In the same way, the messages sent between nodes in ROS get translated to commands to be applied in CARLA.

![rviz setup](./docs/images/ad_demo.png "AD Demo")

**This version requires CARLA 0.9.13**

## Features

- Provide Sensor Data (Lidar, Semantic lidar, Cameras (depth, segmentation, rgb, dvs), GNSS, Radar, IMU)
- Provide Object Data (Transforms (via [tf](http://wiki.ros.org/tf)), Traffic light status, Visualization markers, Collision, Lane invasion)
- Control AD Agents (Steer/Throttle/Brake)
- Control CARLA (Play/pause simulation, Set simulation parameters)

## Getting started and documentation

Installation instructions and further documentation of the ROS bridge and additional packages are found [__here__](https://carla.readthedocs.io/projects/ros-bridge/en/latest/).
