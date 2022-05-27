---
autoware_interface:
  method: function call
  type: autoware_ad_api_msgs/srv/GetInterfaceVersion
---

# /api/version

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the API version. The version follows SemVer.

## Request

None

## Response

| Name    | Type   | Description                                  |
| ------- | ------ | -------------------------------------------- |
| version | string | version string in `major.minor.patch` format |
| major   | uint32 | major version                                |
| minor   | uint32 | minor version                                |
| patch   | uint32 | patch version                                |
