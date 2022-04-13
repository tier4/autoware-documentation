---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/SetAutowareVersion
---

# /api/autoware/version/change

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Change the Autoware version. The version follows the target meta-repository.

## Request

| Name    | Type   | Description    |
| ------- | ------ | -------------- |
| version | string | target version |

## Response

None
