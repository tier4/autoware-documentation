# /api/movement/state

- Method: Notification
- Type: [autoware_ad_api_msgs/msg/MovementState](../type/autoware_ad_api_msgs/msg/movement_state.md)

## Description

Get the movement state. For details, see the [movement state](../features/movement-state.md).

## Message

| Name  | Type   | Description                                                   |
| ----- | ------ | ------------------------------------------------------------- |
| state | uint32 | movement state                                                |
| state | uint32 | distance to stop position during deceleration, otherwise zero |
