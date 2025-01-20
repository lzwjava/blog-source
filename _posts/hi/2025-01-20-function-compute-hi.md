---
audio: true
lang: hi
layout: post
title: अलीबाबा क्लाउड पर Function Compute
translated: true
---

मैंने Alibaba Cloud के Function Compute का उपयोग करके एक फ़ंक्शन सेट किया है। मेरा लक्ष्य कुछ सामान्य दिखने वाले ट्रैफ़िक को उत्पन्न करना है ताकि मेरे प्रॉक्सी सर्वर की गतिविधि को GFW से छिपाया जा सके। इसके लिए, मैंने अपने प्रॉक्सी के साथ एक बैंडविड्थ सर्वर भी तैनात किया है। अब, मैं Alibaba Cloud के Function Compute का उपयोग करके हर मिनट इस बैंडविड्थ API को एक अनुरोध भेज रहा हूँ, जिससे सामान्य और प्रॉक्सी ट्रैफ़िक का मिश्रण बनाया जा सके।

```python
from flask import Flask, request, jsonify
import requests
import time

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # अनुरोध ID और अन्य विवरण लॉग करें
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # काउंटर शुरू करें
    start_time = time.time()  # शुरुआती समय रिकॉर्ड करें
    duration = 60  # 1 मिनट (60 सेकंड) तक चलाएं
    total_calls = 0  # कुल API कॉल ट्रैक करें
    successful_calls = 0  # सफल API कॉल ट्रैक करें

    # 1 मिनट के लिए लूप
    while time.time() - start_time < duration:
        try:
            # बाहरी /bandwidth API को कॉल करें
            response = requests.get('https://www.lzwjava.xyz/bandwidth')
            response.raise_for_status()  # HTTP त्रुटियों के लिए अपवाद उठाएं
            successful_calls += 1  # सफल कॉल काउंटर बढ़ाएं
        except Exception as e:
            print("Error fetching bandwidth data:", e)
        finally:
            total_calls += 1  # कुल कॉल काउंटर बढ़ाएं

        # अगले अनुरोध से पहले 5 सेकंड प्रतीक्षा करें
        time.sleep(5)

    # अनुरोध का अंत लॉग करें
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