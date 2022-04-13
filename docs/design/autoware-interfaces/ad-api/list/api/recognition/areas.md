---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/RecognitionAreaArray
---

# /api/recognition/areas

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the recognition areas.

## Message

| Name  | Type                                       | Description       |
| ----- | ------------------------------------------ | ----------------- |
| areas | autoware_ad_api_msgs/msg/RecognitionArea[] | recognition areas |
