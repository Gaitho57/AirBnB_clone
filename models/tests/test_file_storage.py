#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.id = "test_id"
        self.model.name = "Test Model"
        self.model.my_number = 42
        self.storage.new(self.model)
        self.storage.save()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method(self):
        all_objs = self.storage.all()
        self.assertTrue(isinstance(all_objs, dict))
        self.assertIn("BaseModel.test_id", all_objs)

    def test_new_method(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn("BaseModel." + new_model.id, self.storage.all())

    def test_save_method(self):
        with open(FileStorage._FileStorage__file_path, "r") as f:
            saved_data = json.load(f)
        self.assertTrue("BaseModel.test_id" in saved_data)
        self.assertEqual(saved_data["BaseModel.test_id"]["name"], "Test Model")

    def test_reload_method(self):
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.test_id", all_objs)
        self.assertEqual(all_objs["BaseModel.test_id"].name, "Test Model")

if __name__ == '__main__':
    unittest.main()
