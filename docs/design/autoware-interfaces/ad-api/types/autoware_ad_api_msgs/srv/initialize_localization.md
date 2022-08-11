# autoware_ad_api_msgs/srv/InitializeLocalization

## Definition

```txt
geometry_msgs/PoseWithCovarianceStamped[<=1] pose
---
uint16 ERROR_UNSAFE = 1
uint16 ERROR_GNSS_SUPPORT = 2
uint16 ERROR_GNSS = 3
uint16 ERROR_ESTIMATION = 4
autoware_ad_api_msgs/ResponseStatus status
```

## This type uses

- [autoware_ad_api_msgs/msg/ResponseStatus](../../autoware_ad_api_msgs/msg/response_status.md)
