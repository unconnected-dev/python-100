import csv
import pandas

relative_path_name = "./025_csvFiles/weather_data.csv"

with open(relative_path_name) as weather_data_file:
    if False:
        weather_data_contents = weather_data_file.readlines()
        print(weather_data_contents)

    if False:
        weather_data_contents = csv.reader(weather_data_file)
        for row in weather_data_contents:
            if row[1] != "temp":
                print(f"Day: {row[0]} - Temp: {row[1]} - Condition: {row[2]}")
    
    weather_data = pandas.read_csv(weather_data_file)
    print(weather_data["temp"])