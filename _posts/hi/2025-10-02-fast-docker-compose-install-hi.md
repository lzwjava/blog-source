---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: तेज़ डॉकर कंपोज़ इंस्टालेशन विधियाँ
translated: true
type: note
---

### Ubuntu पर Docker Compose डाउनलोड/इंस्टॉल करने के तेज़ वैकल्पिक तरीके

मान लीजिए कि आप GitHub रिलीज़ पेज की पूरी परेशानी (जैसे, मैन्युअल curl + sha256 सत्यापन) के बिना नवीनतम Docker Compose बाइनरी (अक्टूबर 2025 तक, आधिकारिक डॉक्स के अनुसार वर्तमान में v2.37.3) जल्दी से प्राप्त करना चाहते हैं, तो यहां विश्वसनीय, तेज़ विकल्प दिए गए हैं। ये Ubuntu के पैकेज मैनेजर या Docker के रेपो का लाभ उठाते हैं जो लगभग तत्काल इंस्टॉलेशन प्रदान करते हैं। मैं गति और सरलता को प्राथमिकता दूंगा—अधिकांश 1 मिनट से भी कम समय लेते हैं।

#### 1. **Ubuntu APT के माध्यम से (अधिकांश उपयोगकर्ताओं के लिए सबसे तेज़)**
   यदि आपने Docker इंस्टॉल किया है (जिसमें `docker-compose-plugin` शामिल है), तो बस सबकमांड का उपयोग करें—अलग से बाइनरी डाउनलोड करने की आवश्यकता नहीं है। यह आधुनिक, एकीकृत तरीका है और बाइनरी प्रबंधन से बचाता है।

   - **जांचें कि क्या पहले से उपलब्ध है**:
     ```
     docker compose version
     ```
     यदि यह v2.x दिखाता है, तो आपका काम हो गया—यह आपके Docker इंस्टॉल के माध्यम से नवीनतम है।

   - **आवश्यकता होने पर इंस्टॉल/अपडेट करें** (गायब होने पर प्लगइन जोड़ता है):
     ```
     sudo apt update
     sudo apt install docker-compose-plugin
     ```
     - **यह तेज़ क्यों है?** GitHub ट्रैफिक नहीं; स्थानीय रेपो का उपयोग करता है। `apt upgrade` के साथ स्वचालित रूप से अपडेट हो जाता है।
     - **उपयोग**: `docker compose up` के रूप में चलाएं (ध्यान दें: हाइफन नहीं, स्पेस है)।
     - **प्रो टिप**: यदि Docker अभी तक इंस्टॉल नहीं किया गया है, तो पहले Docker का रेपो जोड़ें:
       ```
       sudo apt update
       sudo apt install ca-certificates curl
       sudo install -m 0755 -d /etc/apt/keyrings
       sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
       sudo chmod a+r /etc/apt/keyrings/docker.asc
       echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       sudo apt update
       sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
       ```

#### 2. **GitHub से वन-लाइन Curl (फुल रिलीज़ की तुलना में थोड़ा तेज़)**
   रिलीज़ पेज ब्राउज़ करना छोड़ दें—curl सीधे नवीनतम Linux x86_64 बाइनरी प्राप्त करता है और इसे इंस्टॉल करता है। यह मैन्युअल एसेट चयन की तुलना में तेज़ है लेकिन फिर भी GitHub का उपयोग करता है।

   ```
   VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4) && sudo curl -L "https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version
   ```
   - **यह तेज़ क्यों है?** API सेकंडों में वर्जन फ़ेच करता है; सिंगल कमांड डाउनलोड + इंस्टॉल को संभालता है।
   - **सत्यापित करें**: अंत में `--version` इसकी पुष्टि करता है।
   - **नोट**: विशेष रूप से v2.39.4 के लिए, `${VERSION}` को `v2.39.4` से बदलें।

#### 3. **Snap के माध्यम से (Ubuntu का यूनिवर्सल पैकेज मैनेजर)**
   Snap Ubuntu 24.04 पर पहले से इंस्टॉल रहता है और Canonical के स्टोर से नवीनतम वर्जन तुरंत खींचता है।

   ```
   sudo snap install docker
   ```
   - **यह तेज़ क्यों है?** रेपो सेटअप की आवश्यकता नहीं; समानांतर में डाउनलोड करता है और स्वचालित रूप से अपडेट हो जाता है। इसमें Compose प्लगइन शामिल है।
   - **उपयोग**: APT विधि के समान (`docker compose`)।
   - **वर्जन जांचें**: `docker compose version`।

#### 4. **Pip के माध्यम से (चूंकि आपके पास Python 3.13.4 है)**
   यदि आप Python-आधारित पसंद करते हैं (लेगेसी v1 स्टाइल, लेकिन pip में v2 रैपर हैं), तो यह सिस्टम डिपेंडेंसी के बिना एक त्वरित इंस्टॉलेशन है।

   ```
   sudo pip3 install docker-compose
   ```
   - **यह तेज़ क्यों है?** Pip कैश करता है और डिपेंडेंसी को तेजी से रिज़ॉल्व करता है; GitHub शामिल नहीं है।
   - **सीमा**: यह v1 कम्पैटिबिलिटी के लिए अधिक है—आधिकारिक v2 प्लगइन के लिए APT का उपयोग करें।
   - **सत्यापित करें**: `docker-compose --version` (हाइफनेटेड)।

ये सभी विधियां GitHub के UI की तुलना में तेज़ हैं क्योंकि वे क्लिक्स को कम से कम करती हैं या APIs/कैश का उपयोग करती हैं। Ubuntu के लिए APT या Snap मेरी शीर्ष सिफारिशें हैं—वे सहजता से एकीकृत होते हैं और अपडेट को संभालते हैं। यदि आपका "docker compose down" से कुछ और मतलब था (जैसे, कमांड स्वयं), तो स्पष्ट करें!

[आधिकारिक Docker Compose इंस्टॉल गाइड](https://docs.docker.com/compose/install/linux/)  
[Docker रिलीज़ेज़](https://github.com/docker/compose/releases)