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

## Restriction

This API can only be used when the route state is UNSET, otherwise an error will be returned.

## Request

| Name      | Type                          | Description                    |
| --------- | ----------------------------- | ------------------------------ |
| header    | std_msgs/Header               | header for pose transformation |
| start     | geometry_msgs/Pose (optional) | start pose                     |
| goal      | geometry_msgs/Pose            | goal pose                      |
| waypoints | geometry_msgs/Pose[]          | waypoint poses                 |

## Response

### response.status

| Name | Description |
| ---- | ----------- |
| 1001 | Test        |
