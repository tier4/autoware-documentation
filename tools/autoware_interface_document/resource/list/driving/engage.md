---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/DrivingEngage
---

# /api/driving/engage

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Engage or disengage the vehicle. This API changes the [driving state](../../../features/driving.md).

## Request

| Name   | Type | Description                         |
| ------ | ---- | ----------------------------------- |
| engage | bool | Engage if true, disengage if false. |

## Response

None
