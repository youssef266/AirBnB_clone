#!/usr/bin/python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        
    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.review, BaseModel)

if __name__ == "__main__":
    unittest.main()