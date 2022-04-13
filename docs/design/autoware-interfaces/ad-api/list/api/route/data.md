# /api/route/data

- Method: Notification
- Type: [autoware_ad_api_msgs/msg/RouteData](../types/autoware_ad_api_msgs/msg/route_data.md)

## Description

Get the route with waypoint poses. It is empty if route is not set.
The waypoints are empty if the route is set by other format.

## Message

| Name  | Type                                  | Description |
| ----- | ------------------------------------- | ----------- |
| route | autoware_ad_api_msgs/Route (optional) | route       |
