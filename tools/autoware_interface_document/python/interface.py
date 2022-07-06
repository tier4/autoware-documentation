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
from .util import hook_markdown_link

class AutowareInterface(object):

    def __init__(self, path, msgs):
        self.path = path
        self.yaml = yaml.safe_load(path.read_text())

        depth = self.name.count("/")
        self.type = _TypeReference(msgs[self.yaml["interface"]["type"]], depth)

        self.yaml["description"] = hook_markdown_link(self.yaml["description"], depth)
        if self.method == "notification":
            for field in self.message:
                field["text"] = hook_markdown_link(field["text"], depth)

        for field in self.yaml.get("message", []):
            field["type"] = self.type.type.spec.access(field["name"]).text
        for field in self.yaml.get("request", []):
            field["type"] = self.type.type.spec.req.access(field["name"]).text
        for field in self.yaml.get("response", []):
            field["type"] = self.type.type.spec.res.access(field["name"]).text

    @property
    def name(self):
        return self.yaml["interface"]["name"]

    @property
    def file(self):
        return self.name.strip("/") + ".md"

    @property
    def method(self):
        return self.yaml["interface"]["method"]

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
        filename = "function-call" if self.method == "function call" else "notification"
        template = templates.get_template(f"interface-{filename}.jinja2")
        path = output_path / self.file
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(template.render(interface=self))

    @staticmethod
    def GenerateIndex(output_path, apis):
        text = "# List of Autoware AD API\n\n"
        apis = "".join(f"- [{api.name}]({api.file})\n" for api in apis)
        path = output_path / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + apis)


class _TypeReference(object):

    def __init__(self, type, depth):
        self.type = type
        self.depth = depth

    @property
    def link(self):
        parents = "../" * self.depth + "types/"
        return f"[{self.type.name}]({parents}{self.type.file})"