---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/MovementFactorArray
---

# /api/movement/factors

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the movement factors.

## Message

| Name    | Type                                      | Description      |
| ------- | ----------------------------------------- | ---------------- |
| factors | autoware_ad_api_msgs/msg/MovementFactor[] | movement factors |
