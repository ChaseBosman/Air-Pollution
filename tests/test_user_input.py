import unittest
import sys
import os

def get_abs_dir_for_module(*args):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), *args)
repo_dir = get_abs_dir_for_module("..")
sys.path.append(repo_dir)
import src.user_input as user_input

from user_input import UserInput

class TestUserInput(unittest.TestCase):
    def test_get_miles(self):
        self.user_data = user_input.UserInput()
        self.user_data.miles_driven = 400
        self.assertEqual(self.user_data.get_miles_driven(), 400)

    def test_get_hw_hour(self):
        self.user_data = user_input.UserInput()
        self.user_data.kw_hour = 300
        self.assertEqual(self.user_data.get_kw_hour_to_years(), 300 * 12)

    def test_get_therms(self):
        self.user_data = user_input.UserInput()
        self.user_data.therms = 200
        self.assertEqual(self.user_data.get_therms(), 200 * 12)

    def test_get_mcf(self):
        self.user_data = user_input.UserInput()
        self.user_data.mcf = 100
        self.assertEqual(self.user_data.get_mcf(), 100 * 12)

    def test_get_propane(self):
        self.user_data = user_input.UserInput()
        self.user_data.propane = 500
        self.assertEqual(self.user_data.get_propane(), 500)


if __name__ == '__main__':
    unittest.main()