# autoware_ad_api_msgs/msg/ResponseStatus

## Definition

```txt
# constants for code
uint16 DEPRECATED = 50000
uint16 SERVICE_UNREADY = 50001
uint16 SERVICE_TIMEOUT = 50002

# variables
bool   success
uint16 code
string message
```

## This type uses

None

## This type is used by

- [autoware_ad_api_msgs/srv/DrivingEngage](../../autoware_ad_api_msgs/srv/driving_engage.md)
- [autoware_ad_api_msgs/srv/PoseResetRequest](../../autoware_ad_api_msgs/srv/pose_reset_request.md)
- [autoware_ad_api_msgs/srv/RouteClear](../../autoware_ad_api_msgs/srv/route_clear.md)
- [autoware_ad_api_msgs/srv/RouteSet](../../autoware_ad_api_msgs/srv/route_set.md)
