# /api/pose_initialization/request

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/PoseInitializationRequest](../type/autoware_ad_api_msgs/srv/pose_initialization_request.md)

## Description

Request the pose initialization based on the specified pose. This API changes the [pose initialization state](../data/pose-initialization-state.md).

## Request

| Name | Type                                        | Description  |
| ---- | ------------------------------------------- | ------------ |
| pose | geometry_msgs/msg/PoseWithCovarianceStamped | initial pose |

## Response

None
