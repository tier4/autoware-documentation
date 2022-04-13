---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/RecognitionObjectArray
---

# /api/recognition/objects

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the recognition objects.

## Message

| Name              | Type                                       | Description       |
| ----------------- | ------------------------------------------ | ----------------- |
| detected_objects  | autoware_ad_api_msgs/msg/DetectedObject[]  | detected objects  |
| tracked_objects   | autoware_ad_api_msgs/msg/TrackedObject[]   | tracked objects   |
| predicted_objects | autoware_ad_api_msgs/msg/PredictedObject[] | predicted objects |
| traffic_signals   | autoware_ad_api_msgs/msg/TrafficSignal[]   | traffic signals   |
