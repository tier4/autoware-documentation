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

import yaml
from pathlib import Path
from .util import hook_markdown_link

class AutowareInterface(object):

    def __init__(self, path):
        self.path = path
        self.yaml = yaml.safe_load(path.read_text())

        depth = self.name.count("/")
        self.yaml["description"] = hook_markdown_link(self.yaml["description"], depth)
        if self.type == "notification":
            for field in self.message:
                field["text"] = hook_markdown_link(field["text"], depth)

    @property
    def name(self):
        return self.yaml["interface"]["name"]

    @property
    def data(self):
        return self.yaml["interface"]["data"]

    @property
    def type(self):
        return self.yaml["interface"]["type"]

    @property
    def link(self):
        return f".{self.name}.md"

    @property
    def description(self):
        return self.yaml["description"]

    @property
    def message(self):
        return self.yaml["message"]

    @property
    def request(self):
        return self.yaml["request"]

    @property
    def response(self):
        return self.yaml["response"]

    def generate(self, output_path, templates):
        filename = self.type.replace(" ", "-")
        template = templates.get_template(f"interface-{filename}.jinja2")
        name = self.name.strip("/") + ".md"
        path = output_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(template.render(interface=self))

    @staticmethod
    def GenerateIndex(output_path, apis):
        text = "# List of Autoware AD API\n\n"
        apis = "".join(f"- [{api.name}]({api.link})\n" for api in apis)
        path = output_path / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + apis)
