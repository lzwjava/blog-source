---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: उबुन्टू पर लिबरेचैट स्थापित करना
translated: true
type: note
---

### Ubuntu 24.04 LTS पर LibreChat इंस्टॉल करना

LibreChat एक ओपन-सोर्स AI चैट प्लेटफॉर्म है जो वेब इंटरफेस के माध्यम से कई AI मॉडल्स (जैसे, OpenAI, Gemini, Ollama) को सपोर्ट करता है। अनुशंसित इंस्टॉलेशन विधि Docker Compose का उपयोग करना है, क्योंकि यह सरल है, MongoDB और MeiliSearch जैसी डिपेंडेंसी को स्वचालित रूप से हैंडल करता है, और Ubuntu पर विश्वसनीय रूप से काम करता है। आपका सिस्टम (Ubuntu 24.04.2 LTS with Python 3.13.4) आवश्यकताओं को पूरा करता है, लेकिन आपको पहले Docker और Git इंस्टॉल करने की आवश्यकता होगी।

#### पूर्वापेक्षाएँ
1. **अपने सिस्टम को अपडेट करें**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **Git इंस्टॉल करें** (अगर पहले से इंस्टॉल नहीं है):
   ```
   sudo apt install git -y
   ```

3. **Docker और Docker Compose इंस्टॉल करें**:
   - Docker इंस्टॉल करें:
     ```
     sudo apt install docker.io -y
     sudo systemctl start docker
     sudo systemctl enable docker
     sudo usermod -aG docker $USER
     ```
     ग्रुप परिवर्तनों के प्रभावी होने के लिए लॉग आउट करें और वापस लॉग इन करें (या `newgrp docker` चलाएँ)।
   - Docker Compose (नवीनतम वर्जन) इंस्टॉल करें:
     ```
     sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```
     `docker-compose --version` से वेरिफाई करें।

#### इंस्टॉलेशन चरण
1. **LibreChat रिपॉजिटरी को क्लोन करें**:
   ```
   cd ~/projects  # या आपका पसंदीदा डायरेक्टरी
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **एनवायरनमेंट फ़ाइल को कॉपी और कॉन्फ़िगर करें**:
   - उदाहरण फ़ाइल को कॉपी करें:
     ```
     cp .env.example .env
     ```
   - एक टेक्स्ट एडिटर (जैसे, `nano .env`) के साथ `.env` को एडिट करें। अपडेट करने के लिए मुख्य सेटिंग्स:
     - एक MongoDB मास्टर की सेट करें: एक मजबूत पासवर्ड जनरेट करें और `MONGODB_URI=mongodb://mongodb:27017/LibreChat?authSource=admin` और `MONGODB_MASTER_KEY=your_generated_key_here` सेट करें।
     - MeiliSearch के लिए: `MEILI_MASTER_KEY=your_generated_key_here` सेट करें (एक मजबूत की जनरेट करें)।
     - अगर जरूरत हो तो AI API कीज एड करें (जैसे, `OPENAI_API_KEY=your_openai_key`)। लोकल मॉडल्स जैसे Ollama के लिए, शुरुआत में कोई की जरूरत नहीं है।
     - सेव करें और बाहर निकलें। पूर्ण कॉन्फ़िग विकल्पों के लिए, डॉक्स देखें।

3. **Docker Compose के साथ LibreChat शुरू करें**:
   ```
   docker-compose up -d
   ```
   - यह इमेजेज को पुल करता है, सर्विसेज (LibreChat ऐप, MongoDB, MeiliSearch) को शुरू करता है, और डिटैच्ड मोड में चलाता है।
   - इसके पूरी तरह से शुरू होने का इंतजार करें (`docker-compose logs -f` से चेक करें)।

4. **LibreChat एक्सेस करें**:
   - अपना ब्राउज़र खोलें और `http://localhost:3080` पर जाएँ।
   - लॉगिन पेज पर एक अकाउंट बनाएँ।
   - एक AI मॉडल चुनें (सेटिंग्स में एंडपॉइंट्स कॉन्फ़िगर करें) और चैटिंग शुरू करें।

#### पोस्ट-इंस्टॉलेशन टिप्स
- **रोकना/अपडेट करना**: रोकने के लिए `docker-compose down` चलाएँ, फिर अपडेट करने के लिए `git pull` और `docker-compose up -d --build` चलाएँ।
- **डेटा परसिस्टेंस**: MongoDB डेटा के लिए वॉल्यूम स्वचालित रूप से बनाए जाते हैं (`./data/mongodb` में)।
- **समस्या निवारण**:
  - अगर पोर्ट्स कॉन्फ्लिक्ट करते हैं, तो `3080:3080` को बदलने के लिए `docker-compose.yml` को एडिट करें।
  - हेडलेस/सर्वर एक्सेस के लिए, अपने सर्वर के IP का उपयोग करें (जैसे, `http://your-server-ip:3080`) और सुनिश्चित करें कि फ़ायरवॉल पोर्ट 3080 की अनुमति देता है (`sudo ufw allow 3080`)।
  - अगर लोकल LLMs का उपयोग कर रहे हैं, तो Ollama को अलग से इंस्टॉल करें और इसे `.env` में एक एंडपॉइंट के रूप में एड करें।
- **वैकल्पिक: NPM विधि** (Docker के बिना): अगर आप पसंद करते हैं, तो Node.js 18+, Yarn, MongoDB, और MeiliSearch को मैन्युअली इंस्टॉल करें, फिर `yarn install` और `yarn run frontend` + `yarn run backend` चलाएँ। लेकिन सरलता के लिए Docker की दृढ़ता से अनुशंसा की जाती है।

यह आपको जल्दी से चलनशील स्थिति में ले आएगा। अगर आपको कोई त्रुटियाँ मिलती हैं, तो और मदद के लिए आउटपुट साझा करें!

[LibreChat ऑफिशियल डॉक्स](https://docs.librechat.ai/install/installation/docker_compose.html)  
[Ubuntu Docker गाइड](https://docs.librechat.ai/install/installation/docker_ubuntu.html)  
[It's FOSS ट्यूटोरियल](https://itsfoss.com/librechat-linux/)