#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.state import State
"""unit test to test for state class"""


class TestState(unittest.TestCase):
    """testing instantation of the State"""

    def test_is_subclass(self):
        self.assertTrue(issubclass(State().__class__, BaseModel), True)

    def test_attr_str(self):
        self.assertEqual(type(State().name), str)

    def test_has_attributes(self):
        Angeles = State()
        Angeles.name = "Angeles"
        self.assertTrue('id' in Angeles.to_dict())
        self.assertTrue('created_at' in Angeles.to_dict())
        self.assertTrue('updated_at' in Angeles.to_dict())
        self.assertTrue('name' in Angeles.to_dict())

    def test_save(self):
        Angeles = State()
        Angeles.name = "Angeles"
        Angeles.save()
        self.assertNotEqual(Angeles.created_at, Angeles.updated_at)

    def test_to_dict(self):
        Angeles = State()
        self.assertTrue(dict, type(Angeles.to_dict))
        self.assertEqual('to_dict' in dir(Angeles), True)


if __name__ == "__main__":
    unittest.main()
