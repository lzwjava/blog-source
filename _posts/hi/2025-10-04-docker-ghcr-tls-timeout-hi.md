---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: डॉकर जीएचसीआर टीएलएस टाइमआउट त्रुटि को ठीक करना
translated: true
type: note
---

आपके सामने आ रही यह त्रुटि, `Get "https://ghcr.io/v2/": net/http: TLS handshake timeout`, आमतौर पर तब होती है जब Docker, GitHub Container Registry (GHCR) से images को pull करने का प्रयास करता है और नेटवर्क में कोई समस्या होती है। इस समस्या के समाधान और जांच के लिए यहां कुछ कदम दिए गए हैं:

---

### 1. **अपने इंटरनेट कनेक्शन की जांच करें**
- सुनिश्चित करें कि आपके मशीन का इंटरनेट कनेक्शन स्थिर है।
- साइट तक पहुंच की पुष्टि करने के लिए अपने ब्राउज़र में `https://ghcr.io` तक पहुंचने का प्रयास करें।

---

### 2. **Docker Daemon की स्थिति की जांच करें**
- Docker daemon को पुनरारंभ करें:
  ```bash
  sudo systemctl restart docker
  ```
- सत्यापित करें कि Docker चल रहा है:
  ```bash
  sudo systemctl status docker
  ```

---

### 3. **Docker DNS कॉन्फ़िगर करें**
- यदि आप कॉर्पोरेट नेटवर्क या प्रॉक्सी के पीछे हैं, तो Docker को कस्टम DNS सेटिंग्स की आवश्यकता हो सकती है।
- `/etc/docker/daemon.json` को संपादित करें या बनाएं:
  ```json
  {
    "dns": ["8.8.8.8", "1.1.1.1"]
  }
  ```
- Docker को पुनरारंभ करें:
  ```bash
  sudo systemctl restart docker
  ```

---

### 4. **प्रॉक्सी सेटिंग्स की जांच करें**
- यदि आप प्रॉक्सी के पीछे हैं, तो Docker को उसका उपयोग करने के लिए कॉन्फ़िगर करें:
  ```bash
  mkdir -p ~/.docker
  echo '{
    "proxies": {
      "default": {
        "httpProxy": "http://your-proxy-address:port",
        "httpsProxy": "http://your-proxy-address:port",
        "noProxy": "localhost,127.0.0.1"
      }
    }
  }' > ~/.docker/config.json
  ```
- `your-proxy-address:port` को अपने वास्तविक प्रॉक्सी विवरण से बदलें।

---

### 5. **Image को मैन्युअल रूप से Pull करने का पुनः प्रयास करें**
- देखें कि क्या समस्या बनी रहती है, image को मैन्युअल रूप से pull करने का प्रयास करें:
  ```bash
  docker pull ghcr.io/librechat/librechat:latest
  ```
- यदि यह काम करता है, तो `docker-compose up -d` का पुनः प्रयास करें।

---

### 6. **फ़ायरवॉल/नेटवर्क प्रतिबंधों की जांच करें**
- सुनिश्चित करें कि आपका फ़ायरवॉल या नेटवर्क `ghcr.io` तक पहुंच को ब्लॉक नहीं कर रहा है।
- परीक्षण करने के लिए फ़ायरवॉल को अस्थायी रूप से अक्षम करें:
  ```bash
  sudo ufw disable
  ```
  (यदि आवश्यक हो तो परीक्षण के बाद इसे पुनः सक्षम करें।)

---

### 7. **Docker और Docker-Compose को अपडेट करें**
- सुनिश्चित करें कि आप नवीनतम संस्करणों का उपयोग कर रहे हैं:
  ```bash
  sudo apt update && sudo apt upgrade docker-ce docker-compose-plugin
  ```

---

### 8. **UID/GID एनवायरनमेंट वेरिएबल्स सेट करें**
- `UID` और `GID` के बारे में चेतावनियां गंभीर नहीं हैं, लेकिन आप उन्हें अपनी `.env` फ़ाइल या `docker-compose.yml` में सेट करके चेतावनियों को दबा सकते हैं:
  ```bash
  echo "UID=$(id -u)" >> .env
  echo "GID=$(id -g)" >> .env
  ```

---

### 9. **एक अलग रजिस्ट्री मिरर का उपयोग करें (वैकल्पिक)**
- यदि GHCR लगातार पहुंच से बाहर है, तो आप एक मिरर का उपयोग करने का प्रयास कर सकते हैं (हालांकि यह प्रोडक्शन के लिए अनुशंसित नहीं है):
  ```json
  {
    "registry-mirrors": ["https://mirror.example.com"]
  }
  ```
- इसे `/etc/docker/daemon.json` में जोड़ें और Docker को पुनरारंभ करें।

---

### 10. **टाइम सिंक्रोनाइज़ेशन की जांच करें**
- सुनिश्चित करें कि आपका सिस्टम समय सिंक्रोनाइज़ है:
  ```bash
  sudo apt install ntp
  sudo systemctl restart ntp
  ```

---

### कमांड्स की सारांश तालिका

| चरण | कमांड/क्रिया |
|------|----------------|
| Docker पुनरारंभ करें | `sudo systemctl restart docker` |
| Docker स्थिति जांचें | `sudo systemctl status docker` |
| DNS कॉन्फ़िगर करें | `/etc/docker/daemon.json` संपादित करें |
| Image मैन्युअल Pull करें | `docker pull ghcr.io/librechat/librechat:latest` |
| UID/GID सेट करें | `echo "UID=$(id -u)" >> .env` |

---

यदि इन चरणों को आजमाने के बाद भी समस्या बनी रहती है, तो मुझे निम्नलिखित का आउटपुट बताएं:
```bash
docker info
```
और उपरोक्त कमांड चलाते समय दिखने वाले कोई भी त्रुटि संदेश। इससे आगे निदान करने में मदद मिलेगी!