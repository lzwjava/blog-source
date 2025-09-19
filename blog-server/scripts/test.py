import requests

params = {'x': 'hi'}
response = requests.get("http://localhost:8080/bandwidth", params=params)
print(response.headers)
print(response.text)
