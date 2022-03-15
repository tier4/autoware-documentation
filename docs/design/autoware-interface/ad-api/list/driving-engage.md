# /api/driving/engage

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/DrivingEngage](../type/autoware_ad_api_msgs/srv/driving_engage.md)

## Description

Engage or disengage the vehicle. This API changes the [driving state](../data/driving-state.md).

## Request

| Name   | Type | Description                         |
| ------ | ---- | ----------------------------------- |
| engage | bool | Engage if true, disengage if false. |

## Response

None
