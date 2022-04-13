---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/RouteData
---

# /api/route/data

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the route with waypoint poses. It is empty if route is not set.
The waypoints are empty if the route is set by other format.

## Message

| Name  | Type                                  | Description |
| ----- | ------------------------------------- | ----------- |
| route | autoware_ad_api_msgs/Route (optional) | route       |
