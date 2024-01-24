import time
import requests
from datetime import datetime
import smtplib

# MY_EMAIL = "****@****.***"
# MY_PASSWORD = "******"

MY_LAT = 51.507351
MY_LONG = -0.127758


def checkISSInView() -> bool:
    global within_view
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (iss_latitude >= MY_LAT - 5 and iss_latitude <= MY_LAT + 5) and (iss_longitude >= MY_LONG - 5 and iss_longitude <= MY_LONG + 5):
        within_view = True
    else:
        within_view = False

    return within_view


def checkSunriseSunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True
    else:
        return False


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if checkSunriseSunset() and checkSunriseSunset():
        print("You can see the ISS")

        # connection = smtplib.SMTP("smtp.gmail.com")
        # connection.starttls()
        # connection.login(MY_EMAIL, MY_PASSWORD)
        # connection.sendmail(
        #     from_addr=MY_EMAIL,
        #     to_addrs=MY_EMAIL,
        #     msg="Subject:Look up\n\nThe ISS is above you"   
        # )



