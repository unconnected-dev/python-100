import requests
import os
from dotenv import load_dotenv
load_dotenv("./python100.env")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
    KIWI_API_KEY = os.getenv("PYTHON100_039_KIWI_API_KEY")

    def get_destination_code(self, city_name):

        kiwi_headers = {
            "apikey": FlightSearch.KIWI_API_KEY,
        }

        kiwi_parameters = {
            "term": city_name,
            "city_types": "city"
        }
        

        #https://tequila.kiwi.com
        kiwi_response = requests.get(url=FlightSearch.KIWI_ENDPOINT, headers=kiwi_headers, params=kiwi_parameters)

        results = kiwi_response.json()['locations']
        code = results[0]["code"]
        return code