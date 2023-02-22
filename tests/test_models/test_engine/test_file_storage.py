#!/usr/bin/python3
"""Unittest for class FileStorage"""
import unittest
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage
import models

class TestFileStorage(unittest.TestCase):
    """Test the instantiation of the class FileStorage"""

    def test_file_path(self):
        fs = FileStorage()
        self.assertEqual(str, type(fs._FileStorage__file_path))

    def test_objects(self):
        fs = FileStorage()
        self.assertEqual(dict, type(fs._FileStorage__objects))

    def test_class(self):
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())

    def test_save(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_reload(self):
        pass

if __name__ == "__main__":
    unittest.main()
