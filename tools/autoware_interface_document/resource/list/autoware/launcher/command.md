---
autoware_interface:
  method: function call
  type: autoware_adapi_v1_msgs/srv/AutowareLauncherCommand
---

# /api/autoware/launcher/command

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Launch or terminate Autoware. This API changes the [launcher state](../../../../features/launcher-state.md).

## Request

| Name    | Type          | Description      |
| ------- | ------------- | ---------------- |
| command | enum (uint32) | launcher command |

## Response

None
