import os
import requests

server_host = 'lzwjava.shop'
params = {'i': 'eth0'}
url = f"https://{server_host}/bandwidth"
response = requests.get(url, params=params)
print(response.text)
