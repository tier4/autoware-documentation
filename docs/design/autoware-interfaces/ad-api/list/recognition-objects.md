# /api/recognition/objects

- Method: Notification
- Type: [autoware_ad_api_msgs/msg/RecognitionObjectArray](../type/autoware_ad_api_msgs/msg/recognition_object_array.md)

## Description

Get the recognition objects.

## Message

| Name              | Type                                       | Description       |
| ----------------- | ------------------------------------------ | ----------------- |
| detected_objects  | autoware_ad_api_msgs/msg/DetectedObject[]  | detected objects  |
| tracked_objects   | autoware_ad_api_msgs/msg/TrackedObject[]   | tracked objects   |
| predicted_objects | autoware_ad_api_msgs/msg/PredictedObject[] | predicted objects |
| traffic_signals   | autoware_ad_api_msgs/msg/TrafficSignal[]   | traffic signals   |
