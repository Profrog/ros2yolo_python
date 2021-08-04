cmake_minimum_required(VERSION 3.5)

project(ros1_bridge)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra)
endif()

find_package(rmw REQUIRED)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rmw_implementation_cmake REQUIRED)
find_package(std_msgs REQUIRED)

# find ROS 1 packages
set(cmake_extras_files cmake/find_ros1_package.cmake cmake/find_ros1_interface_packages.cmake)
include(cmake/find_ros1_package.cmake)

find_package(PkgConfig)
if(NOT PKG_CONFIG_FOUND)
  message(WARNING "Failed to find PkgConfig, skipping...")
  # call ament_package() to avoid ament_tools treating this as a plain CMake pkg
  ament_package()
  return()
endif()

find_ros1_package(roscpp)
if(NOT ros1_roscpp_FOUND)
  message(WARNING "Failed to find ROS 1 roscpp, skipping...")
  # call ament_package() to avoid ament_tools treating this as a plain CMake pkg
  ament_package(
    CONFIG_EXTRAS ${cmake_extras_files}
  )
  return()
endif()

find_ros1_package(std_msgs REQUIRED)

# find ROS 1 packages with messages / services
include(cmake/find_ros1_interface_packages.cmake)
find_ros1_interface_packages(ros1_message_packages)


ament_export_include_directories(include)
ament_export_libraries(${PROJECT_NAME})
ament_python_install_package(${PROJECT_NAME})

ament_package(
  CONFIG_EXTRAS ${cmake_extras_files}
)

set(generated_path "${CMAKE_BINARY_DIR}/generated")
set(generated_files "${generated_path}/get_factory.cpp")
list(APPEND generated_files "${generated_path}/get_mappings.cpp")

# generate per interface compilation units to keep the memory usage low
ament_index_get_resources(ros2_interface_packages "rosidl_interfaces")
# actionlib_msgs is deprecated, but we will quiet the warning until the bridge has support for
# ROS actions: https://github.com/ros2/design/issues/195
set(actionlib_msgs_DEPRECATED_QUIET TRUE)

set(target_dependencies
  "bin/ros1_bridge_generate_factories"
  "resource/get_factory.cpp.em"
  "resource/get_mappings.cpp.em"
  "resource/interface_factories.cpp.em"
  "resource/pkg_factories.cpp.em"
  "resource/pkg_factories.hpp.em"
  "ros1_bridge/__init__.py")


include_directories(include ${generated_path})

function(custom_executable target)
  cmake_parse_arguments(
    ARG "ROS1_DEPENDENCIES" "" "TARGET_DEPENDENCIES" ${ARGN})

  add_executable(${target}
    ${ARG_UNPARSED_ARGUMENTS})
  ament_target_dependencies(${target}
    "rclcpp"
    ${ARG_TARGET_DEPENDENCIES})
  if(ARG_ROS1_DEPENDENCIES)
    ament_target_dependencies(${target}
      "ros1_roscpp"
      "ros1_std_msgs")
  endif()
  if(ARG_DEPENDENCIES)
    add_dependencies(${target} ${ARG_DEPENDENCIES})
  endif()

  install(TARGETS ${target}
  DESTINATION lib/${PROJECT_NAME})
endfunction()

custom_executable(simple_bridge_1_to_2 "src/simple_bridge_1_to_2.cpp"
  ROS1_DEPENDENCIES
  TARGET_DEPENDENCIES "std_msgs")
custom_executable(simple_bridge_2_to_1 "src/simple_bridge_2_to_1.cpp"
  ROS1_DEPENDENCIES
  TARGET_DEPENDENCIES "std_msgs")

custom_executable(simple_bridge "src/simple_bridge.cpp"
  ROS1_DEPENDENCIES
  TARGET_DEPENDENCIES "std_msgs")


install(
  PROGRAMS bin/ros1_bridge_generate_factories
  DESTINATION lib/${PROJECT_NAME}/generate_factories
)
install(
  DIRECTORY cmake
  DESTINATION share/${PROJECT_NAME}
)
install(
  DIRECTORY include/
  DESTINATION include
)

