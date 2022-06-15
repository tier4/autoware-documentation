# Use Case of Bus Service

## Overview

This use case is a bus service that goes around the designated stops.

## Scenario

| Step | Operation                                                  | Use Case                                                         |
| ---- | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| 1    | Startup the autonomous driving system.                     | [Launch and terminate](launch-terminate.md)                      |
| 2    | Drive the vehicle from the garage to the waiting position. | [Drive manually](drive-manually.md)                              |
| 3    | Drive the vehicle to the next bus stop.                    | [Drive to the designated position](drive-designated-position.md) |
| 4    | Get on and off the vehicle.                                |                                                                  |
| 5    | Return to step 3 unless it's the last bus stop.            |                                                                  |
| 6    | Drive the vehicle to the waiting position.                 | [Drive to the designated position](drive-designated-position.md) |
| 7    | Drive the vehicle from the waiting position to the garage. | [Drive manually](drive-manually.md)                              |
| 8    | Shutdown the autonomous driving system.                    | [Launch and terminate](launch-terminate.md)                      |
