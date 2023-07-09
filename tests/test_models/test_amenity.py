import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))

if __name__ == '__main__':
    unittest.main()
