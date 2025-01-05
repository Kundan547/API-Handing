import requests
url = "https://api.freeapi.app/api/v1/public/randomproducts/23"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
print(response.json())