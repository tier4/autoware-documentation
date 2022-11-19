---
autoware_interface:
  method: function call
  type: autoware_adapi_v1_msgs/msg/VehicleStatus
---

# /api/vehicle/status

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

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
