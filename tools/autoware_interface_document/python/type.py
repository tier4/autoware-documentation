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
import yaml
from pathlib import Path

from .util import camel_to_snake


builtins = {"bool", "byte", "char", "float32", "float64", "string", "wstring"}
for byte in (8, 16, 32, 64):
    builtins.add(F"int{byte}")
    builtins.add(F"uint{byte}")


class InterfaceType:

    def __init__(self, path: Path):
        self._path = path
        self._text = path.read_text().strip()
        self._used = set()
        self._uses = set()

    @staticmethod
    def __uses(text):
        regex = re.compile("(\w+)/(\w+)")
        types = (regex.match(line) for line in text.split("\n"))
        types = (match for match in types if match is not None)
        return {match.group(1) + "/msg/" + match.group(2) for match in types}

    @property
    def name(self):
        return "/".join(self._path.with_suffix("").parts[-3:])

    # TODO: MarkdownLink
    @property
    def link(self):
        parts = self.name.split("/")
        return "/".join([*parts[:-1], camel_to_snake(parts[-1])]) + ".md"

    def link_relations(self, types):
        for name in self.__uses(self._text):
            if name in types:
                type = types[name]
                self._uses.add(type)
                type._used.add(self)

    def sort_relations(self):
        self._uses = list(sorted(self._uses, key=lambda t: t.name))
        self._used = list(sorted(self._used, key=lambda t: t.name))

    def write(self, path):
        path = path / self.link
        path.parent.mkdir(parents=True, exist_ok=True)
        text = F"# {self.name}\n\n## Definition\n\n```txt\n{self._text}\n```\n"
        if self._uses:
            text += "\n## The types that this uses\n\n"
            for type in self._uses:
                text += F"- [{type.name}](../../{type.link})\n"
        if self._used:
            text += "\n## The types that use this\n\n"
            for type in self._used:
                text += F"- [{type.name}](../../{type.link})\n"
        path.write_text(text)

    @staticmethod
    def WriteIndex(path, types):
        path = path / "index.md"
        with path.open("w") as fp:
            fp.write("# Types of Autoware AD API\n\n")
            for type in types:
                fp.write(F"- [{type.name}]({type.link})\n")


class InterfaceName:

    def __init__(self, path, name):
        self._path = path
        self._name = name
        self._page = None

    def init(self):
        self._page = MarkdownPage(self._path, self.name)
        return self

    @property
    def name(self):
        return "/" + str(self._name)

    # TODO: MarkdownLink
    @property
    def link(self):
        return self._name.with_suffix(".md")

    def rewrite(self):
        self._path.write_text(self._page.markdown())

    @staticmethod
    def WriteIndex(path, apis):
        path = path / "index.md"
        with path.open("w") as fp:
            fp.write("# List of Autoware AD API\n\n")
            for api in apis:
                fp.write(F"- [{api.name}]({api.link})\n")


class MarkdownPage:

    def __init__(self, path, name):
        lines = path.read_text().split("\n")
        for index, line in enumerate(lines):
            if line.startswith("# "):
                break
        self._name = name
        self._meta = MarkdownMeta(lines[:index])
        self._body = MarkdownBody(lines[index:])

    def markdown(self):
        return self._meta.markdown() + self._body.markdown()


class MarkdownMeta:

    def __init__(self, lines):
        self._data = yaml.safe_load("\n".join(line for line in lines if line != "---"))

    def markdown(self):
        return f"---\n{yaml.safe_dump(self._data)}---\n\n" if self._data else ""

class MarkdownBody:

    def __init__(self, lines):
        self._lines = lines

    def markdown(self):
        return "\n".join(self._lines)
