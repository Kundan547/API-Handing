import os
import requests
import logging

logging.basicConfig(level=logging.INFO)

url = "https://api.freeapi.app/api/v1/users/login"
payload = {
    "username": os.getenv("API_USERNAME", "doejohn"),
    "password": os.getenv("API_PASSWORD", "test@123")
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

try:
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    if response.ok:
        logging.info("Login successful!")
        logging.info(response.json())
    else:
        logging.error(f"Error: {response.status_code}, {response.json() if response.headers.get('content-type') == 'application/json' else response.text}")
except requests.exceptions.RequestException as e:
    logging.error(f"Request failed: {e}")
