#!/usr/bin/python3
"""Stores the unique Filestorage instance"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
