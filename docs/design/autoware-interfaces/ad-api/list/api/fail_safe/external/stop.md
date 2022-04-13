---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/FailSafeExternalStop
---

# /api/fail_safe/external/stop

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Set or clear the external emergency stop. This API changes the [fail safe state](../../../../features/fail-safe-state.md).

## Request

| Name | Type | Description                   |
| ---- | ---- | ----------------------------- |
| stop | bool | Stop if true, start if false. |

## Response

None
