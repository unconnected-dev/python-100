import requests

if True:
    # API_ = "https://api.openweathermap.org/data/2.5/weather"
    API_ = "https://api.openweathermap.org/data/2.5/forecast"
    API_KEY = ""

    parameters = {
        # "q": "London,uk",
        "lat": 53.5240,
        "lon": 2.4923,
        "appid": API_KEY
    }
    
    response = requests.get(url=API_, params=parameters)
    # print(response.status_code)
    response.raise_for_status()
    response_data = response.json()
    print(response_data)