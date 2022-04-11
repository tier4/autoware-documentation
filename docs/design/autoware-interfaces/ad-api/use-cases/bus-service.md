# Use Case of Bus Service

## Overview

This use case is a bus operation service that goes around the designated stops.

## Scenario

1. Startup the autonomous driving system.
   - Launch Autoware.
1. Drive the vehicle from the garage to the waiting position.
   - Drive the vehicle manually.
1. Drive the vehicle to the next bus stop.
   - Drive to the designated position.
1. Get on and off the vehicle.
   - Door operation.
1. Return to step 4 unless it's the last bus stop.
1. Drive the vehicle to the waiting position.
   - Drive to the designated position.
1. Drive the vehicle from the waiting position to the garage.
   - Drive the vehicle manually.
1. Shutdown the autonomous driving system.
   - Launch Autoware.

## Considerations

Currently, Autoware can only handle the route to next bus stop. This is suitable for on-demand driving where next bus stop changes dynamically, but it is inefficient on routes that do not change. Therefore, consider multiple routes. Also, consider how to specify the stop by name instead of pose.