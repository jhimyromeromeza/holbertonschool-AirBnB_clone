#!/usr/bin/python3
import os
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep
""" Unit tests for BaseModel and each of their methods"""


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel"""

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

    """
        def test_instantiate_kwargs(self):
    
        This method test the instantiation of the BaseModel class
        using keyword arguments (kwargs)
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)"""

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

    def test_instantiate_arg(self):
        """ invalid arg when instantiating """
        with self.assertRaises(NameError) as e:
            bm = BaseModel(hello)
        self.assertEqual(str(e.exception), "name 'hello' is not defined")

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
        """ Happy pass to_dict method """
        bm = BaseModel()
        self.assertEqual(dict, type(bm.to_dict))

    def test_to_dict_add_attr(self):
        """
        this test method ensures that when additional
        attr are added to an instance o the BaseModel class
        and the to_dict method is called on that instance
        """
        base1 = BaseModel()
        base1.city = "Los"
        base1.state = "Angeles"
        self.assertIn("city", base1.to_dict())
        self.assertIn("state", base1.to_dict())

    def test_to_dict_wrong_arg(self):
        """ add an undefined arg """
        base1 = BaseModel()
        with self.assertRaises(NameError):
            base1.to_dict(hello)


if __name__ == "__main__":
    unittest.main()
