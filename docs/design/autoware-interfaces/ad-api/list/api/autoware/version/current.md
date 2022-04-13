---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/GetAutowareVersion
---

# /api/autoware/version/current

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the Autoware version. The version follows the target meta-repository.

## Request

None

## Response

| Name    | Type   | Description     |
| ------- | ------ | --------------- |
| version | string | current version |
