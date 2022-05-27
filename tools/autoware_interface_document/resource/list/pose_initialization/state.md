---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/PoseInitializationState
---

# /api/pose_initialization/state

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the pose initialization state. For details, see the [pose initialization state](../../../features/pose-initialization-state.md).

## Message

| Name  | Type   | Description               |
| ----- | ------ | ------------------------- |
| state | uint32 | pose initialization state |
