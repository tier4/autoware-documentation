---
autoware_interface:
  method: notification
  type: autoware_adapi_v1_msgs/msg/AutowareLauncherState
---

# /api/autoware/launcher/state

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the launcher state. For details, see the [launcher state](../../../../features/launcher-state.md).

## Message

| Name  | Type          | Description    |
| ----- | ------------- | -------------- |
| state | enum (uint32) | launcher state |
