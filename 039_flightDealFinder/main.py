#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

my_data_manager = DataManager()
sheet_data = my_data_manager.get_data()
print(f"{sheet_data}")