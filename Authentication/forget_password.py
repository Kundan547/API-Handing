import requests

url = "https://api.freeapi.app/api/v1/users/forgot-password"

payload = { "email": "user.email@domain.com" }
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())