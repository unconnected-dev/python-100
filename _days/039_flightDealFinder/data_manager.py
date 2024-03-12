import requests
import os
from dotenv import load_dotenv
load_dotenv("./python100.env")

class DataManager:
    #https://sheety.co/
    SHEETY_ENDPOINT = os.getenv("PYTHON100_039_SHEETY_ENDPOINT")

    sheety_headers = {
        "Authorization": ""
    }

    def __init__(self) -> None:
        self.data = {}


    def get_data(self):
        sheet_response = requests.get(url=DataManager.SHEETY_ENDPOINT)
        sheet_response.raise_for_status()
        data = sheet_response.json()
        #prices is the sheet name
        self.data = data['prices']
        return self.data

    #Update the google docs sheet data
    def update_codes(self):
        for city in self.data:
            data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{DataManager.SHEETY_ENDPOINT}/{city['id']}", json=data)
            response.raise_for_status()
            print(f"{self.__class__.__name__} {self.update_codes.__name__} : {response.text}")