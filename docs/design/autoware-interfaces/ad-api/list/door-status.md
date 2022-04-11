# /api/door/status

- Method: Notification
- Type: [autoware_ad_api_msgs/msg/DoorStatusArray](../type/autoware_ad_api_msgs/msg/door_status_array.md)

## Description

Get the door status. For details, see the [door operation](../features/door-operation.md).

## Message

| Name   | Type  | Description |
| ------ | ----- | ----------- |
| target | uint8 | door target |
| status | uint8 | door status |
