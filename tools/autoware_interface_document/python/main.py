# Copyright 2022 TIER IV, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import yaml
import logging
from collections import OrderedDict
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from .type import InterfaceName
from .type import InterfaceType


def generate():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", default="docs/design/autoware-interface/ad-api", nargs="?")
    args = parser.parse_args()

    base_path = Path(args.path)
    list_path = Path(get_package_share_directory("autoware_interface_document")) / "resource" / "adapi.yaml"
    api_path = base_path / "list"
    msg_path = base_path / "type"

    msgs = list_msgs()
    for msg in msgs.values():
        print(msg.name)
        msg.write(msg_path)
    InterfaceType.WriteIndex(msg_path, msgs.values())

    apis = list_apis(base_path, list_path)
    for api in apis.values():
        print(api.name)
        api.rewrite()
    InterfaceName.WriteIndex(api_path, apis.values())


def list_apis(base_path: Path, list_path: Path):
    apis = OrderedDict()
    for name in yaml.safe_load(list_path.read_text()):
        apis[name] = None
    for file in (base_path / "list").iterdir():
        if file.is_dir() or file.name in {".pages", "index.md"}:
            continue
        api = InterfaceName(file)
        if api.name not in apis:
            logging.warning(F"API name is not found in list: {api.name}")
            continue
        apis[api.name] = api.init()
    for name in apis:
        if apis[name] is None:
            logging.warning(F"API name is not found in file: {name}")
    return OrderedDict(item for item in apis.items() if item[1])


def list_msgs():
    packages = ["autoware_ad_api_msgs"]
    msgs = {}
    for package in packages:
        path = Path(get_package_share_directory(package))
        for file in (path / "msg").iterdir():
            if file.suffix == ".msg":
                msg = InterfaceType(file)
                msgs[msg.name] = msg
        for file in (path / "srv").iterdir():
            if file.suffix == ".srv":
                msg = InterfaceType(file)
                msgs[msg.name] = msg
    for msg in msgs.values():
        msg.refer(msgs)
    return msgs
