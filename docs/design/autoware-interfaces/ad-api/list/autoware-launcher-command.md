# /api/autoware/launcher/command

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/AutowareLauncherCommand](../type/autoware_ad_api_msgs/srv/autoware_launcher_command.md)

## Description

Launch or terminate Autoware. This API changes the [launcher state](../features/launcher-state.md).

## Request

| Name    | Type          | Description      |
| ------- | ------------- | ---------------- |
| command | enum (uint32) | launcher command |

## Response

None
