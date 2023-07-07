import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def test_inheritance(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_to_dict(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], place.id)
        self.assertEqual(place_dict['created_at'], place.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(place_dict['updated_at'], place.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

if __name__ == '__main__':
    unittest.main()
