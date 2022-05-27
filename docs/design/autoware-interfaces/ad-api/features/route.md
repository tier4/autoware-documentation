# Route API

## Description

The route feature manages destination and waypoints. Note that waypoints are not like stops and just points passing through.
In other words, Autoware does not support the route with multiple stops, the application needs to split it up and switch them.
There are two ways to set the route. The one is a generic method that uses pose, another is a map-dependent.

## Route State

![route-state](./route-state.drawio.svg)

| State    | Description                                        |
| -------- | -------------------------------------------------- |
| WAITING  | The route is not set. Waiting for a route request. |
| SET      | The route is set.                                  |
| CHANGING | Trying to change the route.                        |
| ARRIVED  | The vehicle has arrived at the destination.        |

## Related API

- /api/route/state
- /api/route/clear
- /api/route/set
- /api/route/lanelet/set
