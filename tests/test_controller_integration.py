import unittest
import sys
import os

def get_abs_dir_for_module(*args):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), *args)
repo_dir = get_abs_dir_for_module("..")
sys.path.append(repo_dir)
import src.user_input as user_input

from user_input import UserInput

class TestControllerIntegration(unittest.TestCase):

    def test_calculate_has_no_stats_start(self):
        self.user_info = UserInput()
        self.assertFalse(self.user_info.stats_set)


if __name__ == '__main__':
    unittest.main()

