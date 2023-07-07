import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertEqual(model.first_name, "")

    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(model.id, model_str)

    def test_save(self):
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(prev_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model_dict['updated_at'], model.updated_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))

if __name__ == '__main__':
    unittest.main()
