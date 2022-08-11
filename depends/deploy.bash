#!/bin/bash
source install/setup.bash
ros2 run autoware_interface_document generate
find docs/design/autoware-interfaces/ad-api | xargs pre-commit run --files
# mike deploy HEAD
