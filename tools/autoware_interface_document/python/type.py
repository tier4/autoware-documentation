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
            fp.write("# Type\n\n")
            for type in types:
                fp.write(F"- [{type.name}]({type.link})\n")


class InterfaceName:

    def __init__(self, path):
        self._path: Path = path
        self._page = None

    def init(self):
        self._page = MarkdownPage(self._path, self.name)
        return self

    @property
    def name(self):
        return "/api/" + self._path.stem.replace("-", "/")

    # TODO: MarkdownLink
    @property
    def link(self):
        return self._path.stem + ".md"

    def rewrite(self):
        self._path.write_text(self._page.markdown())

    @staticmethod
    def WriteIndex(path, apis):
        path = path / "index.md"
        with path.open("w") as fp:
            fp.write("# List\n\n")
            for api in apis:
                fp.write(F"- [{api.name}]({api.link})\n")


class MarkdownPage:

    def __init__(self, path, name):
        self._header = MarkdownHeader(name)
        self._others = MarkdownOthers()
        lines = path.read_text().split("\n")
        lines = self._header.parse(lines)
        lines = self._others.parse(lines)

    @property
    def _contents(self):
        yield self._header
        yield self._others

    def markdown(self):
        return "\n".join(content.markdown() for content in self._contents)


class MarkdownHeader:

    def __init__(self, name):
        self._name = name
        self._method = None
        self._type = None

    def markdown(self):
        return "\n".join([
            F"# {self._name}\n",
            F"- Method: {self._method}",
            F"- Type: {self._type}\n",
        ])

    def parse(self, lines):
        for index, line in enumerate(lines):
            if line.startswith("##"):
                return lines[index:]
            if line.startswith("- Method:"):
                self._method = line.split(":")[1].strip()
            if line.startswith("- Type:"):
                self._type = line.split(":")[1].strip()
                self._type = MarkdownLink.LoadType(self._type)
        return lines


class MarkdownOthers:

    def __init__(self):
        self._lines = None

    def markdown(self):
        return "\n".join(self._lines)

    def parse(self, lines):
        self._lines = lines
        return []


class MarkdownLink:

    def __init__(self, text, link):
        self.text = text
        self.link = link

    def __str__(self):
        if self.link is None:  # TODO: remove
            return self.text
        return F"[{self.text}]({self.link})"

    @staticmethod
    def Load(text):
        match = re.match(R"\[(.+)\]\((.+)\)", text)
        link = None
        if match:
            text = match.group(1)
            link = match.group(2)
        return MarkdownLink(text, link)

    # TODO: remove
    @staticmethod
    def LoadType(text):
        link = MarkdownLink.Load(text)
        part = link.text.split("/")
        link.link = "../type/" + "/".join([*part[:-1], camel_to_snake(part[-1])]) + ".md"
        return link
