import requests

url = "https://api.freeapi.app/api/v1/users/google"

response = requests.get(url)

if response.status_code == 500:
    print(response.json())
else:
    print(f"Error: {response.status_codes}, {response.tex}")


#print(response.json())