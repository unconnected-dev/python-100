#APIs

#An API is a set of rules and protocols that allows different software 
#applications to communicate with each other. It defines the methods and
#data formats that applications can use to request and exchange information


import html
import requests


#Basics
if False:
    API_ENDPOINT = "https://api.kanye.rest/"

    response = requests.get(API_ENDPOINT)

    #This method will check if the HTTP request was successful
    #or if it encountered an error

    #1xx Informational
    #These indicate the server has received the request and is
    #continuing the process. They are informational and not
    #usually encountered in typical client-server interactions

    #2xx Success
    #These indicate the request was recieved, understood and
    #processed successfully
    
    #3xx These indicate that further action needs to be taken
    #by the client to fulfill the request. They are typically
    #used for redirection or cache-related purposes

    #4xx Client Error
    #These indicate the client's request cannot be fulfilled
    #due to an error on the client's side. Common reasons include
    #invalid request syntax, authentication failure or 
    #insufficient permissions

    #5xx Server Error
    #These indicate the server encountered an error while
    #trying to fulfill the request. It is typically a 
    #server-side issue such as internal server errors or
    #service unavailability
    response.raise_for_status()

    #Parse response to a json format
    response_data = response.json()

    quote = response_data["quote"]
    print(f"{quote}")


#Parameters
#These are used to send data to the server, typically for creating
#or updating a resource
if False:
    API_ENDPOINT = "https://opentdb.com/api.php"

    parameters = {
        "amount": 5,
        "type": "boolean"
    }

    response = requests.get(url=API_ENDPOINT, params=parameters)
    response.raise_for_status()
    response_data = response.json()
    questions = response_data["results"]

    for item in questions:
        print(f"Question: {html.unescape(item['question'])} - {item['correct_answer']}")
    

#Headers and keys
#An API key is a unique identifier used to authenticate requests
#made to an API
#They are usually included in the request header or as a query parameter
if False:
    #https://developer.nutritionix.com/
    NUTITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
    NUTRITION_APP_ID = ""
    NUTRITION_API_KEY = ""


    #Empty because this is on GitHub but typically
    #a long string
    nutrition_headers = {
        "x-app-id": NUTRITION_APP_ID,
        "x-app-key": NUTRITION_API_KEY
    }

    #Example sentence for the API
    nutrition_exercise_text = "I ran for 46 minutes"

    nutrition_parameters = {
        "query": nutrition_exercise_text,
    }
    
    nutrition_response = requests.post(NUTITION_ENDPOINT, json=nutrition_parameters, headers=nutrition_headers)
    nutrition_result = nutrition_response.json()
    print(f"{nutrition_result}")