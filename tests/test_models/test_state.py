#!/usr/bin/python3
"""Unittests for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the instantiation of the class State"""
    def test_instantiation(self):
        state = State()
        """test if State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel), True)
        """test if state is of class State"""
        self.assertIsInstance(state, State)

    def test_initialization(self):
        """tests if attributes are correct types"""
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
