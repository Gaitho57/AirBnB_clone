#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def test_all(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)

    def test_new(self):
        model = BaseModel()
        storage.new(model)
        self.assertIn(model.id, storage.all())

    def test_save(self):
        model = BaseModel()
        storage.new(model)
        storage.save()
        with open("file.json", "r") as f:
            objects = json.load(f)
            self.assertIn(model.id, objects)


if __name__ == "__main__":
    unittest.main()`
