from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'robo_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Required for ROS2 package indexing
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        # Package manifest
        ('share/' + package_name, ['package.xml']),

        # 🔴 THIS IS THE IMPORTANT PART
        # Install launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abhinav',
    maintainer_email='abhinavkenchi@github.com',
    description='Bringup launch files for robo system',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
