# /api/driving/pause

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/DrivingPause](../types/autoware_ad_api_msgs/srv/driving_pause.md)

## Description

Pause or unpause the vehicle. This API changes the [driving state](../features/driving-state.md).

## Request

| Name  | Type | Description                      |
| ----- | ---- | -------------------------------- |
| pause | bool | Pause if true, unpause if false. |

## Response

None
