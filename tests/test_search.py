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

class LateRoomsSearchTestCase(unittest.TestCase):
    def test_search_unsupported_search_type(self):
        api = laterooms.API("JufM0RVUtJT9ZU8HDAmOg4mGThA78qPn")
        self.assertRaises(ValueError, api.Search, "unsupported", {})

    def test_search_url_with_radius(self):
        api = laterooms.API("JufM0RVUtJT9ZU8HDAmOg4mGThA78qPn")
        parameters = {"lat": "28.053672", "long": "-82.404526", "radius": "10"}
        search = api.Search("location", parameters)
        self.assertEqual(search._url, "https://sandbox.api.tlrg.io/v1/mobile/search/location/28.053672,-82.404526/10/")

    def test_search_url_without_radius(self):
        api = laterooms.API("JufM0RVUtJT9ZU8HDAmOg4mGThA78qPn")
        parameters = {"lat": "28.053672", "long": "-82.404526"}
        search = api.Search("location", parameters)
        self.assertEqual(search._url, "https://sandbox.api.tlrg.io/v1/mobile/search/location/28.053672,-82.404526/")

    def test_search_url_missing_mandatory_parameter(self):
        api = laterooms.API("JufM0RVUtJT9ZU8HDAmOg4mGThA78qPn")
        parameters = {"lat": "28.053672"}
        self.assertRaises(KeyError, api.Search, "location", parameters)

    def test_search_response_status_code(self):
        api = laterooms.API("JufM0RVUtJT9ZU8HDAmOg4mGThA78qPn")
        parameters = {"lat": "28.053672", "long": "-82.404526"}
        search = api.Search("location", parameters)
        response = search.Execute()
        self.assertEqual(200, response.status_code)

    # Radius search currently broken at the API, returns a 404.
    #def test_search_response_status_code_with_radius(self):
        #api = laterooms.API("JufM0RVUtJT9ZU8HDAmOg4mGThA78qPn")
        #parameters = {"lat": "28.053672", "long": "-82.404526", "radius": "10"}
        #search = api.Search("location", parameters)
        #response = search.Execute()
        #self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
