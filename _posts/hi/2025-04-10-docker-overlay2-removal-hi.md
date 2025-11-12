---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: डॉकर ओवरले 2 हटाने की त्रुटियों का समाधान
translated: true
type: note
---

उस त्रुटि का मतलब है कि Docker कंटेनर की overlay2 फाइलसिस्टम को हटाने में विफल रहा — कर्नेल/VM ने एक निम्न-स्तरीय I/O त्रुटि वापस की (`readdirent merged: bad message`)। macOS पर यह आमतौर पर तब होता है जब Docker VM या ओवरले स्टोरेज खराब स्थिति में होती है। नीचे सुरक्षित, क्रमबद्ध चरण दिए गए हैं (कम विनाशकारी → अधिक आक्रामक) जिन्हें आप पुनर्प्राप्त करने के लिए आजमा सकते हैं।

**महत्वपूर्ण:** नीचे दिए गए कुछ कमांड डेटा (images/volumes) हटा सकते हैं। मैं विनाशकारी चरणों को चिह्नित करूंगा और सटीक कमांड दिखाऊंगा ताकि आप चाहें तो कॉपी/पेस्ट कर सकें।

---

# त्वरित जांचें (सुरक्षित)

एक टर्मिनल में, चलाएँ:

```bash
# कंटेनर स्थिति और समस्या वाला कंटेनर id दिखाएँ
docker ps -a --no-trunc | grep ccd89a3f36a1528cb923c90de8755faeb36e229c || true

# कंटेनर को जबरन हटाने का प्रयास करें
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

यदि `docker rm -f` सफल होता है, तो आपका काम पूरा हुआ। यदि यह उसी ओवरले त्रुटि के साथ विफल रहता है, तो जारी रखें।

---

# Docker रीस्टार्ट करें (macOS Docker Desktop) — अनुशंसित अगला कदम (सुरक्षित)

Docker Desktop को पूरी तरह से बंद करें (व्हेल आइकन का उपयोग करें → Quit) और फिर इसे फिर से शुरू करें। या कमांड लाइन से:

```bash
# macOS — AppleScript के माध्यम से Docker Desktop को रीस्टार्ट करें
osascript -e 'quit app "Docker"'
open -a Docker
```

Docker के रीस्टार्ट होने के बाद, फिर से `docker compose down` या `docker rm -f <id>` आज़माएं।

---

# होस्ट को रीस्टार्ट करें (बहुत सुरक्षित)

यदि रीस्टार्ट संभव है, तो macOS को रीबूट करने से अक्सर VM फाइलसिस्टम समस्याएं दूर हो जाती हैं:

* Mac को रीबूट करें, फिर Docker Desktop शुरू करें और पुनः प्रयास करें।

---

# यदि अभी भी विफल हो रहा है — Docker Desktop Troubleshoot कार्यों का उपयोग करें (सुरक्षित / मध्यम)

Docker Desktop → Troubleshoot खोलें:

* **Restart Docker** पर क्लिक करें (यदि आपने पहले से नहीं किया है)।
* यदि यह विफल रहता है, तो **Clean / Purge data** या **Reset to factory defaults** आज़माएं — **चेतावनी**: ये images/containers/volumes हटा देते हैं। केवल तभी उपयोग करें जब आप स्थानीय Docker डेटा खोने का जोखिम उठा सकते हैं।

---

# यदि आप Docker Engine (Linux) पर हैं या मैन्युअल सफाई से सहज हैं (विनाशकारी)

**यह केवल तभी करें जब आप डेटा हानि के जोखिम को समझते हों।** Docker डेमन को रोकें, समस्या वाले id के लिए overlay2 डायरेक्टरी हटाएं, फिर Docker को रीस्टार्ट करें।

```bash
# docker डेमन रोकें (Linux)
sudo systemctl stop docker

# पहले overlay2 फोल्डर का बैकअप लें (वैकल्पिक, यदि आपके पास जगह है)
sudo cp -a /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f /root/overlay2-backup-7acbf095

# यदि बैकअप हो गया है / आवश्यक नहीं है, तो उस ओवरले के लिए merged डायरेक्टरी हटाएं:
sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f

# (वैकल्पिक रूप से) आवश्यकता पड़ने पर कंटेनर मेटाडेटा हटाएं
# चेतावनी: केवल उन्हीं फाइलों को हटाएं जिनके बारे में आप निश्चित हैं कि वे टूटे हुए कंटेनर से संबंधित हैं
sudo rm -rf /var/lib/docker/containers/ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18

# docker शुरू करें
sudo systemctl start docker

# फिर dangling आइटम्स को साफ करने का प्रयास करें
docker system prune -a --volumes
```

फिर से: `/var/lib/docker` के तहत फाइलों को हटाना विनाशकारी है और गलत तरीके से किए जाने पर अन्य कंटेनरों को तोड़ सकता है। केवल तभी उपयोग करें जब आप जानते हों कि आप क्या हटा रहे हैं।

---

# कम-विनाशकारी सफाई जो अक्सर मदद करती है

यदि आप सीधे ओवरले को हटा नहीं सकते हैं या एक नरम दृष्टिकोण पसंद करते हैं:

```bash
# अप्रयुक्त ऑब्जेक्ट्स को हटाने का प्रयास करें
docker system prune -f
docker volume prune -f

# अप्रयुक्त images/containers हटाएं (सावधान रहें)
docker image prune -a -f
docker container prune -f
```

यह स्थान मुक्त कर सकता है और कभी-कभी Docker को हटाने के ऑपरेशन को सफलतापूर्वक फिर से चलाने देता है।

---

# यदि समस्या बार-बार होती है और आप Mac के लिए Docker Desktop का उपयोग करते हैं

* Docker VM डिस्क आकार बढ़ाने पर विचार करें (Settings → Resources → Disk image size)।
* यदि आप महत्वपूर्ण स्थानीय डेटा पर निर्भर हैं, तो Reset/Purge का उपयोग करने से पहले पहले volumes/containers को एक्सपोर्ट करें (`docker export`, `docker save`)।

---

# नैदानिक जानकारी एकत्रित करने के लिए (यदि आप चाहते हैं कि मैं और मदद करूं)

यदि उपरोक्त में से कोई भी इसे ठीक नहीं करता है, तो इन (गैर-विनाशकारी) कमांड के आउटपुट साझा करें और मैं लक्षित अगले चरण सुझाऊंगा:

```bash
docker info
docker ps -a
docker compose version
docker version
# ओवरले डिरेक्टरीज़ की सूची बनाएं (Linux)
ls -lah /var/lib/docker/overlay2 | head -n 40
```

(यदि आप macOS Docker Desktop पर हैं, तो `ls /var/lib/docker` VM सामग्री नहीं दिखाएगा — Docker Desktop को रीस्टार्ट करना या Troubleshoot UI का उपयोग करना पसंद करें।)

---

यदि आप चाहें, तो मुझे बताएं कि आप **Docker Desktop on macOS** (सबसे अधिक संभावना) चला रहे हैं या **Docker Engine on Linux** — मैं एक छोटा, अनुकूलित अनुक्रम दूंगा। यदि आप पसंद करते हैं, तो मैं एक-लाइन चेकलिस्ट भी बना सकता हूं जिसे आप क्रम में चला सकते हैं।