# Pose API

- {{ link_ad_api('/api/pose/state') }}
- {{ link_ad_api('/api/pose/initialize') }}

## Description

This API manages the initialization of the vehicle pose.

## States

![pose-reset-state](./state.drawio.svg)

| State        | Description                                                             |
| ------------ | ----------------------------------------------------------------------- |
| UNAVAILABLE  | The vehicle pose is not available. Waiting for the reset request.       |
| INITIALIZING | The vehicle pose is not available. The reset is processing.             |
| AVAILABLE    | The vehicle pose is available. The reset request can be accepted again. |
