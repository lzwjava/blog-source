---
audio: false
generated: false
lang: hi
layout: post
title: अलीबाबा क्लाउड पर Function Compute
translated: true
---

मैं Alibaba Cloud के Function Compute का उपयोग कर रहा हूँ ताकि सामान्य दिखने वाला ट्रैफिक जनरेट किया जा सके, जो मेरे प्रॉक्सी सर्वर की गतिविधि को GFW से छिपाने में मदद करता है। मैंने अपने प्रॉक्सी के साथ एक बैंडविड्थ सर्वर भी तैनात किया है, और यह Function Compute फंक्शन हर मिनट बैंडविड्थ API को एक अनुरोध भेजता है। इससे सामान्य और प्रॉक्सी ट्रैफिक का मिश्रण बनता है।

```python
from flask import Flask, request, jsonify
import requests
import concurrent.futures

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

# बाहरी API को कॉल करने के लिए फंक्शन
def call_bandwidth_api():
    try:
        response = requests.get('https://www.lzwjava.xyz/bandwidth')
        response.raise_for_status()  # HTTP एरर्स के लिए एक्सेप्शन उठाएं
        return True  # सफलता का संकेत
    except Exception as e:
        print("बैंडविड्थ डेटा प्राप्त करने में त्रुटि:", e)
        return False  # विफलता का संकेत

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # अनुरोध ID और अन्य विवरण लॉग करें
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # काउंटर इनिशियलाइज़ करें
    total_calls = 10  # किए जाने वाले API कॉल की कुल संख्या
    successful_calls = 0  # सफल API कॉल ट्रैक करें

    # ThreadPoolExecutor का उपयोग करके API को 10 बार समवर्ती रूप से कॉल करें
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # एक्सेक्यूटर को टास्क सबमिट करें
        futures = [executor.submit(call_bandwidth_api) for _ in range(total_calls)]

        # सभी टास्क के पूरा होने की प्रतीक्षा करें और सफलताओं की गिनती करें
        for future in concurrent.futures.as_completed(futures):
            if future.result():  # यदि कॉल सफल रहा
                successful_calls += 1

    # अनुरोध के अंत को लॉग करें
    print("FC Invoke End RequestId: " + rid)

    # कॉल और सफल कॉल की संख्या वापस करें
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```