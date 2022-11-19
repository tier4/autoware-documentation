---
autoware_interface:
  method: function call
  type: autoware_adapi_v1_msgs/srv/DoorOperate
---

# /api/door/operate

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Operate the door. For details, see the [door operation](../../../features/door-operation.md).

## Request

| Name    | Type  | Description  |
| ------- | ----- | ------------ |
| target  | uint8 | door target  |
| command | uint8 | door command |

## Response

None
