# Motion API

## Description

The motion feature manages the behavior that the vehicle plans.

## States

![motion-state](./motion-state.drawio.svg)

| State    | Description                                          |
| -------- | ---------------------------------------------------- |
| STOPPED  | The vehicle is stopped.                              |
| STARTING | The vehicle is about to start (it is still stopped). |
| MOVING   | The vehicle is moving.                               |

## Factors

The motion factors are information on the behavior that the vehicle plans.
The factors are an array sorted by distance.
There are two types of factors, stop and direction change.
For each type, the meanings of the data members are as follows.

- stop type

  | Name     | Description                                                   |
  | -------- | ------------------------------------------------------------- |
  | pose     | The pose of the stop point.                                   |
  | distance | Distance to the above pose.                                   |
  | reason   | Reason (e.g. stop line, crosswalk, obstacle, traffic signal). |
  | status   | Whether the vehicle is stopped due to this factor.            |
  | detail   | Additional information.                                       |

- direction change type

  | Name     | Description                                                  |
  | -------- | ------------------------------------------------------------ |
  | pose     | The pose to turn on/off the blinker.                         |
  | distance | Distance to the above pose.                                  |
  | reason   | Reason (e.g. turning, lane change, avoidance).               |
  | status   | Whether the direction change has started due to this factor. |
  | detail   | Additional information.                                      |

## Related API

- /api/motion/state
- /api/motion/factors
