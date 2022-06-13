# Use Case of Bus Service

## Overview

This use case is a taxi service that picks up passengers and drives them to their destination.

## Scenario

1. Startup the autonomous driving system.
1. Drive the vehicle from the garage to the waiting position.
1. [Drive the vehicle to the position to pick up.](./drive-designated-position.md)
1. Get on the vehicle.
1. [Drive the vehicle to the destination.](./drive-designated-position.md)
1. Get off the vehicle.
1. [Drive the vehicle to the waiting position.](./drive-designated-position.md)
1. Return to step 3 if there is another request.
1. Drive the vehicle from the waiting position to the garage.
1. Shutdown the autonomous driving system.
