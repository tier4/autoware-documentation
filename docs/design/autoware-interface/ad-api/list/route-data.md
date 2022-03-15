# /api/route/data

- Method: Function Call
- Type: [autoware_ad_api_msgs/msg/RouteData](../type/autoware_ad_api_msgs/msg/route_data.md)

## Description

Get the route. it is empty if no route is not set. The waypoints are empty if the route is set by other format.

## Message

| Name  | Type                                      | Description |
| ----- | ----------------------------------------- | ----------- |
| route | autoware_ad_api_msgs/msg/Route (optional) | route       |
