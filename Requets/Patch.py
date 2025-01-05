import requests

url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/patch"

headers = {"accept": "application/json"}

response = requests.patch(url, headers=headers)

print(response.json())