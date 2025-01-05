import requests
url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/delete"

headers = {"accept":"application/json"}

response = requests.delete(url, headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")