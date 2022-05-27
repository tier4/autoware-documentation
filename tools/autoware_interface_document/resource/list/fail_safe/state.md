---
autoware_interface:
  method: notification
  type: autoware_ad_api_msgs/msg/FailSafeState
---

# /api/fail_safe/state

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the fail safe state. For details, see the [fail safe state](../../../features/fail-safe-state.md).

## Message

| Name        | Type   | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| state       | uint32 | fail safe state                                |
| recoverable | bool   | fail safe state can be recovered automatically |
