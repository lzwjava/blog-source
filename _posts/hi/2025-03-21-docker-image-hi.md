---
audio: false
generated: true
lang: hi
layout: post
title: डॉकर इमेज का निर्माण और तैनाती
translated: true
type: note
---

यहाँ एक Spring Boot एप्लिकेशन को Docker इमेज में बनाने और सर्वर पर डिप्लॉय करने के लिए चरण-दर-चरण मार्गदर्शिका दी गई है:

### आवश्यक शर्तें
1. **Java** (उदाहरण के लिए, JDK 17 या संगत संस्करण) स्थानीय रूप से इंस्टॉल होना चाहिए।
2. **Maven** या **Gradle** (आपके Spring Boot प्रोजेक्ट सेटअप के आधार पर)।
3. **Docker** आपके स्थानीय मशीन और सर्वर पर इंस्टॉल होना चाहिए।
4. **एक Spring Boot प्रोजेक्ट** कंटेनराइज करने के लिए तैयार होना चाहिए।
5. **सर्वर एक्सेस** (उदाहरण के लिए, SSH के माध्यम से) जिसमें Docker इंस्टॉल हो।

---

### चरण 1: अपने Spring Boot एप्लिकेशन को तैयार करें
सुनिश्चित करें कि आपका Spring Boot एप्लिकेशन स्थानीय रूप से काम कर रहा है। इसके साथ टेस्ट करें:
```bash
mvn spring-boot:run  # अगर Maven का उपयोग कर रहे हैं
# या
gradle bootRun       # अगर Gradle का उपयोग कर रहे हैं
```

सुनिश्चित करें कि एप्लिकेशन सफलतापूर्वक बिल्ड होता है:
```bash
mvn clean package    # Maven
# या
gradle build         # Gradle
```
यह एक `.jar` फ़ाइल (उदाहरण के लिए, `target/myapp-1.0.0.jar`) जनरेट करता है।

---

### चरण 2: एक Dockerfile बनाएँ
अपने प्रोजेक्ट की रूट डायरेक्टरी में (जहाँ `.jar` फ़ाइल स्थित है), निम्नलिखित कंटेंट के साथ `Dockerfile` नामक एक फ़ाइल बनाएँ:

```dockerfile
# बेस इमेज के रूप में एक ऑफिशियल OpenJDK रनटाइम का उपयोग करें
FROM openjdk:17-jdk-slim

# कंटेनर के अंदर वर्किंग डायरेक्टरी सेट करें
WORKDIR /app

# Spring Boot JAR फ़ाइल को कंटेनर में कॉपी करें
COPY target/myapp-1.0.0.jar app.jar

# वह पोर्ट एक्सपोज़ करें जिस पर आपका Spring Boot ऐप चलता है (डिफ़ॉल्ट 8080 है)
EXPOSE 8080

# JAR फ़ाइल को रन करें
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**नोट्स:**
- `myapp-1.0.0.jar` को आपकी JAR फ़ाइल के वास्तविक नाम से बदलें।
- Java संस्करण (`openjdk:17-jdk-slim`) को एडजस्ट करें अगर आपका ऐप अलग वर्जन का उपयोग करता है।

---

### चरण 3: Docker इमेज बनाएँ
`Dockerfile` वाली डायरेक्टरी से, रन करें:
```bash
docker build -t myapp:latest .
```
- `-t myapp:latest` इमेज को `myapp` नाम और `latest` वर्जन के साथ टैग करता है।
- `.` Docker को बिल्ड कॉन्टेक्स्ट के लिए करंट डायरेक्टरी का उपयोग करने के लिए कहता है।

इमेज बन गई है यह सत्यापित करें:
```bash
docker images
```

---

### चरण 4: Docker इमेज को स्थानीय रूप से टेस्ट करें
यह सुनिश्चित करने के लिए कंटेनर को स्थानीय रूप से रन करें कि यह काम करता है:
```bash
docker run -p 8080:8080 myapp:latest
```
- `-p 8080:8080` आपकी मशीन पर पोर्ट 8080 को कंटेनर के पोर्ट 8080 से मैप करता है।
- टेस्ट करने के लिए ब्राउज़र खोलें या `curl` का उपयोग करें (उदाहरण के लिए, `curl http://localhost:8080`)।

कंटेनर को `Ctrl+C` से रोकें या इसकी ID `docker ps` से ढूंढकर रोकें:
```bash
docker stop <container-id>
```

---

### चरण 5: इमेज को एक Docker रजिस्ट्री में पुश करें (ऑप्शनल)
सर्वर पर डिप्लॉय करने के लिए, आपको इमेज को Docker Hub (या एक प्राइवेट रजिस्ट्री) जैसी रजिस्ट्री में पुश करना होगा। अगर आप इसे स्किप करते हैं, तो आपको इमेज को मैन्युअली ट्रांसफर करना होगा।

1. Docker Hub में लॉग इन करें:
   ```bash
   docker login
   ```
2. अपनी इमेज को टैग करें:
   ```bash
   docker tag myapp:latest yourusername/myapp:latest
   ```
3. इमेज को पुश करें:
   ```bash
   docker push yourusername/myapp:latest
   ```

---

### चरण 6: सर्वर पर डिप्लॉय करें
#### विकल्प 1: रजिस्ट्री का उपयोग करके
1. अपने सर्वर में SSH करें:
   ```bash
   ssh user@server-ip
   ```
2. इमेज को पुल करें:
   ```bash
   docker pull yourusername/myapp:latest
   ```
3. कंटेनर को रन करें:
   ```bash
   docker run -d -p 8080:8080 yourusername/myapp:latest
   ```
   - `-d` कंटेनर को डिटैच्ड मोड (बैकग्राउंड) में रन करता है।

#### विकल्प 2: मैन्युअल ट्रांसफर
अगर आपने रजिस्ट्री का उपयोग नहीं किया है:
1. इमेज को स्थानीय रूप से एक `.tar` फ़ाइल के रूप में सेव करें:
   ```bash
   docker save -o myapp.tar myapp:latest
   ```
2. इसे सर्वर पर ट्रांसफर करें (उदाहरण के लिए, SCP के माध्यम से):
   ```bash
   scp myapp.tar user@server-ip:/path/to/destination
   ```
3. सर्वर में SSH करें:
   ```bash
   ssh user@server-ip
   ```
4. इमेज को लोड करें:
   ```bash
   docker load -i myapp.tar
   ```
5. कंटेनर को रन करें:
   ```bash
   docker run -d -p 8080:8080 myapp:latest
   ```

---

### चरण 7: डिप्लॉयमेंट सत्यापित करें
जांचें कि कंटेनर चल रहा है या नहीं:
```bash
docker ps
```

सर्वर से या बाहरी रूप से ऐप को टेस्ट करें:
- अगर सर्वर पर है: `curl http://localhost:8080`
- अगर बाहरी है: सर्वर के IP का उपयोग करें (उदाहरण के लिए, `http://server-ip:8080`), यह सुनिश्चित करते हुए कि पोर्ट सर्वर के फ़ायरवॉल में ओपन है।

---

### ऑप्शनल: एन्हांसमेंट्स
- **एनवायरनमेंट वेरिएबल्स**: अपने ऐप को कॉन्फ़िग पास करें:
  ```bash
  docker run -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=prod" myapp:latest
  ```
- **Docker Compose**: मल्टी-कंटेनर सेटअप्स के लिए, एक `docker-compose.yml` फ़ाइल का उपयोग करें।
- **रिस्टार्ट पॉलिसी**: यह सुनिश्चित करने के लिए कि कंटेनर सर्वर रिबूट पर रिस्टार्ट हो जाए, `--restart unless-stopped` ऐड करें।

मुझे बताएं अगर आपको किसी विशेष भाग में मदद की आवश्यकता है!

---

आपके द्वारा प्रदान किए गए एरर आउटपुट से, आपकी `docker build` कमांड को सफल होने से रोकने वाले कुछ मुद्दे सामने आए हैं। आइए उन्हें तोड़ते हैं और चरण-दर-चरण हल करते हैं।

---

### पहचाने गए मुद्दे
1. **`docker-buildx` प्लगइन गुम है**
   एरर: `fork/exec /Users/lzwjava/.docker/cli-plugins/docker-buildx: no such file or directory`
   इससे पता चलता है कि Docker आधुनिक बिल्ड टूल `buildx` प्लगइन का उपयोग करने का प्रयास कर रहा है, लेकिन यह इंस्टॉल या कॉन्फ़िगर नहीं है।

2. **लेगेसी बिल्डर डिप्रिकेशन वार्निंग**
   वार्निंग: `DEPRECATED: The legacy builder is deprecated...`
   Docker BuildKit (`buildx`) पर स्विच करने की सलाह देता है, लेकिन यह लेगेसी बिल्डर पर फॉल बैक कर रहा है, जो फेल हो रहा है।

3. **Docker डेमन नहीं चल रहा है**
   एरर: `Cannot connect to the Docker daemon at unix:///Users/lzwjava/.docker/run/docker.sock. Is the docker daemon running?`
   Docker डेमन (बैकग्राउंड सर्विस जो कंटेनर्स को मैनेज करती है) आपके सिस्टम पर नहीं चल रही है।

4. **फ़ाइल एक्सेस एरर्स**
   एरर्स: `Can't add file ... to tar: io: read/write on closed pipe` और `Can't close tar writer...`
   ये सेकेंडरी मुद्दे हैं जो डेमन न चलने के कारण बिल्ड प्रक्रिया के फेल होने से उत्पन्न हुए हैं।

5. **प्रॉक्सी सेटिंग्स का पता चला**
   आपका सिस्टम प्रॉक्सी (`HTTP_PROXY` और `HTTPS_PROXY`) का उपयोग कर रहा है। यह Docker में हस्तक्षेप कर सकता है अगर ठीक से कॉन्फ़िगर नहीं किया गया है।

---

### चरण-दर-चरण फिक्स

#### 1. सत्यापित करें कि Docker डेमन चल रहा है
मुख्य मुद्दा यह है कि Docker डेमन नहीं चल रही है। इसे ठीक करने का तरीका यहाँ बताया गया है:

- **macOS पर** (मानते हुए कि आप Docker Desktop का उपयोग कर रहे हैं):
  1. अपने एप्लिकेशन फ़ोल्डर या स्पॉटलाइट से Docker Desktop खोलें।
  2. सुनिश्चित करें कि यह चल रहा है (आपको मेनू बार में Docker व्हेल आइकन हरा दिखाई देगा)।
  3. अगर यह स्टार्ट नहीं हो रहा है:
     - Docker Desktop को बंद करें और पुनरारंभ करें।
     - अपडेट के लिए जांचें: Docker Desktop > Check for Updates.
     - अगर फिर भी फेल होता है, तो [docker.com](https://www.docker.com/products/docker-desktop/) से Docker Desktop को पुनः इंस्टॉल करें।

- **टर्मिनल के माध्यम से जांचें**:
  रन करें:
  ```bash
  docker info
  ```
  अगर डेमन चल रही है, तो आपको सिस्टम जानकारी दिखाई देगी। अगर नहीं, तो आपको वही "Cannot connect" एरर मिलेगा।

- **डेमन को मैन्युअली रीस्टार्ट करें** (अगर जरूरत हो):
  ```bash
  sudo launchctl stop com.docker.docker
  sudo launchctl start com.docker.docker
  ```

एक बार डेमन चलने के बाद, अगले चरणों के लिए आगे बढ़ें।

---

#### 2. `buildx` प्लगइन इंस्टॉल करें (ऑप्शनल लेकिन रिकमेंडेड)
चूंकि लेगेसी बिल्डर डिप्रिकेटेड है, आइए `buildx` सेट अप करें:

1. **`buildx` इंस्टॉल करें**:
   - बाइनरी को मैन्युअली डाउनलोड करें या Docker के निर्देशों का उपयोग करें:
     ```bash
     mkdir -p ~/.docker/cli-plugins
     curl -SL https://github.com/docker/buildx/releases/download/v0.13.0/buildx-v0.13.0.darwin-amd64 -o ~/.docker/cli-plugins/docker-buildx
     chmod +x ~/.docker/cli-plugins/docker-buildx
     ```
     (अपने OS/आर्किटेक्चर के लिए [latest release](https://github.com/docker/buildx/releases) चेक करें, उदाहरण के लिए, M1/M2 Macs के लिए `darwin-arm64`।)

2. **इंस्टॉलेशन सत्यापित करें**:
   ```bash
   docker buildx version
   ```

3. **BuildKit को डिफ़ॉल्ट के रूप में सेट करें** (ऑप्शनल):
   इसे `~/.docker/config.json` में ऐड करें:
   ```json
   {
     "features": { "buildkit": true }
   }
   ```

वैकल्पिक रूप से, आप इसे स्किप कर सकते हैं और अभी के लिए लेगेसी बिल्डर का उपयोग कर सकते हैं (चरण 4 देखें)।

---

#### 3. प्रॉक्सी सेटिंग्स को हैंडल करें
आपकी प्रॉक्सी सेटिंग्स (`http://127.0.0.1:7890`) Docker की इमेज फ़ेच करने की क्षमता में हस्तक्षेप कर सकती हैं। Docker को उनका उपयोग करने के लिए कॉन्फ़िगर करें:

1. **Docker Desktop के माध्यम से**:
   - Docker Desktop > Settings > Resources > Proxies खोलें।
   - "Manual proxy configuration" सक्षम करें और दर्ज करें:
     - HTTP Proxy: `http://127.0.0.1:7890`
     - HTTPS Proxy: `http://127.0.0.1:7890`
   - Apply & Restart करें।

2. **CLI के माध्यम से** (अगर Desktop का उपयोग नहीं कर रहे हैं):
   `~/.docker/config.json` बनाएं या एडिट करें:
   ```json
   {
     "proxies": {
       "default": {
         "httpProxy": "http://127.0.0.1:7890",
         "httpsProxy": "http://127.0.0.1:7890"
       }
     }
   }
   ```
   एडिट करने के बाद Docker को रीस्टार्ट करें।

---

#### 4. बिल्ड को फिर से आजमाएँ
अब जब डेमन चल रही है और प्रॉक्सी कॉन्फ़िगर हो गए हैं, बिल्ड को फिर से आजमाएँ:

```bash
docker build -t myapp:latest .
```

- अगर आपने `buildx` इंस्टॉल किया है, तो यह डिफ़ॉल्ट रूप से BuildKit का उपयोग करेगा।
- अगर आपने `buildx` स्किप किया है, तो लेगेसी बिल्डर को फोर्स करने के लिए `--progress=plain` ऐड करें:
  ```bash
  docker build --progress=plain -t myapp:latest .
  ```

---

#### 5. `.git/hooks` एरर का ट्रबलशूट करें (अगर बना रहता है)
`.git/hooks/pre-rebase.sample` एरर से पता चलता है कि Docker बिल्ड कॉन्टेक्स्ट में अनावश्यक फ़ाइलों को शामिल करने का प्रयास कर रहा है। उन्हें `.dockerignore` फ़ाइल के साथ एक्सक्लूड करें:

1. अपने `Dockerfile` वाली ही डायरेक्टरी में `.dockerignore` बनाएँ:
   ```
   .git
   .gitignore
   *.md
   target/*
   !target/*.jar
   ```
2. यह Docker को `.git` फ़ोल्डर और `target/` में हर चीज़ को इग्नोर करने के लिए कहता है, सिवाय आपकी JAR फ़ाइल के।

3. बिल्ड को फिर से आजमाएँ:
   ```bash
   docker build -t myapp:latest .
   ```

---

### अंतिम सत्यापन
- इमेज की जांच करें:
  ```bash
  docker images
  ```
- इसे स्थानीय रूप से रन करें:
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```
- `curl http://localhost:8080` के साथ टेस्ट करें।

---

### अगले कदम
एक बार इमेज सफलतापूर्वक बन जाने के बाद, मेरी पिछली प्रतिक्रिया से डिप्लॉयमेंट चरणों का पालन करें (उदाहरण के लिए, रजिस्ट्री में पुश करें या सर्वर पर ट्रांसफर करें)। मुझे बताएं अगर आपको कोई और समस्या आती है!