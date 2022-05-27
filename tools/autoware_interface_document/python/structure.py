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

import re
from .util import camel_to_snake


builtins = {"bool", "byte", "char", "float32", "float64", "string", "wstring"}
for byte in (8, 16, 32, 64):
    builtins.add(F"int{byte}")
    builtins.add(F"uint{byte}")


class AutowareStructure(object):

    def __init__(self, path):
        self.path = path
        self.text = path.read_text().strip()
        self.uses = set()
        self.used = set()

    @property
    def name(self):
        return "/".join(self.path.with_suffix("").parts[-3:])

    @property
    def file(self):
        parts = self.name.split("/")
        return "/".join([*parts[:-1], camel_to_snake(parts[-1])]) + ".md"

    def generate(self, output_path, templates):
        template = templates.get_template(f"interface-structure.jinja2")
        path = output_path / self.file
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(template.render(interface=self))

    @staticmethod
    def GenerateIndex(output_path, msgs):
        text = "# Types of Autoware AD API\n\n"
        msgs = "".join(f"- [{msg.name}]({msg.file})\n" for msg in msgs)
        path = output_path / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + msgs)

    @staticmethod
    def __uses(text):
        regex = re.compile("(\w+)/(\w+)")
        types = (regex.match(line) for line in text.split("\n"))
        types = (match for match in types if match is not None)
        return {match.group(1) + "/msg/" + match.group(2) for match in types}

    def link_relations(self, types):
        for name in self.__uses(self.text):
            if name in types:
                type = types[name]
                self.uses.add(type)
                type.used.add(self)

    def sort_relations(self):
        self.uses = list(sorted(self.uses, key=lambda t: t.name))
        self.used = list(sorted(self.used, key=lambda t: t.name))
