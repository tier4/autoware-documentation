# /api/routing/route

- Method: notification
- Type: [autoware_ad_api_msgs/msg/Route](../../../types/autoware_ad_api_msgs/msg/route.md)

## Description

Get the route with the waypoint segments in lanelet format. It is empty if route is not set.

## Message

| Name   | Type                                    | Description                    |
| ------ | --------------------------------------- | ------------------------------ |
| header | std_msgs/msg/Header                     | header for pose transformation |
| body   | autoware_ad_api_msgs/msg/RouteBody[<=1] | The route in lanelet format    |
