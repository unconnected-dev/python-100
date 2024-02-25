import requests

class DataManager:
    SHEETY_ENDPOINT = ""

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