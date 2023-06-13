# 如果要修改rotation_frequency，则需要在发布雷达的launch文件里更改fixed_delta_seconds的值，使二者相乘等于1
# 比如此处在objects.json中 rotation_frequency = 10Hz，则对应的carla_ros_bridge_with_example_ego_vehicle.launch.py文件里的fixed_delta_seconds = 0.1s

# left_fov和right_fov代表了固态激光雷达的左右视角，正前方为0。
