# autoware_ad_api_msgs/msg/LaneletRoute

## Definition

```txt
std_msgs/Header header
string name
geometry_msgs/Pose[<=1] start
geometry_msgs/Pose goal
autoware_ad_api_msgs/LaneletSegment[] segments
```

## The types that this uses

- [autoware_ad_api_msgs/msg/LaneletSegment](../../autoware_ad_api_msgs/msg/lanelet_segment.md)

## The types that use this

- [autoware_ad_api_msgs/msg/LaneletRouteData](../../autoware_ad_api_msgs/msg/lanelet_route_data.md)
- [autoware_ad_api_msgs/srv/LaneletRouteSet](../../autoware_ad_api_msgs/srv/lanelet_route_set.md)
