---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/MovementState
---

# /api/movement/state

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the movement state. For details, see the [movement state](../../../features/movement-state.md).

## Message

| Name  | Type   | Description                                                   |
| ----- | ------ | ------------------------------------------------------------- |
| state | uint32 | movement state                                                |
| state | uint32 | distance to stop position during deceleration, otherwise zero |
