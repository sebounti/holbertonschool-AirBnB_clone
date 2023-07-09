import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def test_inheritance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_to_dict(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['created_at'], review.created_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(review_dict['updated_at'], review.updated_at.\
                         strftime("%Y-%m-%dT%H:%M:%S.%f"))

if __name__ == '__main__':
    unittest.main()
