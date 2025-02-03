import requests

url = "https://api.freeapi.app/api/v1/public/randomusers"

querystring = {"page":"1", "limit":"5"}
headers = {"accept": "application/json"}

response = requests.get(url, headers=headers, params = querystring)

##print(response.json())
if response.status_code == 200:
    print(response.json())
    
else:
    print(f"Error: {response.status_code}, {response.text}")