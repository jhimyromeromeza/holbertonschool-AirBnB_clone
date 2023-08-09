#!/usr/bin/python3
import os
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep
""" Unit tests for BaseModel and each of their methods"""


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel"""

    def setUp(self):
        self.obj = BaseModel()

    def test_instantiate(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uuid(self):
        """
        checks if each instance of BaseModel has a unique id (UUID)
        created at each instantiation.
        """
        base_m1 = BaseModel()
        base_m2 = BaseModel()
        self.assertNotEqual(base_m1.id, base_m2.id)

    def test_str(self):
        """
        the __str__ method of the BaseModel class returns
        a string when called on an instance of the class
        """
        bm = BaseModel()
        self.assertEqual(type(str(bm)), str)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_save(self):
        """
        this test method ensures that the save method
        of the BaseModel class correctly updates
        """
        bm = BaseModel()
        sleep(2)
        update = bm.updated_at
        bm.save()
        self.assertNotEqual(update, bm.updated_at)
    
    def test_to_dict(self):
        obj_dict = self.obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertNotEqual(obj_dict, self.obj.__dict__)

if __name__ == "__main__":
    unittest.main()
