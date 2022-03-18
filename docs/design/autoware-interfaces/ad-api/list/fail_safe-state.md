# /api/fail_safe/state

- Method: Notification
- Type: [autoware_ad_api_msgs/msg/FailSafeState](../type/autoware_ad_api_msgs/msg/fail_safe_state.md)

## Description

Get the fail safe state. For details, see the [fail safe state](../data/fail-safe-state.md).

## Message

| Name        | Type   | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| state       | uint32 | fail safe state                                |
| recoverable | bool   | fail safe state can be recovered automatically |
