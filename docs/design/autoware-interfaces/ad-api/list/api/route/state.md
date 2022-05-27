# /api/route/state

- Type: notification
- Data: autoware_ad_api_msgs/msg/RouteNotice

## Description

Get the route with waypoint poses. It is empty if route is not set.
The waypoints are empty if the route is set by other format.

## Message

- state (uint16)
  - route state
