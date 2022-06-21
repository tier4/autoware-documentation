# Pose Reset API

- {{ link_ad_api('/api/pose_reset/state') }}
- {{ link_ad_api('/api/pose_reset/request') }}

## Description

This API manages the initialization of the vehicle pose.

## States

![pose-reset-state](./state.drawio.svg)

| State      | Description                                                             |
| ---------- | ----------------------------------------------------------------------- |
| WAITING    | The vehicle pose is not available. Waiting for the reset request.       |
| PROCESSING | The vehicle pose is not available. The reset is processing.             |
| COMPLETED  | The vehicle pose is available. The reset request can be accepted again. |
