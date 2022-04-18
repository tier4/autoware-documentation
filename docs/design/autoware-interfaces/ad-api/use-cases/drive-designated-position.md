# Drive to the designated position

## Related features

- [Route](../features/route-state.md)
- [Driving](../features/driving-state.md)

## Scenario

1. 目的地が設定されているか確認する (route/state=unset)
1. 目的地を設定する (route/set)
1. 目的地が設定されたか確認する(route/state=set)
1. 発車可能か確認する(driving/state=ready)
1. 発車する(driving/engage)
1. 発車したか確認する(driving/state=driving)
1. 目的地に付いたか確認する (route/state=arrived)
