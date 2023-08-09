#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity

"""Unittest to test Amenity class"""


class TestAmenity(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_update_at(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_save(self):
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict(self):
        amenity = Amenity()
        self.assertTrue(dict, type(amenity.to_dict))
        self.assertEqual('to_dict' in dir(amenity), True)


if __name__ == "__main__":
    unittest.main()
