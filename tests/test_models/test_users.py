import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], user.id)
        self.assertEqual(user_dict['created_at'], user.created_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(user_dict['updated_at'], user.updated_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))


if __name__ == '__main__':
    unittest.main()
