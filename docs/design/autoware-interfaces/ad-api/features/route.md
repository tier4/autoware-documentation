# Route API

- [/api/route/state](../list/api/route/state.md)
- [/api/route/clear](../list/api/route/clear.md)
- [/api/route/set](../list/api/route/set.md)
- [/api/route/lanelet/set](../list/api/route/lanelet/set.md)
- [/api/route/lanelet/notice](../list/api/route/lanelet/notice.md)

## Description

This API manages destination and waypoints. Note that waypoints are not like stops and just points passing through.
In other words, Autoware does not support the route with multiple stops, the application needs to split it up and switch them.
There are two ways to set the route. The one is a generic method that uses pose, another is a map-dependent.

## States

![route-state](./route-state.drawio.svg)

| State    | Description                                        |
| -------- | -------------------------------------------------- |
| WAITING  | The route is not set. Waiting for a route request. |
| SET      | The route is set.                                  |
| ARRIVED  | The vehicle has arrived at the destination.        |
| CHANGING | Trying to change the route. Not implemented yet.   |
