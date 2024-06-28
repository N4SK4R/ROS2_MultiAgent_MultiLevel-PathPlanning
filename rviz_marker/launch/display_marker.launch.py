from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path
import os

# from launch_ros.parameter_descriptions import ParameterValue
# from launch.substitutions import Command


def generate_launch_description():

    rviz_config_path = os.path.join(get_package_share_path('rviz_marker'),
                                    'rviz', 'rviz_config.rviz')
    
    marker_node = Node(
        package="rviz_marker",
        executable="display_marker"
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]
    )

    return LaunchDescription([
        marker_node,
        rviz2_node
    ])