#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from notification_manager import NotificationManager

my_data_manager = DataManager()
sheet_data = my_data_manager.get_data()

flight_search = FlightSearch()

notification_manager = NotificationManager()

ORIGIN_CITY_IATA="MAN"

#Update iataCode in sheet data by using city name
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])

    my_data_manager.data = sheet_data
    my_data_manager.update_codes()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=180)


for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_now
    )

    if flight != None and flight.price < destination["lowestPrice"]:
        message_=f"Low price alert.  From: {flight.origin_city}, To: {flight.destination_city}, Price: £{flight.price}, From: {flight.out_date}, To: {flight.return_date}"
        # notification_manager.send_sms(
        #     message=message_
        # )
        print(f"{message_}")