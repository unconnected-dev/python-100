#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

my_data_manager = DataManager()
sheet_data = my_data_manager.get_data()

flight_search = FlightSearch()


#Update iataCode in sheet data by using city name
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])

    my_data_manager.data = sheet_data
    my_data_manager.update_codes()