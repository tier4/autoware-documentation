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

from asyncio import protocols
from pathlib import Path


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

    def rewrite(self):
        self._path.write_text(self._page.markdown())


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

    pass
