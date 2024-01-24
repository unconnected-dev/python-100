import requests

#API Endpoint
#Returns status code
#https://www.webfx.com/web-development/glossary/http-status-codes/
response = requests.get(url="http://api.open-notify.org/iss-now.json")

#Will raise HTTP error if unsuccessful status code
response.raise_for_status()

# print(response.status_code)
# print(response.content)

response_data = response.json()
print(response_data)
print(response_data["iss_position"]["longitude"])
print(response_data["iss_position"]["latitude"])