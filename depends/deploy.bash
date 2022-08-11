#!/bin/bash
source install/setup.bash
ros2 run autoware_interface_document generate
pre-commit run -a
mike deploy HEAD
