cmake_minimum_required(VERSION 3.8)
project(robo_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY
    meshes
    urdf
    rviz
    launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

