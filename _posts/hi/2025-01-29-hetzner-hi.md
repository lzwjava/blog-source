---
audio: true
lang: hi
layout: post
title: हेटज़नर क्लाउड
translated: true
---

मैं इस क्लाउड प्लेटफॉर्म को कुछ ही पहले जीते हुए बहुत उत्साहित हूँ।

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*स्रोत: हेत्स्नर*{: .caption }

एक सर्वर हेल्सिन्की में कौन-सा कॉन्फिगरेशन 2 AMD VCPUs, 2GB RAM, 40GB SSD, और 20TB ट्रैफिक की लागत के साथ $4.49 USD प्रति महीने का है।

एक IPv4 एड्रेस की अतिरिक्त लागत का माह प्रति $0.60 USD है, जिससे कुल माह प्रति $5.09 USD हो जाता है।

वे छह स्थानों में सेवाएं प्रदान करते हैं:

- न्यूरनबर्ग, जर्मनी
- फाल्कनस्टाइन, जर्मनी
- हेल्सिन्की, फिन्लैंड
- सिंगापुर, सिंगापुर
- हिल्सबोरो, OR, USA
- एशबर्न, VA, USA

यह इंतेरेस्टिंग है कि वे प्रचलित स्थानों के लिए ट्रैंड्स को अनुसरते हैं नहीं। उनके स्थान वुल्टर या डिजिटल ओशन की तरह अलग हैं।

हेत्स्नर सर्वर का हेल्सिन्की में बहुत जल्द है। स्पिड्टेस्ट iOS एप्प का उपयोग करके, डाउनलोड स्पीड 423 Mbps है, और अपलोड स्पीड 56.1 Mbps है।

शाडौरॉकेट में पिंग 1175 ms है, लेकिन यह एक व्यापक समस्या नहीं है।

एक सर्वर इंस्टान्स डेटा पाने के लिए एक सरल पायथन स्क्रिप्ट।

```python
from hcloud import Client
import os

# एनवायरन्में्ट वारिएबल से API टोकन पाएं
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("त्रुटि: HERTZNER_API_KEY एनवायरन्में्ट वारिएबल नहीं सेट हुआ।")
    exit(1)

# क्लाइंट इंस्टेंस बनाएं
client = Client(token=api_token)

# सभी सर्वरों को लिस्ट करें
servers = client.servers.get_all()

# सर्वर डेटा प्रिंट करें
for server in servers:
    print(f"सर्वर आईडी: {server.id}")
    print(f"सर्वर नाम: {server.name}")
    print(f"सर्वर स्टेटस: {server.status}")
    print(f"सर्वर IPv4: {server.public_net.ipv4.ip}")
    print(f"सर्वर IPv6: {server.public_net.ipv6.ip}")
    print(f"सर्वर टाइप: {server.server_type.name}")
    print(f"सर्वर स्थान: {server.datacenter.location.name}")
    print("----------------------------------")

# एक विशेष सर्वर को एडीडी से पाने के लिए
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"विशेष सर्वर आईडी: {server.id}")
print(f"विशेष सर्वर नाम: {server.name}")
print(f"विशेष सर्वर स्टेटस: {server.status}")
print(f"विशेष सर्वर IPv4: {server.public_net.ipv4.ip}")
print(f"विशेष सर्वर IPv6: {server.public_net.ipv6.ip}")
print(f"विशेष सर्वर टाइप: {server.server_type.name}")
print(f"विशेष सर्वर स्थान: {server.datacenter.location.name}")
```