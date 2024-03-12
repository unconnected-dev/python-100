from datetime import datetime 
import requests


#https://developer.nutritionix.com/
NUTITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITION_APP_ID = ""
NUTRITION_API_KEY = ""


nutrition_headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY
}

nutrition_exercise_text = "I ran for 46 minutes"

nutrition_parameters = {
    "query": nutrition_exercise_text,
    # "gender": GENDER,
    # "weight_kg": WEIGHT,
    # "height_cm": HEIGHT_CM,
    # "age": AGE
}

nutrition_response = requests.post(NUTITION_ENDPOINT, json=nutrition_parameters, headers=nutrition_headers)
nutrition_result = nutrition_response.json()


#https://sheety.co/
SHEETY_ENDPOINT = ""

sheety_headers = {
    "Authorization": ""
}

current_date = datetime.now().strftime("%d/%m/%y")
current_time = datetime.now().strftime("%H:%M:%S")

for exercise in nutrition_result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)

    print(sheet_response.text)