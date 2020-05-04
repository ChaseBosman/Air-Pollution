import requests
import json
import PyQt5


class PollutionApi:
    def __init__(self):
        self.payload = {'token': '25d51f72382f62cd4ead322c899c8e28fc445361'}
        self.msg = "hi"

    def get_api_ip_based(self):
        self.current_location = requests.get("https://api.waqi.info/feed/here/?", params=self.payload)
        self.location_dict = json.loads(self.current_location.text)
        self.json_data = self.current_location.json()

    def get_location(self):
        if self.json_data['data']['city'].get('name'):
            print("City:", self.json_data['data']['city'].get('name'))
        else:
            print("No City Available")

    def read_json_data(self):
        if self.json_data['data']['iaqi'].get('co'):
            print("co,", self.json_data['data']['iaqi']['co'].get('v'))
        else:
            print("co, no data")

        if self.json_data['data']['iaqi'].get('h'):
            print("h,", self.json_data['data']['iaqi']['h'].get('v'))
        else:
            print("h, no data")

        if self.json_data['data']['iaqi'].get('n02'):
            print("no2,", self.json_data['data']['iaqi']['no2'].get('v'))
        else:
            print("no2, no data")

        if self.json_data['data']['iaqi'].get('o3'):
            print("o3,", self.json_data['data']['iaqi']['o3'].get('v'))
        else:
            print("o3, no data")

        if self.json_data['data']['iaqi'].get('p'):
            print("p,", self.json_data['data']['iaqi']['p'].get('v'))
        else:
            print("p, no data")

        if self.json_data['data']['iaqi'].get('pm10'):
            print("pm 10,", self.json_data['data']['iaqi']['pm10'].get('v'))
        else:
            print("pm 10, no data")

        if self.json_data['data']['iaqi'].get('pm25'):
            print("pm 2.5,", self.json_data['data']['iaqi']['pm25'].get('v'))
        else:
            print("pm 2.5, no data")

        if self.json_data['data']['iaqi'].get('so2'):
            print("so2,", self.json_data['data']['iaqi']['so2'].get('v'))
        else:
            print("so2, no data")

        if self.json_data['data']['iaqi'].get('t'):
            print("t,", self.json_data['data']['iaqi']['t'].get('v'))
        else:
            print("t, no data")

        if self.json_data['data']['iaqi'].get('w'):
            print("wind,", self.json_data['data']['iaqi']['w'].get('v'))
        else:
            print("wind, no data")




if __name__ == "__main__":
    getter = PollutionApi()
    getter.get_api_ip_based()
    print(getter.current_location.text)
    getter.read_json_data()
    k = input("press close to exit")
