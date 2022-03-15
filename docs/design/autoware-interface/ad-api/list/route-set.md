# /api/route/set

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/RouteSet](../type/autoware_ad_api_msgs/srv/route_set.md)

## Description

Set the route with the waypoint poses. If start pose is not specified, the current pose will be used.

## Request

| Name      | Type                              | Description                    |
| --------- | --------------------------------- | ------------------------------ |
| header    | std_msgs/msg/Header               | header for pose transformation |
| name      | string                            | route name                     |
| start     | geometry_msgs/msg/Pose (optional) | start pose                     |
| goal      | geometry_msgs/msg/Pose            | goal pose                      |
| waypoints | geometry_msgs/msg/Pose[]          | waypoint poses                 |

## Response

None
