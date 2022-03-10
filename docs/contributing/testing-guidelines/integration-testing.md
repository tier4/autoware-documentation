# Integration Testing

This article explains how to write integration tests.

## Introduction

An Integration test is a type of software testing that tests a collection of software modules. Integration tests occur after unit tests, and before validation tests.

Integration tests verify that independently developed software modules work correctly when the modules are connected to each other. In ROS 2, the software modules are called nodes. As a special case, testing a single node can be referred to as component testing.

## Value of integration testing

Integration tests help to find the following types of errors:

- Incompatible interaction between nodes, such as non-matching topics, different message types, or incompatible QoS settings
- Reveal edge cases that were not touched with unit tests, such as a critical timing issue, network communication delay, disk I/O failure, and many other problems that can occur in production environments
- Using tools like `stress` and `udpreplay`, performance of nodes is tested with real data or while the system is under high CPU/memory load, where situations such as `malloc` failures can be detected

With ROS 2, it is possible to program complex autonomous-driving applications with a large number of nodes. Therefore, a lot of effort has been made to provide an integration-test framework that helps developers test the interaction of ROS2 nodes.

## Integration-test framework

A typical integration-test framework has three parts:

1. A series of executables that work together and generate outputs
2. A series of expected outputs that should match the output of the executables
3. A launcher that starts the tests, compares the outputs to the expected outputs, and determines if the test passes

In Autoware, we use the [launch_testing](https://github.com/ros2/launch/tree/master/launch_testing) framework.

### Smoke tests

Autoware has dedicated API for smoke testing.

Smoke test ensure that node can be:

1. launched with default parameter file.
2. terminated with a standard `SIGTERM` signal.

To use this framework, in `package.xml` add:

```xml
<test_depend>autoware_testing</test_depend>
```

and in `CMakeLists.txt` add:

```cmake
if(BUILD_TESTING)
  find_package(autoware_testing REQUIRED)
  add_smoke_test(${PROJECT_NAME} ${NODE_NAME})
endif()
```

For full API documentation see [package design page](https://github.com/autowarefoundation/autoware.universe/blob/main/common/autoware_testing/design/autoware_testing-design.md).

Note that this API is not suitable for all smoke test cases. For example, it can not be used when some specific file location, like map, is required to be passed to the node or some preparation need to be conducted before node launch. In such cases use manual solution from [section below](#integration-test-with-a-single-node-component-test).

### Interface tests

Autoware has dedicated API for interface testing.

Interface test ensure that node can be:

1. node consumes/produces the desired output in line with the high-level documentation of its design document.
2. helps to keep the docs up to date and to prevent users from having to dig through the source code to find the topic names/types.

To use this framework, create interface definition file:

```yaml
input_topics:
  - name: ~/input/lateral/control_cmd
    type: autoware_auto_control_msgs/msg/AckermannLateralCommand
  - name: ~/input/longitudinal/control_cmd
    type: autoware_auto_control_msgs/msg/LongitudinalCommand
output_topics:
  - name: ~/output/control_cmd
    type: autoware_auto_control_msgs/msg/AckermannControlCommand
```

in `package.xml`, add:

```xml
<test_depend>autoware_testing</test_depend>
```

and in `CMakeLists.txt` add:

```cmake
if(BUILD_TESTING)
  find_package(autoware_testing REQUIRED)
  add_interface_test(${PROJECT_NAME} ${NODE_NAME} ${TOPIC_FILENAME})
endif()
```

For full API documentation see [package design page](https://github.com/autowarefoundation/autoware.universe/blob/main/common/autoware_testing/design/autoware_testing-design.md).

### Integration test with a single node: component test

The simplest scenario is a single node. In this case, the integration test is commonly referred to as a component test.

Component testing can verify that the inputs and outputs of a node are in accordance with specifications.

To add a component test to an existing node, follow the example of the `lanelet2_map_provider` package that has an executable named `lanelet2_map_provider_exe`.

In `package.xml`, add

```xml
<test_depend>ros_testing</test_depend>
```

In `CMakeLists.txt`, add or modify the `BUILD_TESTING` section:

```cmake
if(BUILD_TESTING)
  add_ros_test(
    test/lanelet2_map_provider_launch.test.py
    TIMEOUT "30"
  )
endif()
```

The `TIMEOUT` argument is given in seconds; see [here](https://github.com/ros2/ros_testing/blob/master/ros_testing/cmake/add_ros_test.cmake) for details.

To create test follow [launch_testing quick-start example](https://github.com/ros2/launch/tree/master/launch_testing#quick-start-example).

### Next steps

The simple test described in [Integration test with a single node: component test](integration-test-with-a-single-node-component-test) can be extended in numerous directions:

#### Running multiple nodes together

To run multiple nodes together, simply add more nodes to the launch description in `*launch.test.py`.
The lidar stack has more elaborate examples on how to feed input and to test more than just the exit status of nodes; see [point_cloud_filter_transform_tf_publisher.test.py](https://gitlab.com/autowarefoundation/autoware.auto/AutowareAuto/-/blob/master/src/perception/filters/point_cloud_filter_transform_nodes/test/point_cloud_filter_transform_tf_publisher.test.py) for details.

## References

1. [colcon](https://github.com/ros2/ros2/wiki/Colcon-Tutorial) is used to build and run test.
2. [launch testing](https://github.com/ros2/launch/tree/master/launch_testing) launches nodes and runs tests.
3. [Testing in general](testing-in-general.md) describes the big picture of testing.
