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
import logging
import shutil
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .interface import AutowareInterface
from .structure import AutowareStructure

def generate():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", default="docs/design/autoware-interfaces/ad-api", nargs="?")
    args = parser.parse_args()

    source_path = Path(get_package_share_directory("autoware_interface_document"))
    output_path = Path(args.path)
    api_path = output_path / "list"
    msg_path = output_path / "types"
    templates = Environment(loader=FileSystemLoader(source_path / "templates"), trim_blocks=True)

    # clean_target(api_path)
    # clean_target(msg_path)

    msgs = list_msgs()
    for msg in msgs.values(): msg.generate(msg_path, templates)
    # AutowareStructure.GenerateIndex(msg_path, msgs.values())

    apis = list_apis(source_path / "resource", msgs)
    for api in apis.values(): api.generate(api_path, templates)
    # AutowareInterface.GenerateIndex(api_path, apis.values())


def clean_target(target_path):
    for path in target_path.iterdir():
        if path.is_dir():
            shutil.rmtree(path)


def list_msgs():
    packages = ["autoware_adapi_version_msgs", "autoware_adapi_v1_msgs"]
    msgs = dict()
    for package in packages:
        path = Path(get_package_share_directory(package))
        for file in path.glob("msg/**/*.msg"):
            msg = AutowareStructure(file)
            msgs[msg.name] = msg
        for file in path.glob("srv/**/*.srv"):
            msg = AutowareStructure(file)
            msgs[msg.name] = msg
    for msg in msgs.values(): msg.link_relations(msgs)
    for msg in msgs.values(): msg.sort_relations()
    return dict(sorted(msgs.items()))


def list_apis(source_path: Path, msgs: dict):
    apis = dict()
    for path in (source_path / "list").glob("**/*.yaml"):
        data = AutowareInterface(path, msgs)
        apis.setdefault(data.name, []).append(data)
    for name, data in apis.items():
        if len(data) != 1:
            logging.error(f"The API name '{name}' is duplicated.")
    return {name: data[0] for name, data in apis.items()}
