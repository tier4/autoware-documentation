# /api/version

- Method: Function Call
- Type: autoware_ad_api_msgs/srv/GetInterfaceVersion

## Description

Get the API version. The version numbers follow SemVer.

## Request

None

## Response

| Name    | Type                                    | Description                                  |
| ------- | --------------------------------------- | -------------------------------------------- |
| status  | autoware_ad_api_msgs/msg/ResponseStatus | response status                              |
| version | string                                  | version string in `major.minor.patch` format |
| major   | uint32                                  | major version                                |
| minor   | uint32                                  | minor version                                |
| patch   | uint32                                  | patch version                                |
