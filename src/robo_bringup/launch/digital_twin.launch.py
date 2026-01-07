#!/usr/bin/env python3
"""
Digital Twin Launch File
- Loads URDF
- Publishes TF
- Starts RViz
"""

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    # Path to URDF
    urdf_file = os.path.join(
        get_package_share_directory('robo_description'),
        'urdf',
        'robo.urdf.xacro'
    )

    robot_description = Command(['xacro ', urdf_file])

    return LaunchDescription([

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description
            }]
        ),

        # Static TF: world -> base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='world_to_base_link',
            arguments=['0', '0', '0', '0', '0', '0', 'world', 'base_link']
        ),
	        # Joint State Publisher (temporary)
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),

        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),
    ])
