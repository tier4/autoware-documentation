---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/DrivingState
---

# /api/driving/state

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the driving state. For details, see the [driving state](../../../features/driving-state.md).

## Message

| Name  | Type   | Description   |
| ----- | ------ | ------------- |
| state | uint32 | driving state |
