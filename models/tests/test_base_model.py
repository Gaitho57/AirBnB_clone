import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_instance_creation(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIsNone(self.model.id)

    def test_attribute_setting(self):
        self.model.name = "My First Model"
        self.model.my_number = 89
        self.assertEqual(self.model.name, "My First Model")
        self.assertEqual(self.model.my_number, 89)

    def test_save_and_update(self):
        initial_updated_at = self.model.updated_at
        self.model.save_and_update()
        self.assertNotEqual(self.model.updated_at, initial_updated_at)

    def test_to_dict(self):
        self.model.name = "My Model"
        self.model.my_number = 42
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['name'], "My Model")
        self.assertEqual(model_dict['my_number'], 42)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
