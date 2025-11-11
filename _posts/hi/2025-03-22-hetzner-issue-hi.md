---
audio: false
generated: true
lang: hi
layout: post
title: हेत्ज़नर एपीआई समस्या
translated: true
type: note
---

आइए आपके सामने आने वाली त्रुटि का विश्लेषण करें और आपके कोड के साथ क्या हो रहा है, इसे समझाते हैं:

### त्रुटि:
```
Error creating snapshot for server sg5: cannot perform operation because server is locked (locked, f21b9dc9d1535310)
```

यह त्रुटि Hetzner Cloud API (Python SDK `hcloud` के माध्यम से) से आ रही है और इंगित करती है कि `sg5` नाम के सर्वर के लिए स्नैपशॉट बनाने का ऑपरेशन विफल हो गया क्योंकि सर्वर **लॉक** है। एक लॉक सर्वर का मतलब है कि कोई अन्य ऑपरेशन (जैसे, कोई पिछला स्नैपशॉट, रीबूट, या आकार बदलना) वर्तमान में प्रगति पर है, और उस प्रक्रिया के पूरा होने तक सर्वर अस्थायी रूप से नए ऑपरेशन स्वीकार करने से प्रतिबंधित है।

### कोड विवरण:
यहां आपकी स्क्रिप्ट स्पष्टीकरण के साथ दी गई है और त्रुटि कहां से उत्पन्न हो रही है:

```python
from hcloud import Client
import os

# एनवायरनमेंट वेरिएबल से API टोकन प्राप्त करें
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# एक क्लाइंट इंस्टेंस बनाएं
client = Client(token=api_token)

def create_snapshot(server):
    try:
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")

# सभी सर्वरों की सूची बनाएं
servers = client.servers.get_all()

# सर्वर विवरण प्रिंट करें और स्नैपशॉट बनाएं
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")
    create_snapshot(server)
```

1. **API टोकन सेटअप**:
   - स्क्रिप्ट Hetzner API कुंजी को एक एनवायरनमेंट वेरिएबल (`HERTZNER_API_KEY`) से प्राप्त करती है। यदि यह सेट नहीं है, तो यह एक त्रुटि के साथ समाप्त हो जाती है।

2. **क्लाइंट इनिशियलाइज़ेशन**:
   - Hetzner Cloud API के साथ इंटरैक्ट करने के लिए API टोकन का उपयोग करके एक `Client` इंस्टेंस बनाया जाता है।

3. **`create_snapshot` फ़ंक्शन**:
   - यह फ़ंक्शन `client.servers.create_image()` का उपयोग करके किसी दिए गए सर्वर का स्नैपशॉट बनाने का प्रयास करता है।
   - पैरामीटर:
     - `server`: स्नैपशॉट लेने के लिए सर्वर ऑब्जेक्ट।
     - `description`: स्नैपशॉट के लिए एक नाम (जैसे, `sg5-snapshot`)।
     - `type="snapshot"`: निर्दिष्ट करता है कि इमेज प्रकार एक स्नैपशॉट है (बैकअप या ISO के विपरीत)।
   - यदि सफल होता है, तो यह स्नैपशॉट ID प्रिंट करता है; अन्यथा, यह किसी भी अपवाद (exception) को पकड़कर प्रिंट कर देता है (जैसे कि आप जो देख रहे हैं)।

4. **सर्वर लिस्टिंग**:
   - `client.servers.get_all()` आपके Hetzner खाते से संबद्ध सभी सर्वरों की एक सूची प्राप्त करता है।
   - स्क्रिप्ट उनमें से प्रत्येक के लिए लूप करती है, उनका विवरण (ID, नाम, स्थिति, IPs, आदि) प्रिंट करती है, और प्रत्येक के लिए `create_snapshot()` को कॉल करती है।

5. **त्रुटि कहाँ होती है**:
   - `create_snapshot()` फ़ंक्शन के अंदर, `client.servers.create_image()` कॉल सर्वर `sg5` के लिए विफल हो जाता है क्योंकि वह लॉक है। अपवाद संदेश (`cannot perform operation because server is locked`) `hcloud` लाइब्रेरी द्वारा API प्रतिक्रिया के आधार पर उठाया जाता है।

### सर्वर लॉक क्यों है?
एक सर्वर तब लॉक हो जाता है जब कोई ऑपरेशन पहले से ही प्रगति पर होता है। सामान्य कारणों में शामिल हैं:
- कोई अन्य स्नैपशॉट बनाया जा रहा है।
- सर्वर को रीबूट, रीसाइज़, या रीबिल्ड किया जा रहा है।
- कोई पिछला ऑपरेशन अभी तक पूरा नहीं हुआ है।

त्रुटि संदेश में लॉक ID (`f21b9dc9d1535310`) सर्वर को लॉक कर रही चल रली क्रिया के लिए एक अद्वितीय पहचानकर्ता है।

### इसे कैसे ठीक करें:
यहां समस्या को हल करने और आपकी स्क्रिप्ट में सुधार करने के चरण दिए गए हैं:

#### 1. **आगे बढ़ने से पहले लॉक स्थिति की जांच करें**
स्क्रिप्ट को संशोधित करें ताकि सर्वर लॉक होने पर स्नैपशॉट निर्माण को छोड़ दिया जाए। आप `client.actions.get_all()` का उपयोग करके सर्वर की वर्तमान क्रियाओं की जांच कर सकते हैं या लॉक साफ होने की प्रतीक्षा कर सकते हैं।

अपडेट किया गया `create_snapshot` फ़ंक्शन:
```python
def create_snapshot(server):
    try:
        # सर्वर की क्रियाओं को देखकर जांचें कि क्या सर्वर लॉक है
        actions = client.actions.get_all(server=server)
        for action in actions:
            if action.status == "running":
                print(f"Skipping snapshot for {server.name}: Server is locked by action {action.id}")
                return
        # यदि कोई चल रही क्रिया नहीं है, तो स्नैपशॉट के साथ आगे बढ़ें
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 2. **लॉक साफ होने की प्रतीक्षा करें**
यदि आप छोड़ने के बजाय प्रतीक्षा करना चाहते हैं, तो आप लॉक के हटने तक सर्वर की क्रियाओं की जांच कर सकते हैं (poll):
```python
import time

def wait_for_unlock(server):
    while True:
        actions = client.actions.get_all(server=server)
        running = any(action.status == "running" for action in actions)
        if not running:
            break
        print(f"Waiting for server {server.name} to unlock...")
        time.sleep(5)  # दोबारा जांच करने से पहले 5 सेकंड प्रतीक्षा करें

def create_snapshot(server):
    try:
        wait_for_unlock(server)
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 3. **लॉक की मैन्युअल रूप से जांच करें**
- ID `f21b9dc9d1535310` वाली क्रिया की स्थिति की जांच करने के लिए Hetzner Cloud Console या API का उपयोग करें।
- उदाहरण API कॉल (Python के माध्यम से):
  ```python
  action = client.actions.get_by_id("f21b9dc9d1535310")
  print(f"Action Status: {action.status}, Command: {action.command}")
  ```
- यदि यह अटक गई है, तो आपको Hetzner सपोर्ट से संपर्क करने की आवश्यकता हो सकती है।

#### 4. **स्क्रिप्ट को फिर से चलाएं**
एक बार सर्वर लॉक नहीं रह जाता (क्रिया पूरी हो जाती है या आप इसे मैन्युअल रूप से हल कर लेते हैं), स्क्रिप्ट को फिर से चलाएं।

### अतिरिक्त नोट्स:
- **दर सीमाएं (Rate Limits)**: लूप में कई सर्वरों के लिए स्नैपशॉट बनाने से Hetzner की API दर सीमाएं प्रभावित हो सकती हैं। यदि आवश्यक हो तो अनुरोधों के बीच एक विलंब (जैसे, `time.sleep(1)`) जोड़ें।
- **त्रुटि प्रबंधन**: वर्तमान स्क्रिप्ट पहली त्रुटि पर रुक जाती है। यदि आप चाहते हैं कि यह अन्य सर्वरों के लिए जारी रहे, तो सुनिश्चित करें कि अपवाद लूप को नहीं रोकता (आपके मामले में ऐसा नहीं है, जो अच्छा है)।

यदि आपको इनमें से किसी भी सुधार को लागू करने या आगे डीबगिंग में सहायता की आवश्यकता हो तो मुझे बताएं!