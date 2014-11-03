#!/usr/bin/env python
#
# Copyright 2014 The Python-LateRooms developers.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class SearchFactory:
    def create(type, base_url=None):
        handler = {
            'text': SearchText(base_url),
            'keyword': SearchKeyword(base_url),
            'area': SearchArea(base_url),
            'location': SearchLocation(base_url),
            'map': SearchMap(base_url),
            'polygon': SearchPolygon(base_url)
            }.get(type, None)

        if None == handler:
            raise ValueError('Unsupported search type requested.')

        return handler

class SearchBase:
    _base_path = "search"
    _url = None

    def __init__(self, base_url, path):
        url = [base_url]
        url.append(self._base_path)
        url.append(path)
        self._url = str.join("/", url)

    def HandleRequest(self):
        pass

class SearchText(SearchBase):
    def __init__(self, base_url):
        super().__init__(base_url, "")

class SearchKeyword(SearchBase):
    def __init__(self, base_url):
        super().__init__(base_url, "")

class SearchArea(SearchBase):
    def __init__(self, base_url):
        super().__init__(base_url, "")

class SearchLocation(SearchBase):
    def __init__(self, base_url):
        super().__init__(base_url, "location")

class SearchMap(SearchBase):
    def __init__(self, base_url):
        super().__init__(base_url, "")

class SearchPolygon(SearchBase):
    def __init__(self, base_url):
        super().__init__(base_url, "")