---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: MongoDB डॉकर कंटेनर पुनर्प्राप्ति गाइड
translated: true
type: note
---

धन्यवाद — `docker inspect` का आउटपुट पुष्टि करता है कि कंटेनर **Dead** है और आपका MongoDB डेटा डायरेक्टरी एक होस्ट बाइंड-माउंट है:
`/Users/lzwjava/projects/LibreChat/data-node:/data/db:rw`.
यह एक अच्छी खबर है — आपकी MongoDB *डेटा फाइलें आपके macOS होस्ट पर हैं*, इसलिए हमारे द्वारा कोई भी डिस्ट्रक्टिव Docker-साइड सफाई करने से पहले उनका बैकअप लिया जा सकता है।

नीचे दो सुरक्षित विकल्प दिए गए हैं। **विकल्प A (सुझाया गया)** आपके डेटा को सुरक्षित रखता है और सरल है: होस्ट डेटा डायरेक्टरी का बैकअप लें, फिर Docker Desktop के Troubleshoot → Clean / Purge का उपयोग करें। **विकल्प B (एडवांस्ड / आखिरी उपाय)** Docker VM स्टेट को लो-लेवल पर डिलीट करने का विकल्प है। मैं सटीक कमांड्स दूंगा ताकि आप कॉपी/पेस्ट कर सकें।

---

# विकल्प A — सुझाया गया (होस्ट डेटा का बैकअप लें, फिर Docker Desktop रीसेट का उपयोग करें)

1. पुष्टि करें कि होस्ट डेटा डायरेक्टरी मौजूद है और उसकी सामग्री सूचीबद्ध करें:

```bash
ls -la /Users/lzwjava/projects/LibreChat/data-node
```

2. उस डायरेक्टरी का tar बैकअप बनाएं (यह आपकी MongoDB फाइलों को सुरक्षित रखता है):

```bash
mkdir -p ~/docker-backups/librechat
tar -czvf ~/docker-backups/librechat/data-node-backup-$(date +%Y%m%dT%H%M%S).tgz -C /Users/lzwjava/projects/LibreChat data-node
# परिणाम: ~/docker-backups/librechat/data-node-backup-YYYYMMDDTHHMMSS.tgz
```

(आप tar के बजाय फोल्डर की कॉपी भी बना सकते हैं अगर आप `cp -a /Users/lzwjava/projects/LibreChat/data-node ~/docker-backups/librechat/data-node-copy` पसंद करते हैं।)

3. Docker Desktop को पूरी तरह से बंद करें:

```bash
osascript -e 'quit app "Docker"'
```

4. Docker Desktop खोलें → Troubleshoot (या Preferences → Troubleshoot) → **Clean / Purge data** पर क्लिक करें (या अगर Clean मौजूद नहीं है तो **Reset to factory defaults**)।

   * **महत्वपूर्ण**: यह Docker इमेजेज, कंटेनर्स और वॉल्यूम्स को हटाता है जो Docker VM के अंदर रहते हैं, लेकिन यह आपके macOS होस्ट से बाइंड-माउंट की गई फाइलों को **नहीं** हटाएगा (आपका `/Users/.../data-node` बैकअप सुनिश्चित करता है कि आप सुरक्षित हैं)।

5. Docker रीसेट होने के बाद, Docker Desktop को फिर से शुरू करें, पुष्टि करें कि Docker चल रहा है, फिर अपना Compose स्टैक वापस लाएं:

```bash
open -a Docker
# तब तक प्रतीक्षा करें जब तक Docker स्वस्थ न हो जाए
docker compose up -d
```

6. Mongo कंटेनर और डेटा जांचें:

```bash
docker ps -a
# docker logs <new-mongo-container-id>  (अगर जरूरत हो)
```

अगर चरण 5/6 में कुछ गलत लगता है, तो बैकअप को रीस्टोर करें: कोई भी चल रहे mongo कंटेनर को रोकें, पुनर्निर्मित data-node फोल्डर को हटाएं या मूव करें और बैकअप को `/Users/lzwjava/projects/LibreChat/data-node` में अनटार करें।

---

# विकल्प B — एडवांस्ड / आखिरी उपाय (Docker Desktop VM फाइलों का मैन्युअल डिलीशन)

इसका उपयोग केवल तभी करें यदि आप Docker Desktop Clean/Purge UI का उपयोग *नहीं* कर सकते या इसने समस्या का समाधान नहीं किया और आप Docker-आंतरिक स्टेट खोने को तैयार हैं।

1. Docker Desktop बंद करें:

```bash
osascript -e 'quit app "Docker"'
```

2. Docker Desktop यूजर कॉन्फ़िग का बैकअप लें (वैकल्पिक):

```bash
cp -a ~/Library/Containers/com.docker.docker ~/Library/Containers/com.docker.docker.backup-$(date +%Y%m%dT%H%M%S)
```

3. Docker Desktop आंतरिक स्टेट हटाएं (विनाशकारी — Desktop VM के अंदर के कंटेनर्स/इमेजेज को डिलीट करता है):

```bash
rm -rf ~/Library/Containers/com.docker.docker
rm -rf ~/.docker
```

4. Docker Desktop को पुनरारंभ करें:

```bash
open -a Docker
```

5. अपना स्टैक पुनः बनाएं:

```bash
docker compose up -d
```

फिर से — आपका होस्ट बाइंड-माउंट किया गया Mongo डेटा अछूता रहेगा क्योंकि यह `/Users/...` में रहता है, जब तक कि आप इसे मैन्युअल रूप से नहीं हटाते।

---

# अतिरिक्त जांच / कमांड्स जो आप यहाँ पेस्ट कर सकते हैं अगर आप चाहते हैं कि रीसेट करने से पहले मैं समीक्षा करूं

(ये गैर-विनाशकारी हैं।)

```bash
# दिखाएँ कि होस्ट पर डेटा मौजूद है
ls -la /Users/lzwjava/projects/LibreChat/data-node

# इमेजेज और वॉल्यूम्स दिखाएँ ताकि हम सेव की योजना बना सकें
docker images
docker volume ls

# त्वरित निदान के लिए docker info & ps
docker info
docker ps -a
```

अगर आप `data-node` फोल्डर के लिए `ls -la` आउटपुट पेस्ट करते हैं, तो मैं पुष्टि करूंगा कि बैकअप स्वस्थ दिखता है। यदि आप पसंद करते हैं, तो विकल्प A के साथ आगे बढ़ें: बैकअप लें (चरण 2) फिर Docker Desktop → Troubleshoot → Clean / Purge चलाएं — यह सबसे साफ-सुथरा समाधान है और आमतौर पर अटके हुए `overlay2` रिमूवल एरर को ठीक कर देता है, साथ ही आपकी Mongo फाइलों को सुरक्षित रखता है।