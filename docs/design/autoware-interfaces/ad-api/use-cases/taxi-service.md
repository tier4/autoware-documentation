# Use Case of Bus Service

## Overview

This use case is a taxi service that picks up passengers and drives them to their destination.

## Scenario

| Step | Operation                                                  | Use Case                                                         |
| ---- | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| 1    | Startup the autonomous driving system.                     | [Launch and terminate](launch-terminate.md)                      |
| 2    | Drive the vehicle from the garage to the waiting position. |                                                                  |
| 3    | Drive the vehicle to the position to pick up.              | [Drive to the designated position](drive-designated-position.md) |
| 4    | Get on the vehicle.                                        |                                                                  |
| 5    | Drive the vehicle to the destination.                      | [Drive to the designated position](drive-designated-position.md) |
| 6    | Get off the vehicle.                                       |                                                                  |
| 7    | Drive the vehicle to the waiting position.                 | [Drive to the designated position](drive-designated-position.md) |
| 8    | Return to step 3 if there is another request.              |                                                                  |
| 9    | Drive the vehicle from the waiting position to the garage. |                                                                  |
| 10   | Shutdown the autonomous driving system.                    | [Launch and terminate](launch-terminate.md)                      |
