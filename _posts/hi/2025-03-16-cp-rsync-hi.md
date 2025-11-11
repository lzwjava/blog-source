---
audio: false
generated: true
lang: hi
layout: post
title: निर्देशिका संरचना के साथ फ़ाइलों की प्रतिलिपि बनाना
translated: true
type: note
---

आपके `find` कमांड आउटपुट के अनुसार, आप सभी `.log` फाइलों को `/Users/lzwjava/projects/logs` में कॉपी करना चाहते हैं, उनकी डायरेक्टरी संरचना को बनाए रखते हुए। उदाहरण के लिए, `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` जैसी फाइल `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` के रूप में कॉपी होनी चाहिए। मैं आपको दिखाऊंगा कि `find` को `cp` या `rsync` के साथ कैसे उपयोग करके यह प्राप्त किया जाए, यह सुनिश्चित करते हुए कि डायरेक्टरी पदानुक्रम बना रहे।

---

### **समाधान 1: `find` के साथ `cp` का उपयोग करना**
आप `.log` फाइलों को ढूंढने के लिए `find` और उनकी डायरेक्टरी संरचना को बनाए रखते हुए कॉपी करने के लिए `cp` को `--parents` विकल्प के साथ उपयोग कर सकते हैं।

#### **कमांड**
```bash
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

#### **स्पष्टीकरण**
- **`find . -name "*.log"`**: वर्तमान डायरेक्टरी और उप-डायरेक्टरीज़ में सभी `.log` फाइलों को ढूंढता है (जैसा कि आपके उदाहरण में है)।
- **`-exec cp --parents {} /Users/lzwjava/projects/logs \;`**:
  - `cp --parents`: फाइल को कॉपी करता है और स्रोत (`.`) के सापेक्ष उसके डायरेक्टरी पथ को पुनः बनाता है।
  - `{}`: `find` द्वारा पाई गई प्रत्येक फाइल के लिए प्लेसहोल्डर।
  - `/Users/lzwjava/projects/logs`: गंतव्य डायरेक्टरी।
  - `\;`: `-exec` कमांड को समाप्त करता है।

#### **परिणाम**
- `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` → `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`
- `CoreSimulator` के तहत डायरेक्टरी संरचना बनी रहती है।

#### **चलाने से पहले**
- सुनिश्चित करें कि `/Users/lzwjava/projects/logs` मौजूद है:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **समाधान 2: `rsync` का उपयोग करना**
`rsync` एक और शक्तिशाली टूल है जो डायरेक्टरी संरचना को बनाए रखते हुए फाइलों को कॉपी कर सकता है, और यह बड़े पैमाने पर ऑपरेशन के लिए अक्सर अधिक कुशल होता है।

#### **कमांड**
```bash
find . -name "*.log" -exec rsync -R -a {} /Users/lzwjava/projects/logs \;
```

#### **स्पष्टीकरण**
- **`-R`**: सापेक्ष पथों का उपयोग करता है, स्रोत (`.`) से डायरेक्टरी संरचना को बनाए रखता है।
- **`-a`**: आर्काइव मोड (टाइमस्टैम्प, अनुमतियाँ आदि को संरक्षित करता है)।
- `{}`: `find` द्वारा पाई गई प्रत्येक `.log` फाइल।
- `/Users/lzwjava/projects/logs`: लक्ष्य डायरेक्टरी।

#### **परिणाम**
ऊपर के समान—फाइलें उनके पूर्ण सापेक्ष पथों के साथ कॉपी हो जाती हैं।

#### **चलाने से पहले**
- गंतव्य डायरेक्टरी बनाएं यदि यह मौजूद नहीं है:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **कॉपी सत्यापित करना**
दोनों में से किसी भी कमांड को चलाने के बाद, गंतव्य की जांच करें:
```bash
ls -R /Users/lzwjava/projects/logs
```
आपको यह देखना चाहिए:
```
/Users/lzwjava/projects/logs:
CoreSimulator

/Users/lzwjava/projects/logs/CoreSimulator:
CoreSimulator.log  FC275C39-59CC-4483-A64E-5D459D7A1D57  Simulator.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57:
com.apple.itunesstored  system.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/com.apple.itunesstored:
itunesstored.log
```

---

### **मुख्य नोट्स**
- **अनुमतियाँ:** सुनिश्चित करें कि आपके पास `/Users/lzwjava/projects/logs` के लिए लिखने की अनुमति है। यदि नहीं, तो `sudo` का उपयोग करें (जैसे, `sudo cp ...`) या अनुमतियाँ समायोजित करें:
  ```bash
  chmod -R u+w /Users/lzwjava/projects/logs
  ```
- **ओवरराइटिंग:** यदि फाइलें गंतव्य पर पहले से मौजूद हैं:
  - `cp` बिना चेतावनी के ओवरराइट कर देगा।
  - `rsync -a` भी ओवरराइट करेगा, लेकिन आप मौजूदा फाइलों को छोड़ने के लिए `--ignore-existing` जोड़ सकते हैं:
    ```bash
    find . -name "*.log" -exec rsync -R -a --ignore-existing {} /Users/lzwjava/projects/logs \;
    ```
- **ड्राई रन (पहले परीक्षण करें):**
  - `cp` के लिए, पूर्वावलोकन करने के लिए `echo` जोड़ें:
    ```bash
    find . -name "*.log" -exec echo cp --parents {} /Users/lzwjava/projects/logs \;
    ```
  - `rsync` के लिए, `--dry-run` का उपयोग करें:
    ```bash
    find . -name "*.log" -exec rsync -R -a --dry-run {} /Users/lzwjava/projects/logs \;
    ```

---

### **कौन सा चुनें?**
- **`cp`**: सरल, किसी अतिरिक्त टूल की आवश्यकता नहीं (सभी यूनिक्स-जैसी प्रणालियों पर उपलब्ध)।
- **`rsync`**: अधिक लचीला (जैसे, सिंक करने, डुप्लिकेट छोड़ने के लिए), लेकिन इसके लिए `rsync` इंस्टॉल होना आवश्यक है (अधिकांश प्रणालियों पर मानक)।

आपके मामले के लिए दोनों काम करेंगे। सादगी के लिए मैं `cp --parents` से शुरुआत करने की सलाह देता हूं।

---

### **अंतिम कमांड (अनुशंसित)**
```bash
mkdir -p /Users/lzwjava/projects/logs
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

इसे अपनी `Logs` डायरेक्टरी (`lzwjava@anonymous Logs %`) से चलाएं, और आपका काम हो गया! यदि आपको कोई समस्या आती है या आप व्यवहार को समायोजित करना चाहते हैं (जैसे, संरचना को समतल करना), तो मुझे बताएं।