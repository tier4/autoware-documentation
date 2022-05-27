---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/OperationMode
---

# /api/operation/mode/notice

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the operation mode. For details, see the [operation mode](../../../../features/operation-mode.md).

## Message

| Name | Type  | Description    |
| ---- | ----- | -------------- |
| mode | uint8 | operation mode |
