# /api/fail_safe/external/stop

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/FailSafeExternalStop](../type/autoware_ad_api_msgs/srv/fail_safe_external_stop.md)

## Description

Set or clear the external emergency stop. This API changes the [fail safe state](../features/fail-safe-state.md).

## Request

| Name | Type | Description                   |
| ---- | ---- | ----------------------------- |
| stop | bool | Stop if true, start if false. |

## Response

None
