import requests
from twilio.rest import Client
import os

if True:
    # API_ = "https://api.openweathermap.org/data/2.5/weather"
    API_ = "https://api.openweathermap.org/data/2.5/forecast"
    API_KEY = os.environ.get("OWM_API_KEY")

    parameters = {
        # "q": "London,uk",
        "lat": 53.5240,
        "lon": 2.4923,
        "appid": API_KEY,
        "cnt": 4
    }
    
    response = requests.get(url=API_, params=parameters) # type: ignore
    # print(response.status_code)
    response.raise_for_status()
    response_data = response.json()
    # print(response_data["list"][0])

    # condition_list = []
    will_rain = False
    for interval in response_data["list"]:
        # print(interval["weather"][0]["id"])
        # condition_list.append(interval["weather"][0]["id"])
        
        condition_code = interval["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
            break
    
    if will_rain == True:
        # print("It will rain")

        #Twilio SMS
        account_sid = ''
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='',
        body="It's going to rain today, bring an umbrella",
        to=''
        )

        # print(message.sid)
        print(message.status)