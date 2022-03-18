cmake_minimum_required(VERSION 3.5)
project(autoware_ad_api_msgs)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
  set(CMAKE_CXX_EXTENSIONS OFF)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

rosidl_generate_interfaces(${PROJECT_NAME}
  common/srv/GetInterfaceVersion.srv
  common/msg/ResponseStatus.msg
  common/msg/ResponseStatusCode.msg
  common/msg/ResponseStatusDetail.msg
  launcher/msg/AutowareLauncherState.msg
  launcher/srv/AutowareLauncherCommand.srv
  launcher/srv/GetAutowareVersion.srv
  launcher/srv/SetAutowareVersion.srv
  launcher/srv/FetchAutowareVersion.srv
  route/msg/RouteState.msg
  route/srv/RouteClear.srv
  route/srv/RouteSet.srv
  route/msg/Route.msg
  route/msg/RouteData.msg
  route/srv/LaneletRouteSet.srv
  route/msg/LaneletRoute.msg
  route/msg/LaneletRouteData.msg
  route/msg/LaneletSegment.msg
  route/msg/LaneletPrimitive.msg
  others/msg/OperationMode.msg
  others/srv/OperationModeChange.srv
  others/msg/FailSafeState.msg
  others/msg/DrivingState.msg
  others/srv/DrivingEngage.srv
  others/msg/VehicleStatus.msg
  others/msg/DoorStatusArray.msg
  others/msg/DoorStatus.msg
  others/msg/DoorCommand.msg
  others/srv/DoorOperate.srv
  DEPENDENCIES
    builtin_interfaces
    std_msgs
    geometry_msgs
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package()
