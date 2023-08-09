#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City
"""unittest to test class City"""


class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the Review class"""

    def test_has_attributes(self):
        city = City()

        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
