# /api/pose_reset/request

- Method: function call
- Type: [autoware_ad_api_msgs/srv/PoseResetRequest](../../../types/autoware_ad_api_msgs/srv/pose_reset_request.md)

## Description

Request to initialize or reset the vehicle pose. For details, see the [pose reset state](../../../features/pose-reset.md).

## Request

| Name | Type                                        | Description                                                                          |
| ---- | ------------------------------------------- | ------------------------------------------------------------------------------------ |
| pose | geometry_msgs/msg/PoseWithCovarianceStamped | The initial guess for pose estimation. If not specified, the GNSS pose will be used. |

## Response

| Name   | Type                                    | Description     |
| ------ | --------------------------------------- | --------------- |
| status | autoware_ad_api_msgs/msg/ResponseStatus | response status |
