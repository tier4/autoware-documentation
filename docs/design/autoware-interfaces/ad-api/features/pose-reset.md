# Pose Reset API

## Description

The pose reset feature manages the initialization of the vehicle pose.

## Pose Reset State

![pose-reset-state](./pose-reset-state.drawio.svg)

| State      | Description                                                             |
| ---------- | ----------------------------------------------------------------------- |
| WAITING    | The vehicle pose is not available. Waiting for the reset request.       |
| PROCESSING | The vehicle pose is not available. The reset is processing.             |
| COMPLETED  | The vehicle pose is available. The reset request can be accepted again. |

## Related API

- /api/pose_reset/state
- /api/pose_reset/request
