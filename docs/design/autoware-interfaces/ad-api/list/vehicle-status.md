# /api/vehicle/status

- Method: Function Call
- Type: [autoware_ad_api_msgs/msg/VehicleStatus](../types/autoware_ad_api_msgs/msg/vehicle_status.md)

## Description

Get the vehicle status.

## Message

| Name            | Type  | Description                     |
| --------------- | ----- | ------------------------------- |
| pose            | Pose  | 位置、角度 (RPY の方が良いかも) |
| velocity        | Twist | 速度、角速度                    |
| acceleration    | Twist | 加速度、角加速度                |
| gear            | Enum  | ギア                            |
| turn_indicators | Enum  | ウィンカー                      |
| hazard_lights   | Enum  | ハザード                        |
| fuel_remaining  | float | 燃料（残量）                    |
| fuel_capacity   | float | 燃料（最大）                    |
