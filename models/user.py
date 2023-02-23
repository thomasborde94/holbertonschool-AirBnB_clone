#!/usr/bin/python3
"""Defines the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """represents a user, inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
