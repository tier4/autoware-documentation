# /api/interface/version

- Method: function call
- Type: [autoware_ad_api_msgs/srv/InterfaceVersion](../../../types/autoware_ad_api_msgs/srv/interface_version.md)

## Description

Get the interface version. The version follows SemVer.

## Request

None

## Response

| Name  | Type   | Description   |
| ----- | ------ | ------------- |
| major | uint16 | major version |
| minor | uint16 | minor version |
| patch | uint16 | patch version |