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
        self.uses = set()
        self.used = set()
        self.spec = self.__spec(path.parts[-3], path.parts[-2], path.stem, self.text)

    @staticmethod
    def __spec(package, type, name, definition):
        if type == "msg":
            return _MessageSpec(parse_message_string(package, name, definition))
        if type == "srv":
            return _ServiceSpec(parse_service_string(package, name, definition))

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

    def link_relations(self, types):
        for name in set(self.spec.uses):
            if name in types:
                type = types[name]
                self.uses.add(type)
                type.used.add(self)
        self.spec.link(types)


    def sort_relations(self):
        self.uses = list(sorted(self.uses, key=lambda t: t.name))
        self.used = list(sorted(self.used, key=lambda t: t.name))


class _ServiceSpec(object):

    def __init__(self, spec):
        self.req = _MessageSpec(spec.request)
        self.res = _MessageSpec(spec.response)

    def link(self, types):
        pass

    @property
    def uses(self):
        for name in self.req.uses:
            yield name
        for name in self.res.uses:
            yield name


class _MessageSpec(object):

    def __init__(self, spec):
        self.fields = [_MessageField(field) for field in spec.fields]
        self.fields = {field.name: field for field in self.fields}

    def access(self, path):
        parts = path.split(".")
        field = self.fields[parts[0]]
        for part in parts[1:]:
            field = field.type.ref.spec.fields[part]
        return field

    def link(self, types):
        for field in self.fields.values():
            field.type.ref = types.get(field.type.name)

    @property
    def uses(self):
        for field in self.fields.values():
            if not field.type.is_primitive:
                yield field.type.name


class _MessageField(object):

    def __init__(self, field):
        self.name = field.name
        self.type = _MessageTypeDummy(field.type.pkg_name, field.type.type)
        self.list = self.__list(field.type) if field.type.is_array else ""

    @property
    def text(self):
        return self.type.name + self.list

    @staticmethod
    def __list(type):
        sign = "<=" if type.is_upper_bound else ""
        size = "" if type.array_size is None else type.array_size
        return f"[{sign}{size}]"


class _MessageTypeDummy(object):

    def __init__(self, pkg, msg):
        self.pkg = pkg
        self.msg = msg
        self.ref = None

    @property
    def name(self):
        return f"{self.pkg}/msg/{self.msg}" if self.pkg else self.msg

    @property
    def is_primitive(self):
        return self.pkg is None
