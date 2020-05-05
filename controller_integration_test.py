import unittest
from user_input import UserInput


class TestControllerIntegration(unittest.TestCase):

    def test_calculate_has_no_stats_start(self):
        self.user_info = UserInput()
        self.assertFalse(self.user_info.stats_set)