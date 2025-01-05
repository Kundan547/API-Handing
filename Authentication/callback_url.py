import requests

url = "https://api.freeapi.app/api/v1/users/google/callback"

response = requests.get(url)

if response.status_code == 500:
    print(response.json())
else:
    print(f"Error: {response.status_codes}, {response.tex}")

