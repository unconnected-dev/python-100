import requests
from datetime import datetime

#No Parameters for ISS
if False:
    #API Endpoint
    #Returns status code
    #https://www.webfx.com/web-development/glossary/http-status-codes/
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    #Will raise HTTP error if unsuccessful status code
    response.raise_for_status()

    # print(response.status_code)
    # print(response.content)

    response_data = response.json()
    print(response_data)
    print(response_data["iss_position"]["longitude"])
    print(response_data["iss_position"]["latitude"])

if True:

    MY_LAT = 53.523510
    MY_LONG = -2.496480

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    response_data = response.json()

    # time_now = datetime.now()
    # print(time_now)

    sunrise = response_data["results"]["sunrise"].split("T")
    sunset = response_data["results"]["sunset"].split("T")

    sunrise_time_split= sunrise[1].split(":")
    sunset_time_split= sunset[1].split(":")
    
    sunrise_hour = sunrise_time_split[0]
    sunset_hour = sunset_time_split[0]
    print(f"sunrise hour: {sunrise_hour}, sunset hour: {sunset_hour}")

    
