import requests

url = "https://api.freeapi.app/api/v1/public/randomjokes/100"

##querystring = {"limit":"10","query":"science","inc":"categories%2Cid%2Ccontent","page":"1"}

headers = {"accpet": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
    
else:
    print(f"Error: {response.status_code}, {response.text}")