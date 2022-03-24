# autoware_ad_api_msgs/msg/FailSafeState

## Definition

```txt
uint32 UNKNOWN = 0
uint32 NORMAL = 1
uint32 TAKEOVER_REQUEST = 2
uint32 MRM_OPERATING = 3
uint32 MRM_SUCCEEDED = 4
uint32 MRM_FAILED = 5

uint32 state
bool auto_recovery
bool external_stop
```
