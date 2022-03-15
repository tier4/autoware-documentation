# autoware_ad_api_msgs/msg/Route

## Definition

```txt
std_msgs/Header header
string name
geometry_msgs/Pose[<=1] start
geometry_msgs/Pose goal
geometry_msgs/Pose[] waypoints
```

## The types that use this

- [autoware_ad_api_msgs/msg/RouteData](../../autoware_ad_api_msgs/msg/route_data.md)
- [autoware_ad_api_msgs/srv/RouteSet](../../autoware_ad_api_msgs/srv/route_set.md)
