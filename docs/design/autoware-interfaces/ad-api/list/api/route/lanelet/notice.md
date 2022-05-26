---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/LaneletRouteData
---

# /api/route/lanelet/data

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the route with lanelet segments. It is empty if route is not set.

## Message

| Name  | Type                                         | Description |
| ----- | -------------------------------------------- | ----------- |
| route | autoware_ad_api_msgs/LaneletRoute (optional) | route       |
