#!/usr/bin/python3
"""Defines the class Review"""
from models.base_model import BaseModel



class Review(BaseModel):
    """represents a Review, inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
