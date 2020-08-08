import unittest
from pollution_api import PollutionApi


class TestApiIntegration(unittest.TestCase):

    def test_location(self):
        """Note: this test is location specific, individual locations will need to be entered
        for passing when tested in a location outside of reno/tahoe area. Your closest location can be determined
        through aqi.waqi's sample aqi finder"""
        api_response = PollutionApi()
        api_response.get_api_ip_based()
        self.assertEqual("ok",
                         api_response.json_data['status'])

    def test_status(self):
        """Test if the api is up and running aka status"""
        api_response = PollutionApi()
        api_response.get_api_ip_based()
        self.assertEqual("ok", api_response.json_data['status'])

