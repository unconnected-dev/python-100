import requests
import os
from dotenv import load_dotenv
load_dotenv("./python100.env")
from flight_data import FlightData


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
    KIWI_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
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
    

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        
        kiwi_headers = {
            "apikey": FlightSearch.KIWI_API_KEY,
        }

        kiwi_parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        #https://tequila.kiwi.com
        kiwi_response = requests.get(url=f"{FlightSearch.KIWI_SEARCH_ENDPOINT}", headers=kiwi_headers, params=kiwi_parameters)

        try:
            data = kiwi_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None


        # print(data)

        flight_data = FlightData(
            price=data["price"],
            origin_city = data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data