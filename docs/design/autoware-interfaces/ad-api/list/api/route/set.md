---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/RouteSet
---

# /api/route/set

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Set the route with the waypoint poses. If start pose is not specified, the current pose will be used.

## Request

| Name      | Type                          | Description                    |
| --------- | ----------------------------- | ------------------------------ |
| header    | std_msgs/Header               | header for pose transformation |
| name      | string                        | route name                     |
| start     | geometry_msgs/Pose (optional) | start pose                     |
| goal      | geometry_msgs/Pose            | goal pose                      |
| waypoints | geometry_msgs/Pose[]          | waypoint poses                 |

## Response

None
