---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: डॉकर रजिस्ट्री कनेक्शन टाइमआउट समस्या निवारण
translated: true
type: note
---

आपको यह त्रुटि मिल रही है, `Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)`, जो दर्शाती है कि Docker क्लाइंट, Docker Hub registry से कनेक्ट नहीं हो पाया है क्योंकि टाइमआउट हो गया। यह नेटवर्क समस्याओं, प्रमाणीकरण (authentication) समस्याओं, या कॉन्फ़िगरेशन त्रुटियों के कारण हो सकता है। चूंकि आप वेब-आधारित लॉगिन का प्रयास कर रहे हैं, आइए चरणबद्ध तरीके से इस समस्या का निवारण और समाधान करें।

### समस्या को हल करने के चरण

1. **नेटवर्क कनेक्टिविटी सत्यापित करें**
   - सुनिश्चित करें कि आपका इंटरनेट कनेक्शन स्थिर है।
   - Docker Hub से कनेक्टिविटी का परीक्षण करने के लिए चलाएँ:
     ```bash:disable-run
     ping registry-1.docker.io
     ```
     या
     ```bash
     curl -v https://registry-1.docker.io/v2/
     ```
     यदि ये विफल होते हैं, तो आपको नेटवर्क समस्या (जैसे फ़ायरवॉल, प्रॉक्सी, या DNS समस्याएं) हो सकती है।

2. **वेब-आधारित प्रमाणीकरण जांचें**
   - संदेश इंगित करता है कि आप एक बार-उपयोग वाला डिवाइस पुष्टिकरण कोड (`LVFK-KCQX`) का उपयोग कर रहे हैं। सुनिश्चित करें कि आप:
     - ब्राउज़र खोलने के लिए `ENTER` दबाया है या मैन्युअल रूप से `https://login.docker.com/activate` पर गए हैं।
     - कोड ब्राउज़र में सही ढंग से दर्ज किया है।
     - ब्राउज़र में प्रमाणीकरण प्रक्रिया को टाइमआउट अवधि के भीतर पूरा किया है।
   - यदि ब्राउज़र स्वचालित रूप से नहीं खुला, तो मैन्युअल रूप से URL पर जाएं और कोड इनपुट करें।
   - यदि प्रमाणीकरण विफल हो जाता है या टाइमआउट हो जाता है, तो प्रक्रिया को पुनः आरंभ करने का प्रयास करें:
     ```bash
     docker login
     ```

3. **टाइमआउट समस्याओं को संभालें**
   - टाइमआउट त्रुटि बताती है कि Docker क्लाइंट registry से कनेक्ट नहीं हो पाया। `DOCKER_CLIENT_TIMEOUT` environment variable सेट करके टाइमआउट बढ़ाएँ:
     ```bash
     export DOCKER_CLIENT_TIMEOUT=120
     export COMPOSE_HTTP_TIMEOUT=120
     docker login
     ```
     यह टाइमआउट को 120 सेकंड तक बढ़ा देता है।

4. **प्रॉक्सी या फ़ायरवॉल समस्याओं की जांच करें**
   - यदि आप प्रॉक्सी के पीछे हैं, तो Docker को इसका उपयोग करने के लिए कॉन्फ़िगर करें। `~/.docker/config.json` को संपादित करें या बनाएं और जोड़ें:
     ```json
     {
       "proxies": {
         "default": {
           "httpProxy": "http://<proxy-host>:<proxy-port>",
           "httpsProxy": "https://<proxy-host>:<proxy-port>",
           "noProxy": "localhost,127.0.0.1"
         }
       }
     }
     ```
     `<proxy-host>` और `<proxy-port>` को अपने प्रॉक्सी विवरण से बदलें।
   - यदि कोई फ़ायरवॉल एक्सेस को ब्लॉक कर रहा है, तो सुनिश्चित करें कि `registry-1.docker.io` और `login.docker.com` की अनुमति है।

5. **क्रेंडेंशियल हेल्पर का उपयोग करें (वैकल्पिक लेकिन अनुशंसित)**
   - `~/.docker/config.json` में अनएन्क्रिप्टेड क्रेडेंशियल्स के बारे में चेतावनी एक क्रेंडेंशियल हेल्पर सेट अप करने का सुझाव देती है। `docker-credential-pass` या `docker-credential-secretservice` जैसे क्रेंडेंशियल हेल्पर इंस्टॉल करें:
     - Linux के लिए `pass` के साथ:
       ```bash
       sudo apt-get install pass
       curl -fsSL https://github.com/docker/docker-credential-helpers/releases/download/v0.7.0/docker-credential-pass-v0.7.0-amd64.tar.gz | tar -xz
       sudo mv docker-credential-pass /usr/local/bin/
       ```
       `pass` को इनिशियलाइज़ करें:
       ```bash
       gpg2 --gen-key
       pass init <your-gpg-key-id>
       ```
       हेल्पर का उपयोग करने के लिए `~/.docker/config.json` अपडेट करें:
       ```json
       {
         "credsStore": "pass"
       }
       ```
     - क्रेंडेंशियल हेल्पर को कॉन्फ़िगर करने के बाद लॉगिन पुनः प्रयास करें।

6. **कमांड-लाइन लॉगिन का विकल्प**
   - यदि वेब-आधारित लॉगिन विफल रहता है, तो अपने Docker Hub यूज़रनेम और पासवर्ड के साथ कमांड-लाइन लॉगिन आज़माएँ:
     ```bash
     docker login -u <your-username>
     ```
     जब संकेत मिले, तो अपना पासवर्ड या एक Personal Access Token (PAT) दर्ज करें। आप अपनी Docker Hub अकाउंट सेटिंग्स से एक PAT जनरेट कर सकते हैं।

7. **Docker डेमन स्थिति जांचें**
   - सुनिश्चित करें कि Docker डेमन चल रहा है:
     ```bash
     sudo systemctl status docker
     ```
     यदि यह नहीं चल रहा है, तो इसे शुरू करें:
     ```bash
     sudo systemctl start docker
     ```

8. **Docker कॉन्फ़िगरेशन साफ़ करें (अंतिम उपाय)**
   - यदि समस्या बनी रहती है, तो Docker कॉन्फ़िगरेशन फ़ाइल को साफ़ करें और पुनः प्रयास करें:
     ```bash
     mv ~/.docker/config.json ~/.docker/config.json.bak
     docker login
     ```

### अतिरिक्त नोट्स
- **Docker Hub स्थिति**: जांचें कि क्या Docker Hub में कोई आउटेज है, `https://status.docker.com/` पर जाकर।
- **DNS समस्याएं**: यदि `registry-1.docker.io` रिज़ॉल्व नहीं होता है, तो अपनी नेटवर्क सेटिंग्स में Google (`8.8.8.8`) या Cloudflare (`1.1.1.1`) जैसे पब्लिक DNS का उपयोग करने का प्रयास करें।
- **Docker वर्जन**: सुनिश्चित करें कि आपका Docker क्लाइंट अप-टू-डेट है:
  ```bash
  docker --version
  ```
  अपने OS के लिए निर्देशों का पालन करते हुए, यदि आवश्यक हो तो Docker को अपडेट करें।

### संदर्भ
- [Docker Credential Store Documentation](https://docs.docker.com/go/credential-store/)
- [Docker Login Documentation](https://docs.docker.com/engine/reference/commandline/login/)
- [Docker Hub Status](https://status.docker.com/)