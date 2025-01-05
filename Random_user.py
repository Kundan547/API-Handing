import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

headers = {"accept": "application/json"}
querystring = {"limit":"2"}
response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data =  response.json()
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")