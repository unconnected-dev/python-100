import pandas

weather_data = {
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10'],
    'temperature': [15, 17, 14, 16, 18, 20, 22, 19, 17, 15],
    'humidity': [50, 48, 52, 55, 53, 49, 47, 51, 53, 50],
    'wind_speed': [10, 12, 8, 9, 11, 14, 13, 10, 9, 12]
}
weather_dataframe = pandas.DataFrame(weather_data)



#Calculate the daily change in temperature
if False:
    weather_dataframe['temp_change'] = weather_dataframe['temperature'].diff()
    print(f"{weather_dataframe[['date','temperature','temp_change']]}")

#Find the days with the largest increase in humidity
if False:
    weather_dataframe['humidity_change'] = weather_dataframe['humidity'].diff()
    print(f"{weather_dataframe.loc[weather_dataframe['humidity_change'].idxmax()]}")

#Calculate the average wind speed change over 3 day periods
if False:
    weather_dataframe['avg_wind_change'] = weather_dataframe['wind_speed'].diff().rolling(window=3).mean()
    print(f"{weather_dataframe[['date','wind_speed','avg_wind_change']]}")

#Find the days where temperature increased by more than 2 degree celsius
if False:
    temp_increase = weather_dataframe[weather_dataframe['temperature'].diff() > 2]
    print(f"{weather_dataframe}")

#Calculate the cumulative change in humidity from the start date to each day
if False:
    weather_dataframe['change'] = weather_dataframe['temperature'].diff().cumsum()
    print(f"{weather_dataframe}")

#Calculate the 5 day moving average of temperature
if False:
    weather_dataframe['avg_temp_change'] = weather_dataframe['temperature'].diff().rolling(window=5).mean()
    print(f"{weather_dataframe}")

#Find the days with the highest 3 day average wind speed
if False:
    weather_dataframe['3_day_avg'] = weather_dataframe['wind_speed'].diff().rolling(window=3).mean()
    highest_ = weather_dataframe.loc[weather_dataframe['3_day_avg'].idxmax()]
    print(f"{highest_}")

#Calculate the absolute change in humidity from the previous day
if False:
    weather_dataframe['abs_change'] = weather_dataframe['temperature'].diff().abs()
    print(f"{weather_dataframe}")

#Find the days with a decrease in wind speed compared to the previous day
if False:
    weather_dataframe['wind_speed_change'] = weather_dataframe['wind_speed'].diff()
    print(f"{weather_dataframe.loc[weather_dataframe['wind_speed_change'] < 0]}")

if False:
    decrease_ = weather_dataframe[weather_dataframe['wind_speed'].diff() < 0]
    print(f"{decrease_}")

#Calculate the percentage change in temperature from the previous day
if False:
    weather_dataframe['temp_change_perc'] = (weather_dataframe['temperature'].diff() / weather_dataframe['temperature'].shift(1)) * 100
    weather_dataframe['difference'] = weather_dataframe['temperature'].diff()
    weather_dataframe['yesterday'] = weather_dataframe['temperature'].shift(1)
    print(f"{weather_dataframe[['date','temperature','yesterday', 'difference','temp_change_perc']]}")

#Calculate the absolute change in wind speed from the previous day
if False:
    weather_dataframe['abs_wind_change'] = weather_dataframe['wind_speed'].diff().abs()
    print(f"{weather_dataframe[['date','wind_speed','abs_wind_change']]}")

#Find the days with an increase in humidity of more than 5% compared to the previous day
if False:
    weather_dataframe['humidity_perc_change'] = (weather_dataframe['humidity'].diff() / weather_dataframe['humidity'].shift(1)) * 100
    weather_dataframe['difference'] = weather_dataframe['humidity'].diff()
    weather_dataframe['yesterday'] = weather_dataframe['humidity'].shift(1)
    print(f"{weather_dataframe[['date','humidity','yesterday','difference','humidity_perc_change']]}")