# Drive to the designated position

## Related features

- [Route](../features/route-state.md)
- [Driving](../features/driving-state.md)

## Scenario

1. Check if the route can be set.
   - route/state == UNSET
1. Set the route.
   - /api/v0/route/set
1. Check if the route has been set.
   - route/state=set
1. Check if the vehicle can depart
   - driving/state=ready
1. Depart the vehicle
   - driving/engage
1. Check if the vehicle has departed
   - driving/state=driving
1. Check if the vehicle has arrived at the destination
   - route/state=arrived
