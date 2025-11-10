---
audio: false
generated: true
image: false
lang: hi
layout: post
title: उबुन्टू के लिए Node.js अपग्रेड गाइड
translated: true
type: note
---

Ubuntu पर Node.js को अपग्रेड करने के कई तरीके हैं। सबसे विश्वसनीय और अनुशंसित तरीके **`nvm` (Node Version Manager)** या **NodeSource रिपॉजिटरी** का उपयोग करना हैं। नीचे दोनों तरीकों के लिए चरण-दर-चरण निर्देश दिए गए हैं।

---

## **विधि 1: NVM का उपयोग करना (अनुशंसित)**
NVM आपको आसानी से कई Node.js संस्करण स्थापित और प्रबंधित करने की अनुमति देता है।

### 1. NVM स्थापित करें
एक टर्मिनल खोलें और चलाएँ:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
फिर, अपने शेल को रीलोड करें:
```bash
source ~/.bashrc
```
या
```bash
source ~/.zshrc
```
(आपके शेल के आधार पर)

### 2. नवीनतम Node.js संस्करण स्थापित करें
उपलब्ध संस्करणों की सूची देखें:
```bash
nvm ls-remote
```
नवीनतम LTS संस्करण स्थापित करें (अधिकांश उपयोगकर्ताओं के लिए अनुशंसित):
```bash
nvm install --lts
```
या कोई विशिष्ट संस्करण स्थापित करें (उदाहरण के लिए, 20.x):
```bash
nvm install 20
```

### 3. डिफ़ॉल्ट संस्करण सेट करें
```bash
nvm alias default 20
```

### 4. सत्यापित करें
```bash
node -v
npm -v
```

---

## **विधि 2: NodeSource रिपॉजिटरी का उपयोग करना**
यह विधि Node.js को सिस्टम-वाइड स्थापित करती है।

### 1. पुराना Node.js हटाएँ (यदि apt के माध्यम से स्थापित है)
```bash
sudo apt remove --purge nodejs npm
sudo apt autoremove
```

### 2. NodeSource रिपॉजिटरी जोड़ें
**Node.js 20.x** के लिए (अगस्त 2025 तक LTS):
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```
**Node.js 22.x** के लिए (यदि उपलब्ध हो):
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
```

### 3. Node.js स्थापित करें
```bash
sudo apt install -y nodejs
```

### 4. सत्यापित करें
```bash
node -v
npm -v
```

---

## **विधि 3: Ubuntu डिफ़ॉल्ट रिपॉजिटरी का उपयोग करना (अनुशंसित नहीं)**
Ubuntu की डिफ़ॉल्ट रिपॉजिटरी में अक्सर पुराने Node.js संस्करण होते हैं। यदि आप फिर भी इसका उपयोग करना चाहते हैं:
```bash
sudo apt update
sudo apt install nodejs npm
```
लेकिन यह विकास के लिए **अनुशंसित नहीं** है, क्योंकि संस्करण आमतौर पर पुराना होता है।

---

## **आपको किस विधि का उपयोग करना चाहिए?**
- **NVM का उपयोग करें** यदि आप आसानी से Node.js संस्करणों के बीच स्विच करना चाहते हैं या नवीनतम सुविधाओं की आवश्यकता है।
- **NodeSource का उपयोग करें** यदि आप एक सिस्टम-वाइड, स्थिर स्थापना चाहते हैं।