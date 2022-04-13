# /api/version

- Method: Function Call
- Type: [autoware_ad_api_msgs/srv/GetInterfaceVersion](../types/autoware_ad_api_msgs/srv/get_interface_version.md)

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
