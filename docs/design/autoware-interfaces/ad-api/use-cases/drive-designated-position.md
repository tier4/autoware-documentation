# Drive to the designated position

## Related features

- [Route](../features/route-state.md)
- [Driving](../features/driving-state.md)

## Scenario

1. Check if the route can be set.
   - /api/v0/route/state
1. Set the route.
   - /api/v0/route/set
1. Check if the route can be set.
   - /api/v0/route/state
1. Check if the vehicle can depart
   - /api/v0/driving/state
1. Depart the vehicle
   - /api/v0/driving/engage
1. Check if the vehicle has departed
   - /api/v0/driving/state
1. Check if the vehicle has arrived at the destination
   - /api/v0/route/state
1. Clear the route.
   - /api/v0/route/clear
