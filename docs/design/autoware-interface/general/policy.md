# Autoware Interface Policy

## Communication Method

As shown in the table below, interfaces are classified into four communication methods to define their behavior.

| Communication Method | ROS 2 Interface                   | Optional Interface   |
| -------------------- | --------------------------------- | -------------------- |
| Function Call        | Service                           | HTTP                 |
| Notification         | Topic (reliable, transient_local) | MQTT (QoS=2, retain) |
| Reliable Stream      | Topic (reliable, volatile)        | MQTT (QoS=2)         |
| Realtime Stream      | Topic (best_effort, volatile)     | MQTT (QoS=0)         |

Function Call is a request-response communication and is used for processing that requires immediate results. The others are publish-subscribe communication.
Notification is used to process data that changes with some event, typically a callback. Streams handle continuously changing data.
Reliable Stream expects all data to arrive without loss, Realtime Stream expects the latest data to arrive with low delay.

These methods are provided as services or topics of ROS 2 since Autoware is developed using ROS 2 and mainly communicates with its packages.
HTTP and MQTT are recommended as additional options for applications that do not use ROS 2 because these protocols are widely used and can substitute the behavior of services and topics. In that case, text formats such as JSON, where field names are repeated in an array of objects, are inefficient and it is necessary to consider the serialization method.

## Naming Convention

The name of the interface must be `/<component name>/api/<interface name>`,
where `<component name>` is the name of the component. For an AD API component, omit this part and start with `/api`.
The `<interface name>` is an arbitrary string separated by slashes, and all parts except the last must be nouns.
Note that this rule causes a restriction that the namespace `api` must not be used as a name other than AD API and Component Interface.

The following are examples of correct interface names for AD API and Component Interface:

- /api/autoware/state
- /api/autoware/engage
- /planning/api/route/change
- /vehicle/api/status

The following are examples of incorrect interface names for AD API and Component Interface:

- /autoware/state
- /api/engage/autoware
- /planning/route/api
- /vehicle/my_api/status

## Logging

If logging is needed, rosbag is available for topics and use logger in rclcpp or rclpy for services.

## Stream Frequency

Set the recommended and minimum frequency for Stream. The minimum frequency is used for diagnostics.

## Restrictions

Consider the following restrictions and describe if necessary.

- response time
- pre-condition
- post-condition
- execution order
- concurrent execution
- etc.

## Response Status

Function Call uses the following response code to handle the return value in general.

| Group  | Code   | Description  |
| ------ | ------ | ------------ |
| 0x0000 | 0x0000 | Unknown      |
| 0x1000 | -      | OK           |
| 0x1000 | 0x1001 | Success      |
| 0x1000 | 0x1002 | Accepted     |
| 0x1000 | 0x1003 | NoEffect     |
| T.B.D. | T.B.D. | Unavailable  |
| T.B.D. | T.B.D. | Warning      |
| T.B.D. | T.B.D. | Error        |
| T.B.D. | T.B.D. | Forbidden    |
| T.B.D. | T.B.D. | NotSupported |
| T.B.D. | T.B.D. | Timeout      |
