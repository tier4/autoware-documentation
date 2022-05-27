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

## This type uses

None

## This type is used by

- autoware_ad_api_msgs/srv/DrivingEngage
- autoware_ad_api_msgs/srv/RouteClear
- autoware_ad_api_msgs/srv/RouteSet
