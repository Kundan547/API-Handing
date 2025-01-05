import requests

url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/put"

headers = {"accept": "application/json"}

response = requests.put(url, headers=headers)

print(response.json())