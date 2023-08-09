#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """testing file storage"""

    def test_file_path_attribute(self):
        """file_path attribute test to pass correctly"""
        file_storage = FileStorage()
        file_path = file_storage._FileStorage__file_path
        self.assertIsNotNone(file_path)

    def test_objects_attribute(self):
        """__object attribute test to pass correctly"""
        file_storage = FileStorage()
        file_object = file_storage._FileStorage__objects
        text = "__file_object is not dictionary"
        self.assertIsInstance(file_object, dict, text)

    def test_all(self):
        """check if returns dic<class>.<id> : {obj instance}"""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsNotNone(all_objs)
        self.assertEqual(dict, type(all_objs))
        self.assertIs(all_objs, storage._FileStorage__objects)

    def test_new(self):
        file_storage = FileStorage()
        base_model = BaseModel()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)

        file_storage.new(base_model)
        self.assertIn(key, file_storage.all())

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        base_model = BaseModel()
        file_storage = FileStorage()
        file_storage.new(base_model)
        file_storage.reload()
        self.assertEqual(len(file_storage.all()), 2)


if __name__ == "__main__":
    unittest.main()
