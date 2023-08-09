#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review
"""unittest to test Review class"""


class TestReview(unittest.TestCase):
    """Unittests for testing instantiation of the Review class"""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_has_attributes_in_to_dict(self):
        """check if attr is in to_dict"""
        review = Review()
        review.place_id = "melb"
        review.user_id = "jacq"
        review.text = "hello"
        self.assertTrue('id' in review.to_dict())
        self.assertTrue('created_at' in review.to_dict())
        self.assertTrue('updated_at' in review.to_dict())
        self.assertTrue('place_id' in review.to_dict())
        self.assertTrue('user_id' in review.to_dict())
        self.assertTrue('text' in review.to_dict())

    def test_save(self):
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict(self):
        review = Review()
        self.assertTrue(dict, type(review.to_dict))
        self.assertEqual('to_dict' in dir(review), True)


if __name__ == "__main__":
    unittest.main()
