#!/usr/bin/python3
"""Defines the class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """represents a City, inherits from BaseModel"""
    state_id = ""
    name = ""
