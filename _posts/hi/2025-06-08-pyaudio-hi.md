---
audio: false
generated: true
lang: hi
layout: post
title: पोर्टऑडियो और पायऑडियो
translated: true
type: note
---

त्रुटि इसलिए होती है क्योंकि **pyaudio** को संकलित करने के लिए PortAudio विकास हेडर (development headers) की आवश्यकता होती है, जो आपके सिस्टम पर अनुपस्थित हैं। इसे ठीक करने का तरीका यहां बताया गया है:

### चरण-दर-चरण समाधान:

1. **PortAudio विकास हेडर स्थापित करें** (pyaudio के लिए आवश्यक):
```bash
sudo apt update && sudo apt install portaudio19-dev
```

2. **Python विकास उपकरण स्थापित करें** (यदि पहले से स्थापित नहीं हैं):
```bash
sudo apt install python3-dev
```

3. **स्थापना पुनः प्रयास करें**:
```bash
pip install -r requirements.local.txt
```

### यदि आपको अभी भी pycrypto संबंधी समस्याएँ आती हैं:
pycrypto पैकेज deprecated हो चुका है और इसकी संगतता संबंधी समस्याएं हो सकती हैं। इसे **pycryptodome** से बदलने के लिए अपनी `requirements.local.txt` फ़ाइल को संशोधित करें:

1. आवश्यकताओं की फ़ाइल खोलें:
```bash
nano requirements.local.txt
```

2. `pycrypto` को इससे बदलें:
```
pycryptodome
```

3. सहेजें और स्थापना पुनः चलाएँ:
```bash
pip install -r requirements.local.txt
```

### यह काम क्यों करता है:
- `portaudio19-dev` वह PortAudio हेडर प्रदान करता है जो pyaudio के संकलन के लिए आवश्यक था
- `python3-dev` आवश्यक Python विकास हेडर शामिल करता है
- `pycryptodome` deprecated pycrypto का एक संरक्षित ड्रॉप-इन प्रतिस्थापन है

### pycrypto के लिए वैकल्पिक उपाय (यदि आपको इसे रखना ही है):
यदि आपको विशेष रूप से pycrypto की आवश्यकता है, तो पहले build dependencies स्थापित करें:
```bash
sudo apt install build-essential libgmp-dev
pip install pycrypto
```
लेकिन ध्यान दें कि pycrypto की नए Python संस्करणों के साथ संगतता संबंधी समस्याएं हैं।

इन चरणों के बाद, सभी पैकेज सही ढंग से स्थापित हो जाने चाहिए। legacy builds के बारे में DEPRECATION चेतावनियाँ सूचनात्मक हैं और स्थापना को रोकेंगी नहीं - वे संकेत देती हैं कि भविष्य में पैकेजों को PEP 517 builds में माइग्रेट करने की आवश्यकता होगी।