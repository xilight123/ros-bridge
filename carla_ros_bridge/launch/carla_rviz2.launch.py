import os

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            remappings=[
                (
                    "carla/ego_vehicle/spectator_pose",
                    "/carla/ego_vehicle/rgb_view/control/set_transform"
                )
            ],
            arguments=[
                '-d', os.path.join(get_package_share_directory('carla_ros_bridge'), 'config/carla_rviz_ros2.rviz')],
            on_exit=launch.actions.Shutdown()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
