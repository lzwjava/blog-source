---
audio: true
lang: en
layout: post
title: Function Compute on Alibaba Cloud
---

I've set up a function using Alibaba Cloud's Function Compute. My goal is to generate some normal-looking traffic to help obscure my proxy server's activity from the GFW. To do this, I've deployed a bandwidth server alongside my proxy. Now, I'm using Alibaba Cloud's Function Compute to make a request to this bandwidth API every minute, creating a mix of normal and proxy traffic.

```python
from flask import Flask, request, jsonify
import requests

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # Log the request ID and other details
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # Call the external /bandwidth API
    try:
        response = requests.get('https://www.lzwjava.xyz/bandwidth')
        bandwidth_data = response.json()
        print("Bandwidth Data:", bandwidth_data)
    except Exception as e:
        print("Error fetching bandwidth data:", e)
        bandwidth_data = {"error": "Failed to fetch bandwidth data"}

    # Log the end of the request
    print("FC Invoke End RequestId: " + rid)

    # Return the bandwidth data as part of the response
    return jsonify({
        "message": "Hello, World!",
        "bandwidth_data": bandwidth_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```