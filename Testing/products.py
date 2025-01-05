import requests

url = "https://api.freeapi.app/api/v1/public/randomproducts"

querystring = {"page":"1","limit":"2","inc":"category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid","query":"mens-watches"}

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())