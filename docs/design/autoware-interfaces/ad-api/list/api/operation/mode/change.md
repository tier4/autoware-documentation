---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/OperationModeChange
---

# /api/operation/mode/change

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Set the operation mode. For details, see the [operation mode](../../../../features/operation-mode.md).
This API always fail if the vehicle does not support mode change by software.

## Request

| Name | Type  | Description    |
| ---- | ----- | -------------- |
| mode | uint8 | operation mode |

## Response

None
