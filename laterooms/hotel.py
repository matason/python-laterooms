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

class Hotel:
    _api_key = ""
    _base_path = "hotel"
    _url = None

    def __init__(self, api_key, base_url):
        self._api_key = api_key
        url = [base_url]
        url.append(self._base_path)
        self._url = str.join("/", url)

    def Execute(self):
        try:
            headers = {"API-Key": self._api_key}
            response = requests.get(self._url, headers=headers)
        except requests.RequestException as e:
            raise Exception(str(e))

        return response
