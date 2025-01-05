import requests

url = "https://api.freeapi.app/api/v1/users/login"

payload = {
    "password": "test@123",
    "username": "doejohn"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("Login successful!")
    print(response.json()) 
else:
    print(f"Error: {response.status_code}, {response.text}") 
