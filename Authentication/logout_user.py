import requests

url = "https://api.freeapi.app/api/v1/users/logout"

headers = {"accept": "application/json"}

response = requests.post(url, headers=headers)

print(response.json())