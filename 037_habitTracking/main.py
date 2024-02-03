import requests

USERNAME = ""
TOKEN = ""

pixela_user_url = "https://pixe.la/v1/users"

if False:
    post_user_parameters = {
        "username":USERNAME, 
        "token": TOKEN, 
        "agreeTermsOfService":"yes", 
        "notMinor":"yes"
    }

    pixela_response = requests.post(url=pixela_user_url, json=post_user_parameters)
    print(pixela_response.text)

if True:
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