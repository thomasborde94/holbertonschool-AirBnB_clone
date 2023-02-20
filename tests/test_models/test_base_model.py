#!/usr/bin/python3
"""Unittest for class BaseModel"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the instantiation of the class BaseModel"""

    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(bm1, "id")
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_created_at(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime.datetime)
        
    def test_updated_at(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime.datetime)

    def test_str(self):
##        bm1 = BaseModel()
##        self.assertEqual(str(bm1), "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
        pass

    def test_save(self):
        bm1 = BaseModel()
        tmp = bm1.updated_at
        bm1.save()
        self.assertNotEqual(tmp, bm1.updated_at)

    def test_to_dict(self):
        bm1 = BaseModel()
        newDic = bm1.to_dict()
        self.assertIsInstance(newDic, dict)
        self.assertTrue("__class__" in newDic)

if __name__ == "__main__":
    unittest.main()
