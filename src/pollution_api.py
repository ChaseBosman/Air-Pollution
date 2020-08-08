import requests
import json


class PollutionApi:
    def __init__(self):
        self.payload = {'token': '25d51f72382f62cd4ead322c899c8e28fc445361'}
        self.json_data = ""
        self.get_api_ip_based()

    def get_api_ip_based(self):
        self.current_location = requests.get("https://api.waqi.info/feed/here/?", params=self.payload)
        self.json_data = self.current_location.json()

    def get_location(self):
        if self.json_data['data']['city'].get('name'):
            return self.json_data['data']['city'].get('name')
        else:
            return "No City Available"

    def get_co(self):
        if self.json_data['data']['iaqi'].get('co'):
            return self.json_data['data']['iaqi']['co'].get('v')
        else:
            return "No Data Available"

    def get_h(self):
        if self.json_data['data']['iaqi'].get('h'):
            return self.json_data['data']['iaqi']['h'].get('v')
        else:
            return "No Data Available"

    def get_no2(self):
        if self.json_data['data']['iaqi'].get('n02'):
            return self.json_data['data']['iaqi']['no2'].get('v')
        else:
            return "No Data Available"

    def get_o3(self):
        if self.json_data['data']['iaqi'].get('o3'):
            return self.json_data['data']['iaqi']['o3'].get('v')
        else:
            return "No Data Available"

    def get_p(self):
        if self.json_data['data']['iaqi'].get('p'):
            return self.json_data['data']['iaqi']['p'].get('v')
        else:
            return "No Data Available"

    def get_pm10(self):
        if self.json_data['data']['iaqi'].get('pm10'):
            return self.json_data['data']['iaqi']['pm10'].get('v')
        else:
            return "No Data Available"

    def get_pm25(self):
        if self.json_data['data']['iaqi'].get('pm25'):
            return self.json_data['data']['iaqi']['pm25'].get('v')
        else:
            return "No Data Available"

    def get_so2(self):
        if self.json_data['data']['iaqi'].get('so2'):
            return self.json_data['data']['iaqi']['so2'].get('v')
        else:
            return "No Data Available"

    def get_t(self):
        if self.json_data['data']['iaqi'].get('t'):
            return self.json_data['data']['iaqi']['t'].get('v')
        else:
            return "No Data Available"

    def get_w(self):
        if self.json_data['data']['iaqi'].get('w'):
            return self.json_data['data']['iaqi']['w'].get('v')
        else:
            return "No Data Available"




if __name__ == "__main__":
    getter = PollutionApi()
    getter.get_api_ip_based()
    print(getter.current_location.text)
    print(getter.json_data['data']['city'].get('name'))
    getter.read_json_data()
    k = input("press close to exit")
