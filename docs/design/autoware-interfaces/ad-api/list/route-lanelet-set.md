# /api/route/lanelet/set

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/LaneletRouteSet](../types/autoware_ad_api_msgs/srv/lanelet_route_set.md)

## Description

Set the route with the lanelet segments. If start pose is not specified, the current pose will be used.

## Request

| Name      | Type                                  | Description                    |
| --------- | ------------------------------------- | ------------------------------ |
| header    | std_msgs/Header                       | header for pose transformation |
| name      | string                                | route name                     |
| start     | geometry_msgs/Pose (optional)         | start pose                     |
| goal      | geometry_msgs/Pose                    | goal pose                      |
| waypoints | autoware_ad_api_msgs/LaneletSegment[] | lanelet segments               |

## Response

None
