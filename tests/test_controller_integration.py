import unittest
import user_input

class TestControllerIntegration(unittest.TestCase):

    def test_calculate_has_no_stats_start(self):
        self.user_info = user_input.UserInput()
        self.assertFalse(self.user_info.stats_set)


if __name__ == '__main__':
    unittest.main()

