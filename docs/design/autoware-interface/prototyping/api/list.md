# List of Autoware API

## External API

| Type    | Name                                                                                              | Data                                                                                                              |
| ------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| service | [/api/external/get/version](../../api/external/get/version)                                       | [autoware_external_api_msgs/srv/GetVersion](../../type/autoware_external_api_msgs/srv/GetVersion)                 |
| service | [/api/external/get/metadata/packages](../../api/external/get/metadata/packages)                   | [tier4_external_api_msgs/srv/GetMetadataPackages](../../type/tier4_external_api_msgs/srv/GetMetadataPackages)     |
| service | [/api/external/set/service](../../api/external/set/service)                                       | [tier4_external_api_msgs/srv/SetService](../../type/tier4_external_api_msgs/srv/SetService)                       |
| topic   | [/api/external/get/service](../../api/external/get/service)                                       | [tier4_external_api_msgs/msg/Service](../../type/tier4_external_api_msgs/msg/Service)                             |
| topic   | [/api/external/get/diagnostics](../../api/external/get/diagnostics)                               | [tier4_external_api_msgs/msg/ClassifiedDiagnostics](../../type/tier4_external_api_msgs/msg/ClassifiedDiagnostics) |
| service | [/api/external/set/engage](../../api/external/set/engage)                                         | [tier4_external_api_msgs/srv/Engage](../../type/tier4_external_api_msgs/srv/Engage)                               |
| topic   | [/api/external/get/engage](../../api/external/get/engage)                                         | [tier4_external_api_msgs/msg/EngageStatus](../../type/tier4_external_api_msgs/msg/EngageStatus)                   |
| service | [/api/external/set/emergency](../../api/external/set/emergency)                                   | [tier4_external_api_msgs/srv/SetEmergency](../../type/tier4_external_api_msgs/srv/SetEmergency)                   |
| topic   | [/api/external/get/emergency](../../api/external/get/emergency)                                   | [tier4_external_api_msgs/msg/Emergency](../../type/tier4_external_api_msgs/msg/Emergency)                         |
| service | [/api/external/set/door](../../api/external/set/door)                                             | [tier4_external_api_msgs/srv/SetDoor](../../type/tier4_external_api_msgs/srv/SetDoor)                             |
| topic   | [/api/external/get/door](../../api/external/get/door)                                             | [tier4_external_api_msgs/msg/DoorStatus](../../type/tier4_external_api_msgs/msg/DoorStatus)                       |
| topic   | [/api/external/get/vehicle/status](../../api/external/get/vehicle/status)                         | [tier4_external_api_msgs/msg/VehicleStatusStamped](../../type/tier4_external_api_msgs/msg/VehicleStatusStamped)   |
| service | [/api/external/set/initialize_pose](../../api/external/set/initialize_pose)                       | [tier4_external_api_msgs/srv/InitializePose](../../type/tier4_external_api_msgs/srv/InitializePose)               |
| service | [/api/external/set/initialize_pose_auto](../../api/external/set/initialize_pose_auto)             | [tier4_external_api_msgs/srv/InitializePoseAuto](../../type/tier4_external_api_msgs/srv/InitializePoseAuto)       |
| service | [/api/external/set/route](../../api/external/set/route)                                           | [tier4_external_api_msgs/srv/SetRoute](../../type/tier4_external_api_msgs/srv/SetRoute)                           |
| topic   | [/api/external/get/route](../../api/external/get/route)                                           | [tier4_external_api_msgs/msg/Route](../../type/tier4_external_api_msgs/msg/Route)                                 |
| service | [/api/external/set/clear_route](../../api/external/set/clear_route)                               | [tier4_external_api_msgs/srv/ClearRoute](../../type/tier4_external_api_msgs/srv/ClearRoute)                       |
| service | [/api/external/set/operator](../../api/external/set/operator)                                     | [tier4_external_api_msgs/srv/SetOperator](../../type/tier4_external_api_msgs/srv/SetOperator)                     |
| topic   | [/api/external/get/operator](../../api/external/get/operator)                                     | [tier4_external_api_msgs/msg/Operator](../../type/tier4_external_api_msgs/msg/Operator)                           |
| service | [/api/external/set/observer](../../api/external/set/observer)                                     | [tier4_external_api_msgs/srv/SetObserver](../../type/tier4_external_api_msgs/srv/SetObserver)                     |
| topic   | [/api/external/get/observer](../../api/external/get/observer)                                     | [tier4_external_api_msgs/msg/Observer](../../type/tier4_external_api_msgs/msg/Observer)                           |
| topic   | [/api/external/get/map/info/hash](../../api/external/get/map/info/hash)                           | [tier4_external_api_msgs/msg/MapHash](../../type/tier4_external_api_msgs/msg/MapHash)                             |
| service | [/api/external/get/map/lanelet/xml](../../api/external/get/map/lanelet/xml)                       | [tier4_external_api_msgs/srv/GetTextFile](../../type/tier4_external_api_msgs/srv/GetTextFile)                     |
| service | [/api/external/set/pause_driving](../../api/external/set/pause_driving)                           | [tier4_external_api_msgs/srv/PauseDriving](../../type/tier4_external_api_msgs/srv/PauseDriving)                   |
| service | [/api/external/set/velocity_limit](../../api/external/set/velocity_limit)                         | [tier4_external_api_msgs/srv/SetVelocityLimit](../../type/tier4_external_api_msgs/srv/SetVelocityLimit)           |
| topic   | [/api/external/set/command/local/control](../../api/external/set/command/local/control)           | [tier4_external_api_msgs/msg/ControlCommandStamped](../../type/tier4_external_api_msgs/msg/ControlCommandStamped) |
| topic   | [/api/external/set/command/local/shift](../../api/external/set/command/local/shift)               | [tier4_external_api_msgs/msg/GearShiftStamped](../../type/tier4_external_api_msgs/msg/GearShiftStamped)           |
| topic   | [/api/external/set/command/local/turn_signal](../../api/external/set/command/local/turn_signal)   | [tier4_external_api_msgs/msg/TurnSignalStamped](../../type/tier4_external_api_msgs/msg/TurnSignalStamped)         |
| topic   | [/api/external/set/command/local/heartbeat](../../api/external/set/command/local/heartbeat)       | [tier4_external_api_msgs/msg/Heartbeat](../../type/tier4_external_api_msgs/msg/Heartbeat)                         |
| topic   | [/api/external/set/command/remote/control](../../api/external/set/command/remote/control)         | [tier4_external_api_msgs/msg/ControlCommandStamped](../../type/tier4_external_api_msgs/msg/ControlCommandStamped) |
| topic   | [/api/external/set/command/remote/shift](../../api/external/set/command/remote/shift)             | [tier4_external_api_msgs/msg/GearShiftStamped](../../type/tier4_external_api_msgs/msg/GearShiftStamped)           |
| topic   | [/api/external/set/command/remote/turn_signal](../../api/external/set/command/remote/turn_signal) | [tier4_external_api_msgs/msg/TurnSignalStamped](../../type/tier4_external_api_msgs/msg/TurnSignalStamped)         |
| topic   | [/api/external/set/command/remote/heartbeat](../../api/external/set/command/remote/heartbeat)     | [tier4_external_api_msgs/msg/Heartbeat](../../type/tier4_external_api_msgs/msg/Heartbeat)                         |
| topic   | [/api/external/get/command/selected/control](../../api/external/get/command/selected/control)     | [tier4_external_api_msgs/msg/ControlCommandStamped](../../type/tier4_external_api_msgs/msg/ControlCommandStamped) |
| topic   | [/api/external/get/command/selected/vehicle](../../api/external/get/command/selected/vehicle)     | [tier4_external_api_msgs/msg/ControlCommandStamped](../../type/tier4_external_api_msgs/msg/ControlCommandStamped) |