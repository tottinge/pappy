import unittest
from pappy import *  # So it's "just like" users see it


class IntegrationTest(unittest.TestCase):
    baseURL = 'https://jsonplaceholder.typicode.com/posts/'
    def test_can_get(self):
        result = get(self.baseURL)
        assert result.ok, "The url should be present and reachable"
    def test_result_as_box(self):
        x = get(self.baseURL)
        cool = body_for(x)
