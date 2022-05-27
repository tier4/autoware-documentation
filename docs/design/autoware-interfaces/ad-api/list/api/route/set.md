# /api/route/set

- Method: function call
- Type: [autoware_ad_api_msgs/srv/RouteSet](../../../types/autoware_ad_api_msgs/srv/route_set.md)

## Description

Set the route with the waypoint poses. If start pose is not specified, the current pose will be used.

## Request

- header (std_msgs/msg/Header)
  - header for pose transformation
- start (geometry_msgs/Pose)
  - start pose
- goal (geometry_msgs/Pose)
  - goal pose
- waypoints (geometry_msgs/Pose[])
  - waypoint poses

## Response

- status (autoware_ad_api_msgs/msg/ResponseStatus)
  - response status
