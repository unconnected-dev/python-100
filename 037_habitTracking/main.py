import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""

pixela_user_url = "https://pixe.la/v1/users"

#creating an account
if False:
    post_user_parameters = {
        "username":USERNAME, 
        "token": TOKEN, 
        "agreeTermsOfService":"yes", 
        "notMinor":"yes"
    }

    pixela_response = requests.post(url=pixela_user_url, json=post_user_parameters)
    print(pixela_response.text)


#Creating a new graph
if False:
    pixela_graph_url = f"{pixela_user_url}/{USERNAME}/graphs"

    graph_header = {
        "X-USER-TOKEN": TOKEN
    }

    graph_config = {
        "id": "graph1",
        "name": "test graph",
        "unit": "t",
        "type": "float",
        "color": "momiji"
    }

    pixela_response = requests.post(url=pixela_graph_url, json=graph_config, headers=graph_header)


#Posting a pixel
if False:
    pixela_graph_specific_url = f"{pixela_user_url}/{USERNAME}/graphs/graph1"

    graph_header = {
        "X-USER-TOKEN": TOKEN
    }
    
    graph_post_parameters = {
        "date":"20240204",
        "quantity":"5"
    }
    
    pixela_response = requests.post(url=pixela_graph_specific_url, json=graph_post_parameters, headers=graph_header)
    print(f"{pixela_response}")


#Could use strftime to post current date
if False:
    current_date = datetime.now()
    print(f"{current_date.strftime('%Y%m%d')}")

    a_previous_date = datetime(year=2020, month=1, day=30)
    print(f"{a_previous_date.strftime('%Y%m%d')}")


#Updating a pixel
if False:
    pixela_graph_date_specific_url = f"{pixela_user_url}/{USERNAME}/graphs/graph1/20240204"

    graph_header = {
        "X-USER-TOKEN": TOKEN
    }
    
    graph_date_post_parameters = {
        "quantity":"2"
    }
    
    pixela_response = requests.put(url=pixela_graph_date_specific_url, json=graph_date_post_parameters, headers=graph_header)
    print(f"{pixela_response}")