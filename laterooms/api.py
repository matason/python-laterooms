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

import requests
from laterooms import search
from laterooms import hotel

class API:
    _base_url = None
    _search = {}
    _hotel = None

    def __init__(self, base_url=None):
        if base_url is None:
            self._base_url = 'https://sandbox.api.tlrg.io/v1/mobile'
        else:
            self._base_url = base_url

    def Search(self, type):
        if type not in self._search:
            self._search[type] = search.SearchFactory.create(type, self._base_url)

        self._search[type].HandleRequest()

    def Hotel(self):
        if None == self._hotel:
            self._hotel = hotel.Hotel(self._base_url)

        self._hotel.HandleRequest()