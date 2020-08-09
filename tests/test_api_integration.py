import unittest
import pollution_api


class TestApiIntegration(unittest.TestCase):

    def test_status(self):
        """Test if the api is up and running aka status"""
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()
        self.assertEqual("ok", api_response.json_data['status'])

    def test_location(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['city'].get('name'):
            self.assertEqual(api_response.get_location(), api_response.json_data['data']['city'].get('name'))
        else:
            self.assertEqual(api_response.get_location(), "No City Available")

    def test_co(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('co'):
            self.assertEqual(api_response.get_co(), api_response.json_data['data']['iaqi']['co'].get('v'))
        else:
            self.assertEqual(api_response.get_co(), "No Data Available")

    def test_h(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('h'):
            self.assertEqual(api_response.get_h(), api_response.json_data['data']['iaqi']['h'].get('v'))
        else:
            self.assertEqual(api_response.get_h(), "No Data Available")

    def test_no2(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('no2'):
            self.assertEqual(api_response.get_no2(), api_response.json_data['data']['iaqi']['no2'].get('v'))
        else:
            self.assertEqual(api_response.get_no2(), "No Data Available")

    def test_o3(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('o3'):
            self.assertEqual(api_response.get_o3(), api_response.json_data['data']['iaqi']['o3'].get('v'))
        else:
            self.assertEqual(api_response.get_o3(), "No Data Available")

    def test_p(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('p'):
            self.assertEqual(api_response.get_p(), api_response.json_data['data']['iaqi']['p'].get('v'))
        else:
            self.assertEqual(api_response.get_p(), "No Data Available")

    def test_pm10(self):

        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('pm10'):
            self.assertEqual(api_response.get_pm10(), api_response.json_data['data']['iaqi']['pm10'].get('v'))
        else:
            self.assertEqual(api_response.get_pm10(), "No Data Available")

    def test_pm25(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('pm25'):
            self.assertEqual(api_response.get_pm25(), api_response.json_data['data']['iaqi']['pm25'].get('v'))
        else:
            self.assertEqual(api_response.get_pm25(), "No Data Available")

    def test_so2(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('so2'):
            self.assertEqual(api_response.get_so2(), api_response.json_data['data']['iaqi']['so2'].get('v'))
        else:
            self.assertEqual(api_response.get_so2(), "No Data Available")

    def test_t(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('t'):
            self.assertEqual(api_response.get_t(), api_response.json_data['data']['iaqi']['t'].get('v'))
        else:
            self.assertEqual(api_response.get_t(), "No Data Available")

    def test_w(self):
        api_response = pollution_api.PollutionApi()
        api_response.get_api_ip_based()

        if api_response.json_data['data']['iaqi'].get('w'):
            self.assertEqual(api_response.get_w(), api_response.json_data['data']['iaqi']['w'].get('v'))
        else:
            self.assertEqual(api_response.get_w(), "No Data Available")


if __name__ == '__main__':
    unittest.main()
