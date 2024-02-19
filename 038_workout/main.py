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

nutrition_response = requests.post(NUTITION_ENDPOINT, json=nutrition_parameters, headers=headers)
nutrition_result = nutrition_response.json()

