---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: डॉकर कंपोज़ के बिना लिबरचैट सेटअप
translated: true
type: note
---

हाँ, आप LibreChat को Docker Compose के बिना भी सेट अप कर सकते हैं, अलग-अलग `docker run` कमांड्स का इस्तेमाल करके या फिर एक गैर-डॉकर तरीके से (Node.js, Yarn, MongoDB, और MeiliSearch के साथ मैन्युअल इंस्टॉलेशन)। इससे `docker-compose` बाइनरी को डाउनलोड करने से बच जाता है (जो छोटी है, ~20-30MB, लेकिन मेरा अनुमान है कि आपका मतलब LibreChat की सर्विसेज के लिए कुल ~70MB+ इमेज पुल्स से है)। हालाँकि, कोर Docker इमेजेज (जैसे ऐप, MongoDB, MeiliSearch के लिए) फिर भी कुल मिलाकर लगभग 500MB-1GB की होंगी जब उन्हें पुल किया जाएगा—Docker Compose सिर्फ Docker के ऊपर एक ऑर्केस्ट्रेशन टूल है, मुख्य बैंडविड्थ उपयोगकर्ता नहीं। धीमे 4G/5G पर इमेजेज पुल करना फिर भी बॉटलनेक होगा, लेकिन आप इसे कम कर सकते हैं।

मैं नीचे विकल्पों की रूपरेखा दूंगा, पहली प्राथमिकता बैंडविड्थ बचाने के टिप्स को देते हुए। अगर मोबाइल डेटा बहुत सीमित है, तो अस्थायी रूप से वाई-फाई नेटवर्क से टेदरिंग करने पर विचार करें या किसी दूसरी मशीन पर पहले से डाउनलोड किए गए सेटअप का इस्तेमाल करें (जैसे, `docker save`/`docker load` के जरिए इमेजेज को एक्सपोर्ट/इम्पोर्ट करके)।

### किसी भी Docker-आधारित सेटअप के लिए बैंडविड्थ बचत टिप्स
- **तेज कनेक्शन पर इमेजेज पहले से पुल करें**: बेहतर इंटरनेट वाले किसी दूसरे डिवाइस पर, `docker pull node:20-alpine` (ऐप के लिए), `docker pull mongo:7` (डेटाबेस), और `docker pull getmeili/meilisearch:v1.10` (सर्च) चलाएं। फिर उन्हें फाइलों में सेव करें:
  ```
  docker save -o librechat-app.tar node:20-alpine
  docker save -o mongo.tar mongo:7
  docker save -o meili.tar getmeili/meilisearch:v1.10
  ```
  .tar फाइलों को USB/ड्राइव के जरिए ट्रांसफर करें (कुल ~500-800MB कंप्रेस्ड), फिर आपकी Ubuntu मशीन पर: `docker load -i librechat-app.tar` आदि। ऑनलाइन पुलिंग की जरूरत नहीं।
- **हल्के विकल्पों का इस्तेमाल करें**: टेस्टिंग के लिए, शुरुआत में MeiliSearch को छोड़ दें (यह सर्च के लिए ऑप्शनल है; कॉन्फ़िग में डिसेबल करें)। MongoDB इमेज ~400MB की है—इसके बजाय लोकल MongoDB इंस्टॉल करके ~400MB बचाएं (नीचे गैर-डॉकर सेक्शन देखें)।
- **उपयोग पर नजर रखें**: `docker pull --quiet` या `watch docker images` जैसे टूल्स का इस्तेमाल करके ट्रैक करें।
- **प्रॉक्सी या कैश**: अगर आपके पास Docker Hub मिरर या प्रॉक्सी है, तो `/etc/docker/daemon.json` में कॉन्फ़िगर करें ताकि पुल्स तेज हों।

### विकल्प 1: शुद्ध Docker (Compose नहीं) – Compose सेटअप के बराबर
आप `docker-compose.yml` के बिहेवियर को `docker run` और `docker network` से रिप्लिकेट कर सकते हैं। यह वही इमेजेज डाउनलोड करता है लेकिन आपको हर स्टेप कंट्रोल करने देता है। कुल डाउनलोड फिर भी ~700MB+ (ऐप बिल्ड + DBs)।

1. **एक Docker नेटवर्क बनाएं** (सर्विसेज को अलग करता है):
   ```
   docker network create librechat-network
   ```

2. **MongoDB चलाएं** (`your_mongo_key` को एक मजबूत पासवर्ड से बदलें):
   ```
   docker run -d --name mongodb --network librechat-network \
     -e MONGO_INITDB_ROOT_USERNAME=librechat \
     -e MONGO_INITDB_ROOT_PASSWORD=your_mongo_key \
     -v $(pwd)/data/mongodb:/data/db \
     mongo:7
   ```
   - पर्सिस्टेंस के लिए `./data/mongodb` बनाता है।

3. **MeiliSearch चलाएं** (`your_meili_key` को बदलें):
   ```
   docker run -d --name meilisearch --network librechat-network \
     -e MEILI_MASTER_KEY=your_meili_key \
     -p 7700:7700 \
     -v $(pwd)/data/meili:/meili_data \
     getmeili/meilisearch:v1.10
   ```
   - अगर बैंडविड्थ टाइट है तो छोड़ दें; बाद में ऐप कॉन्फ़िग में डिसेबल करें।

4. **LibreChat ऐप को क्लोन और बिल्ड/रन करें**:
   - अगर नहीं किया है तो रेपो क्लोन करें: `git clone https://github.com/danny-avila/LibreChat.git && cd LibreChat` (~50MB रेपो के लिए)।
   - इमेज बिल्ड करें (यह Node.js बेस ~200MB पुल करता है और ऐप लेयर्स बिल्ड करता है):
     ```
     docker build -t librechat-app .
     ```
   - इसे रन करें (DB से लिंक करता है, env वेरिएबल्स का इस्तेमाल करता है—मेरी पिछली प्रतिक्रिया की तरह एक `.env` फाइल बनाएं):
     ```
     docker run -d --name librechat --network librechat-network -p 3080:3080 \
       --env-file .env \
       -v $(pwd):/app \
       librechat-app
     ```
     - `.env` में, `MONGODB_URI=mongodb://librechat:your_mongo_key@mongodb:27017/LibreChat` और `MEILI_HOST=http://meilisearch:7700` आदि सेट करें।

5. **एक्सेस**: `http://localhost:3080`। लॉग्स: `docker logs -f librechat`।

- **स्टॉप/क्लीनअप**: `docker stop mongodb meilisearch librechat && docker rm them`।
- **फायदे/नुकसान**: Compose जैसा ही, लेकिन ज्यादा मैन्युअल। इमेज पुल्स/बिल्ड के लिए अभी भी डेटा भारी।

### विकल्प 2: गैर-डॉकर इंस्टॉलेशन (मैन्युअल, कोई इमेज पुल नहीं) – कम बैंडविड्थ के लिए सुझाया गया
Ubuntu पर नेटिवली डिपेंडेंसीज इंस्टॉल करें। यह सभी Docker ओवरहेड से बचाता है (~0MB कंटेनर्स के लिए; सिर्फ apt/yarn के जरिए पैकेज डाउनलोड, कुल ~200-300MB)। आपके सिस्टम के Python/Node सेटअप्स का अप्रत्यक्ष रूप से इस्तेमाल करता है।

#### पूर्वापेक्षाएँ (एक बार इंस्टॉल करें)
```
sudo apt update
sudo apt install nodejs npm mongodb-org redis meilisearch git curl build-essential python3-pip -y  # MongoDB ऑफिशियल पैकेज; MeiliSearch ~50MB बाइनरी
sudo systemctl start mongod redis meilisearch
sudo systemctl enable mongod redis meilisearch
```
- Node.js: अगर v20+ नहीं है, तो nvm के जरिए इंस्टॉल करें: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`, फिर `nvm install 20`।
- Yarn: `npm install -g yarn`।
- MongoDB कॉन्फ़िग: `/etc/mongod.conf` एडिट करके localhost पर बाइंड करें, रीस्टार्ट करें।

#### इंस्टॉलेशन स्टेप्स
1. **रेपो क्लोन करें**:
   ```
   cd ~/projects
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **डिपेंडेंसीज इंस्टॉल करें**:
   ```
   yarn install  # पैकेजेस के लिए ~100-200MB डाउनलोड
   ```

3. **`.env` कॉन्फ़िगर करें** (`.env.example` से कॉपी करें):
   - `cp .env.example .env && nano .env`
   - मुख्य बदलाव:
     - Mongo: `MONGODB_URI=mongodb://localhost:27017/LibreChat` (अगर जरूरत हो तो `mongo` शेल के जरिए DB यूजर बनाएं)।
     - Meili: `MEILI_HOST=http://localhost:7700` और `MEILI_MASTER_KEY=your_key`।
     - अगर Meili छोड़ रहे हैं तो सर्च डिसेबल करें: `SEARCH=false`।
     - जरूरत के हिसाब से AI कीज एड करें।

4. **बिल्ड और रन करें**:
   - एक टर्मिनल में: `yarn run backend` (पोर्ट 3090 पर API शुरू करता है)।
   - दूसरे में: `yarn run frontend` (पोर्ट 3080 पर UI शुरू करता है)।
   - या प्रोडक्शन के लिए PM2 का इस्तेमाल करें: `yarn global add pm2 && pm2 start yarn --name backend -- run backend` आदि।

5. **एक्सेस**: `http://localhost:3080`। अकाउंट बनाएं और कॉन्फ़िगर करें।

- **डेटा**: MongoDB `/var/lib/mongodb` में स्टोर करता है, Meili `/var/lib/meilisearch` में।
- **समस्या निवारण**:
  - Mongo ऑथ: `mongo` चलाएं और यूजर बनाएं: `use LibreChat; db.createUser({user: 'librechat', pwd: 'yourpass', roles: ['readWrite']})`।
  - पोर्ट्स/फायरवॉल: `sudo ufw allow 3080,3090,7700`।
  - अपडेट्स: `git pull && yarn install && सर्विसेज रीस्टार्ट करें`।
- **फायदे**: बैंडविड्थ पर हल्का (कोई कंटेनर्स नहीं), सिस्टम रिसोर्सेज का सीधा इस्तेमाल करता है। नुकसान: सेटअप में ज्यादा झंझट, संभावित डिपेंडेंसी कॉन्फ्लिक्ट्स (जैसे, आपके Python 3.13 के साथ, लेकिन Node अलग है)।

अगर मोबाइल डेटा बेहद सीमित है, तो गैर-डॉकर तरीका सबसे अच्छा है—इसे चरणों में करें, डायरेक्टरीज पर `du -sh` से मॉनिटरिंग करते हुए। एरर के लिए, लॉग्स शेयर करें (जैसे, `yarn run backend` से)। ऑफिशियल गैर-डॉकर गाइड: https://docs.librechat.ai/install/installation/manual_install.html। अगर आपको लोकल AI के लिए Ollama इंटीग्रेशन चाहिए (API कॉस्ट बचाता है), तो इसे अलग से उनके स्क्रिप्ट के जरिए इंस्टॉल करें (~100MB)। ट्वीक्स के लिए बताएं!