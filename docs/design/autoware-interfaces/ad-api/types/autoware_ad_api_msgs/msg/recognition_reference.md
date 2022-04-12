# autoware_ad_api_msgs/msg/RecognitionReference

## Definition

```txt
uint32 RECOGNITION_AREA = 1
uint32 DETECTED_OBJECT = 2
uint32 TRACKED_OBJECT = 3
uint32 PREDICTED_OBJECT = 4
uint32 TRAFFIC_SIGNAL = 5

builtin_interfaces/Time stamp
uint32 type
string index
```

## The types that use this

- [autoware_ad_api_msgs/msg/MovementFactor](../../autoware_ad_api_msgs/msg/movement_factor.md)
- [autoware_ad_api_msgs/msg/RecognitionArea](../../autoware_ad_api_msgs/msg/recognition_area.md)
