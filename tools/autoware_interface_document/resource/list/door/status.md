---
autoware_interface:
  method: notification
  type: autoware_adapi_v1_msgs/msg/DoorStatusArray
---

# /api/door/status

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the door status. For details, see the [door operation](../../../features/door-operation.md).

## Message

| Name   | Type  | Description |
| ------ | ----- | ----------- |
| target | uint8 | door target |
| status | uint8 | door status |
