# /api/autoware/version/fetch

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/FetchAutowareVersion](../type/autoware_ad_api_msgs/srv/fetch_autoware_version.md)

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
