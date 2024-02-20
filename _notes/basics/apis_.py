#APIs

#An API is a set of rules and protocols that allows different software 
#applications to communicate with each other. It defines the methods and
#data formats that applications can use to request and exchange information


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