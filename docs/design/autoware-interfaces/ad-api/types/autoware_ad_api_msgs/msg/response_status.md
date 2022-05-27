# autoware_ad_api_msgs/msg/ResponseStatus

## Definition

```txt
# constants for level
uint16 UNKNOWN=0
uint16 SUCCESS=1
uint16 WARNING=2
uint16 ERROR=3

# constants for code
uint16 INTERNAL_SERVICE_UNREADY=101
uint16 INTERNAL_SERVICE_TIMEOUT=102

# variables
uint16 level
uint16 code
string message
```

## The types that use this

- [autoware_ad_api_msgs/srv/DrivingEngage](../../autoware_ad_api_msgs/srv/driving_engage.md)
- [autoware_ad_api_msgs/srv/RouteClear](../../autoware_ad_api_msgs/srv/route_clear.md)
- [autoware_ad_api_msgs/srv/RouteSet](../../autoware_ad_api_msgs/srv/route_set.md)
