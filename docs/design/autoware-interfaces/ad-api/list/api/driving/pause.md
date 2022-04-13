---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/DrivingPause
---

# /api/driving/pause

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Pause or unpause the vehicle. This API changes the [driving state](../../../features/driving-state.md).

## Request

| Name  | Type | Description                      |
| ----- | ---- | -------------------------------- |
| pause | bool | Pause if true, unpause if false. |

## Response

None
