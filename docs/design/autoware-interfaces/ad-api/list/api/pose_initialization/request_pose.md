---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/PoseInitializationRequest
---

# /api/pose_initialization/request

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Request the pose initialization based on the specified pose. This API changes the [pose initialization state](../../../features/pose-initialization-state.md).

## Request

| Name | Type                                        | Description  |
| ---- | ------------------------------------------- | ------------ |
| pose | geometry_msgs/msg/PoseWithCovarianceStamped | initial pose |

## Response

None
