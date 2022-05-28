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
from rosidl_adapter.parser import parse_message_string, parse_service_string
from .util import camel_to_snake


builtins = {"bool", "byte", "char", "float32", "float64", "string", "wstring"}
for byte in (8, 16, 32, 64):
    builtins.add(F"int{byte}")
    builtins.add(F"uint{byte}")


class AutowareStructure(object):

    def __init__(self, path):
        self.path = path
        self.text = path.read_text().strip()
        self.uses = []
        self.used = []
        self.spec = _MessageSpec(path.parts[-3], path.parts[-2], path.stem, self.text)

    @property
    def name(self):
        return "/".join(self.path.with_suffix("").parts[-3:])

    @property
    def file(self):
        parts = self.name.split("/")
        return "/".join([*parts[:-1], camel_to_snake(parts[-1])]) + ".md"

    def get_field(self, group, path):
        field = self
        for name in path.split("."):
            field = field.spec.fields[group][name].type
            group = "msg"
        return field

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

    def link_relations(self, types):
        self.uses = set()
        self.used = set()
        for name in set(self.spec.uses):
            if name in types:
                type = types[name]
                self.uses.add(type)
                type.used.add(self)
        for fields in self.spec.fields.values():
            for field in fields.values():
                field.type = types.get(field.type.name, field.type)

    def sort_relations(self):
        self.uses = list(sorted(self.uses, key=lambda t: t.name))
        self.used = list(sorted(self.used, key=lambda t: t.name))


class _MessageSpec(object):

    def __init__(self, package, type, name, definition):
        self.fields = dict()
        if type == "msg":
            spec = parse_message_string(package, name, definition)
            self.fields["msg"] = self.__fields(spec.fields)
        if type == "srv":
            spec = parse_service_string(package, name, definition)
            self.fields["req"] = self.__fields(spec.request.fields)
            self.fields["res"] = self.__fields(spec.response.fields)

    @staticmethod
    def __fields(fields):
        fields = [_MessageField(field) for field in fields]
        return {field.name: field for field in fields}

    @property
    def uses(self):
        for fields in self.fields.values():
            for field in fields.values():
                if not field.type.is_primitive:
                    yield field.type.name


class _MessageField(object):

    def __init__(self, field):
        self.name = field.name
        self.type = _MessageTypeDummy(field.type.pkg_name, field.type.type)
        self.list = self.__list(field.type) if field.type.is_array else None

    @staticmethod
    def __list(type):
        bound = "<=" if type.is_upper_bound else ""
        return f"[{bound}{type.array_size}]"


class _MessageTypeDummy(object):

    def __init__(self, pkg, msg):
        self.pkg = pkg
        self.msg = msg

    @property
    def name(self):
        return f"{self.pkg}/msg/{self.msg}" if self.pkg else self.msg

    @property
    def is_primitive(self):
        return self.pkg is None
