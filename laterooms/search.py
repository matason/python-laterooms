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

import sys
import requests

class SearchFactory:
    def create(type, api_key, base_url):
        handler = {
            "text": "SearchText",
            "keyword": "SearchKeyword",
            "area": "SearchArea",
            "location": "SearchLocation",
            "map": "SearchMap",
            "polygon": "SearchPolygon",
            }.get(type, None)

        if None == handler:
            raise ValueError('Unsupported search type requested.')

        class_name = getattr(sys.modules[__name__], handler)
        return class_name(api_key, base_url)

class SearchBase:
    _api_key = ""
    _base_path = "search"
    _url = None

    def __init__(self, api_key, base_url, path):
        self._api_key = api_key
        url = [base_url]
        url.append(self._base_path)
        url.append(path)
        self._url = str.join("/", url)

    def Execute(self):
        try:
            headers = {"API-Key": self._api_key}
            response = requests.get(self._url, headers=headers)
        except requests.RequestException as e:
            raise Exception(str(e))

        return response

class SearchText(SearchBase):
    def __init__(self, api_key, base_url):
        super().__init__(api_key, base_url, "")

class SearchKeyword(SearchBase):
    def __init__(self, api_key, base_url):
        super().__init__(api_key, base_url, "")

class SearchArea(SearchBase):
    def __init__(self, api_key, base_url):
        super().__init__(api_key, base_url, "")

class SearchLocation(SearchBase):
    def __init__(self, api_key, base_url):
        super().__init__(api_key, base_url, "location")

    def SetParameters(self, parameters):
        url_parts = []
        mandatory_parts = []

        # Process mandatory paramaters.
        mandatory_parts.append(parameters["lat"])
        mandatory_parts.append(parameters["long"])
        url_parts.append(str.join(",", mandatory_parts))

        # Process optional parameters.
        if "radius" in parameters.keys():
            url_parts.append(parameters["radius"])

        self._url += "/" + str.join("/", url_parts)

        # A trailing slash is required by the API.
        self._url += "/"

class SearchMap(SearchBase):
    def __init__(self, api_key, base_url):
        super().__init__(api_key, base_url, "")

class SearchPolygon(SearchBase):
    def __init__(self, api_key, base_url):
        super().__init__(api_key, base_url, "")
