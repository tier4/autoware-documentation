# autoware_ad_api_msgs/msg/RouteState

## Definition

```txt
# constants for both states
uint32 UNKNOWN = 0

# constants for main states
uint32 UNSET = 1
uint32 SET = 2
uint32 CHANGING = 3

# constants for goal states
uint32 ON_THE_WAY = 1
uint32 ARRIVE_SOON = 2
uint32 ARRIVED_GOAL = 3

# fields
uint32 main_state
uint32 goal_state
```
