# /api/operation_mode/state

- Method: notification
- Type: [autoware_ad_api_msgs/msg/OperationModeState](../../../types/autoware_ad_api_msgs/msg/operation_mode_state.md)

## Description

Get the operation mode state. For details, see the [operation mode](./index.md).

## Message

| Name                         | Type                                   | Description                                              |
| ---------------------------- | -------------------------------------- | -------------------------------------------------------- |
| mode                         | autoware_ad_api_msgs/msg/OperationMode | The selected command for Autoware control.               |
| is_autoware_control_enabled  | bool                                   | True if vehicle control by Autoware is enabled.          |
| is_in_transition             | bool                                   | True if the operation mode is in transition.             |
| is_stop_mode_available       | bool                                   | True if the operation mode can be changed to stop.       |
| is_autonomous_mode_available | bool                                   | True if the operation mode can be changed to autonomous. |
| is_local_mode_available      | bool                                   | True if the operation mode can be changed to local.      |
| is_remote_mode_available     | bool                                   | True if the operation mode can be changed to remote.     |
