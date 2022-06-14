# Pose Reset API

- [/api/pose_reset/state](../list/api/pose_reset/state.md)
- [/api/pose_reset/request](../list/api/pose_reset/request.md)

## Description

This API manages the initialization of the vehicle pose.

## States

![pose-reset-state](./pose-reset-state.drawio.svg)

| State      | Description                                                             |
| ---------- | ----------------------------------------------------------------------- |
| WAITING    | The vehicle pose is not available. Waiting for the reset request.       |
| PROCESSING | The vehicle pose is not available. The reset is processing.             |
| COMPLETED  | The vehicle pose is available. The reset request can be accepted again. |
