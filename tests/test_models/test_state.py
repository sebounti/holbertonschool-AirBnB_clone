import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], state.id)
        self.assertEqual(state_dict['created_at'], state.created_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(state_dict['updated_at'], state.updated_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))

if __name__ == '__main__':
    unittest.main()
