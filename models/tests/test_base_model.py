#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertIsInstance(self.model.id, str)

        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertIsInstance(self.model.created_at, datetime)

        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        self.model.name = "My Model"
        self.model.my_number = 42
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['name'], "My Model")
        self.assertEqual(model_dict['my_number'], 42)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
