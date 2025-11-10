---
audio: false
generated: true
image: false
lang: hi
layout: post
title: एपीटी जीपीजी हस्ताक्षर त्रुटि को ठीक करना
translated: true
type: note
---

आपको यह त्रुटि दिखाई दे रही है क्योंकि APT, ShiftKey रिपॉजिटरी से अपडेट करने से मना कर रहा है क्योंकि यह उसके GPG सिग्नेचर को सत्यापित नहीं कर सकता। इसे ठीक करने के आपके पास दो सरल तरीके हैं:

---

## 1. **टूटी हुई रिपॉजिटरी को हटाएं या अक्षम करें**

यदि आपको वास्तव में `https://apt.packages.shiftkey.dev/ubuntu` की आवश्यकता नहीं है, तो बस इसे अक्षम कर दें:

```bash
# उस फ़ाइल को ढूंढें जो उस रिपॉजिटरी को परिभाषित करती है (यह /etc/apt/sources.list.d/ में होगी)
ls /etc/apt/sources.list.d/shiftkey*

# इसे हटा दें (वास्तविक फ़ाइलनाम से बदलें)
sudo rm /etc/apt/sources.list.d/shiftkey.packages.shiftkey.dev.list

# फिर अपडेट करें और इंस्टॉल करें
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

## 2. **रिपॉजिटरी के साइनिंग की को इम्पोर्ट करें**

यदि आप ShiftKey के पैकेजों का उपयोग जारी रखना चाहते हैं, तो आपको इसकी पब्लिक की को प्राप्त करके इंस्टॉल करना होगा:

```bash
# उनकी GPG की को डाउनलोड करें और APT की कीरिंग में डिआर्मर करें
curl -fsSL https://apt.packages.shiftkey.dev/ubuntu/pubkey.gpg \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/shiftkey-archive-keyring.gpg > /dev/null

# रिपॉजिटरी फ़ाइल को एडिट करें ताकि यह उस कीरिंग को रेफरेंस करे।  
# अपने एडिटर में /etc/apt/sources.list.d/shiftkey*.list खोलें, और deb लाइन को इस प्रकार बदलें:
#   deb [signed-by=/usr/share/keyrings/shiftkey-archive-keyring.gpg] https://apt.packages.shiftkey.dev/ubuntu any main

# फिर अपडेट करें और इंस्टॉल करें
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

एक बार जब APT बिना GPG त्रुटियों के अपडेट हो जाएगा, तो आप `pkg-config` और `libssl-dev` इंस्टॉल करने के लिए स्वतंत्र होंगे, और फिर रीबिल्ड कर सकेंगे:

```bash
cargo clean
cargo run
```