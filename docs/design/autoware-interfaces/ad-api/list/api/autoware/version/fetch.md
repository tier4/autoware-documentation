---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/FetchAutowareVersion
---

# /api/autoware/version/fetch

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the list of available Autoware versions. The version follows the target meta-repository.

## Request

| Name   | Type | Description                       |
| ------ | ---- | --------------------------------- |
| update | bool | update the list using the network |

## Response

| Name     | Type     | Description        |
| -------- | -------- | ------------------ |
| versions | string[] | available versions |
