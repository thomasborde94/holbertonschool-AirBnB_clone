#!/usr/bin/python3
"""Unittests for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel
import datetime


class TestUser(unittest.TestCase):
    """Test the instantiation of the class User"""
    def test_instantiation(self):
        user = User()
        """test if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel), True)
        """test if user is of class User"""
        self.assertIsInstance(user, User)

    def test_initialization(self):
        """tests if attributes are correct types"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == '__main__':
    unittest.main()
