# /api/operation/mode/change

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/OperationModeChange](../type/autoware_ad_api_msgs/srv/operation_mode_change.md)

## Description

Set the operation mode. For details, see the [operation mode](../features/operation-mode.md).
This API always fail if the vehicle does not support mode change by software.

## Request

| Name | Type  | Description    |
| ---- | ----- | -------------- |
| mode | uint8 | operation mode |

## Response

None
