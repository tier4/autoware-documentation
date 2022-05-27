---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/RouteState
---

# /api/route/state

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the route state. For details, see the [route state](../../../features/route-state.md).

## Message

| Name  | Type          | Description |
| ----- | ------------- | ----------- |
| state | enum (uint32) | route state |
