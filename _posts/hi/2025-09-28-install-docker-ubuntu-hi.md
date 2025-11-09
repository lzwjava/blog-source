---
audio: false
generated: true
image: false
lang: hi
layout: post
model: anthropic/claude-sonnet-4
title: उबुन्टू पर डॉकर इंस्टॉल करने की गाइड
translated: true
type: note
---

आपके Ubuntu सिस्टम आउटपुट के आधार पर, Docker इंस्टॉल करने के लिए आपके पास कई विकल्प हैं। यहाँ अनुशंसित तरीका दिया गया है:

## विकल्प 1: Docker Engine इंस्टॉल करें (अनुशंसित)

सबसे आम और अनुशंसित तरीका है Docker Engine को Docker की आधिकारिक रिपॉजिटरी से इंस्टॉल करना:

```bash
# पैकेज इंडेक्स अपडेट करें
sudo apt update

# पूर्व-आवश्यकताएँ इंस्टॉल करें
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Docker का आधिकारिक GPG key जोड़ें
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Docker रिपॉजिटरी जोड़ें
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# पैकेज इंडेक्स फिर से अपडेट करें
sudo apt update

# Docker Engine इंस्टॉल करें
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## विकल्प 2: APT के माध्यम से त्वरित इंस्टॉलेशन (सरल)

आपके टर्मिनल में दिखाए गए विकल्पों से, आप इस्तेमाल कर सकते हैं:

```bash
sudo apt install docker.io
```

## इंस्टॉलेशन के बाद की सेटअप

इंस्टॉलेशन के बाद, आप यह करना चाहेंगे:

1. **Docker सेवा शुरू और सक्षम करें:**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

2. **अपने यूज़र को docker ग्रुप में जोड़ें** (बिना sudo के Docker चलाने के लिए):
```bash
sudo usermod -aG docker $USER
```

फिर लॉग आउट करें और वापस लॉग इन करें, या चलाएँ:
```bash
newgrp docker
```

3. **इंस्टॉलेशन सत्यापित करें:**
```bash
docker --version
docker run hello-world
```

## कौन सा विकल्प चुनें?

- **विकल्प 1** आपको Docker Inc. से सीधे Docker का नवीनतम वर्जन देता है।
- **विकल्प 2** सरल है लेकिन Ubuntu की रिपॉजिटरीज़ से थोड़ा पुराना वर्जन हो सकता है।

ज्यादातर यूज़र्स के लिए, विकल्प 2 (`sudo apt install docker.io`) पूरी तरह से ठीक है और बहुत सरल है। नियमित उपयोग के लिए वर्जन का अंतर आमतौर पर न्यूनतम होता है।

क्या आप इनमें से किसी भी चरण के बारे में और विस्तार से समझना चाहेंगे?