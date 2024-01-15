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
    
    # print(weather_data["temp"])
    # print(type(weather_data))
    # print(type(weather_data["temp"]))

    #Convert to dict
    # weather_data_dict = weather_data.to_dict()
    # print(weather_data_dict)

    #Convert series to list
    # temp_list = weather_data["temp"].to_list()
    # print(temp_list)
    
    # avg_temp = sum(temp_list) / len(temp_list)
    # print(avg_temp)

    #In built panda functions
    # print(weather_data["temp"].mean())
    # print(weather_data["temp"].max())

    #You don't need to use brackets
    # print(weather_data.condition)

    #Getting row data
    # print(weather_data[weather_data.day == "Monday"])
    # print(weather_data[weather_data.temp == weather_data.temp.max()])
    # print(weather_data[weather_data.day == "Monday"].temp[0] * 9/5 + 32)

    #Create dataframe
    # data_dict = {
    #     "students": ["amy", "james", "angela"],
    #     "scores": [76,56,65]
    # }

    # data = pandas.DataFrame(data_dict)
    # data.to_csv("./025_csvFiles/new_data.csv")