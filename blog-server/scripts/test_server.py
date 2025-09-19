import os
import requests

server_ip = os.environ.get('SERVER_IP', 'localhost')
params = {'i': 'eth0'}
url = f"http://{server_ip}:8080/bandwidth"
response = requests.get(url, params=params)
print(response.text)
