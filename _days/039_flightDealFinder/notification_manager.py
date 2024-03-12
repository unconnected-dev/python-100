import os
from dotenv import load_dotenv
load_dotenv("./python100.env")
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    #https://www.twilio.com/en-us
    TWILIO_ACCOUNT_SID = os.getenv("PYTHON100_039_TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("PYTHON100_039_TWILIO_AUTH_TOKEN")
    TWILIO_VIRTUAL_NUMBER = os.getenv("PYTHON100_039_TWILIO_VIRTUAL_NUMBER")
    TWILIO_VERIFIED_NUMBER = os.getenv("PYTHON100_039_TWILIO_VERIFIED_NUMBER")

    def __init__(self) -> None:
        self.client = Client(NotificationManager.TWILIO_ACCOUNT_SID, NotificationManager.TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        
        message = self.client.messages.create(
            from_=NotificationManager.TWILIO_VIRTUAL_NUMBER,
            body=message,
            to=NotificationManager.TWILIO_VERIFIED_NUMBER
        )

        print(f"{message.status}")