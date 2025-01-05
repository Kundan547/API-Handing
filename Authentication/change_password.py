import requests

url = "https://api.freeapi.app/api/v1/users/change-password"

payload = {
    "newPassword": "test@123",
    "oldPassword": "new@123"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())