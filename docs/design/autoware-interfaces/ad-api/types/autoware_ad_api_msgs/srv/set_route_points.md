# autoware_ad_api_msgs/srv/SetRoutePoints

## Definition

```txt
std_msgs/Header header
geometry_msgs/Pose goal
geometry_msgs/Pose[] waypoints
---
uint16 ERROR_ROUTE_EXISTS = 1
uint16 ERROR_PLANNER_UNREADY = 2
uint16 ERROR_PLANNER_FAILED = 3
autoware_ad_api_msgs/ResponseStatus status
```

## This type uses

- [autoware_ad_api_msgs/msg/ResponseStatus](../../autoware_ad_api_msgs/msg/response_status.md)
