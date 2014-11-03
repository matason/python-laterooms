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

import unittest
import laterooms

class LateRoomsAPITestCase(unittest.TestCase):
    def test_api_default_base_url(self):
        api = laterooms.API()
        self.assertEqual(api._base_url, "https://sandbox.api.tlrg.io/v1/mobile")

    def test_api_overridden_base_url(self):
        url = "http://example.com"
        api = laterooms.API(url)
        self.assertEqual(api._base_url, url)

if __name__ == '__main__':
    unittest.main()