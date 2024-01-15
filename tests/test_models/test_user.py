#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    setUp method is a special method in unittest.TestCase that is called before each test method is executed
    """
    def setUp(self):
        self.user = User()
        
    """
        creating an instance of BaseModel:
    """
    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        
    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.user, BaseModel)
        
if __name__ == '__main__':
    unittest.main()