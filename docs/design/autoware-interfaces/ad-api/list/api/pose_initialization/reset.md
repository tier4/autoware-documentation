---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/PoseInitializationReset
---

# /api/pose_initialization/reset

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Reset the pose initialization state. This API changes the [pose initialization state](../../../features/pose-initialization-state.md).

## Request

None

## Response

None
