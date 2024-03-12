import requests
from twilio.rest import Client
import os

#https://www.alphavantage.co/documentation/#daily
STOCK_API_KEY = ""
STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

#https://newsapi.org/ 
NEWS_API_KEY = ""
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

if False:
    stock_parameters = {
            "apikey": STOCK_API_KEY,
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK_NAME
        }


    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters) # type: ignore
    stock_data = stock_response.json()["Time Series (Daily)"]

    #data_0_data is yesterday
    stock_data_list = [value for (key, value) in stock_data.items()]
    day_0_data = stock_data_list[0]
    day_0_close = float(day_0_data['4. close'])

    #data_1_data is the day before yesterday
    day_1_data = stock_data_list[1]
    day_1_close = float(day_1_data['4. close'])

    #calculate % difference
    day_difference = abs(day_0_close - day_1_close)
    day_difference_perc = (day_difference / day_0_close) * 100


# if day_difference_perc >= 5:
if True:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters) # type: ignore
    news_data = news_response.json()
    news_articles = news_data["articles"]
    
    sms_message = ''
    for article in news_articles[:3]:
        # print(article["title"])
        sms_message += article["title"] + ","


if False:
    account_sid = ''
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='',
    body=sms_message[:-1],
    to=''
    )

    print(message.status)