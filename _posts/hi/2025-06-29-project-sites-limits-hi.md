---
audio: false
generated: true
lang: hi
layout: post
title: GitHub पेजेज़ प्रोजेक्ट साइट यूआरएल नियम
translated: true
type: note
---

GitHub Pages के साथ, आप अपने User Site (`username.github.io`) के अलावा अपने व्यक्तिगत खाते के तहत **Project Sites** भी बना सकते हैं। हालाँकि, Project Sites के लिए URL का प्रारूप विशिष्ट पैटर्न तक सीमित है, और सभी सबडोमेन या सबपाथ कॉन्फ़िगरेशन नेटिवली सपोर्टेड नहीं हैं। आइए आपके इस सवाल पर गौर करें कि क्या आप Project Sites के लिए `username.github.io/project1` या `project1.username.github.io` का उपयोग कर सकते हैं।

### मुख्य बिंदु
- **User Site**: `username.github.io` नाम की एक सिंगल रिपॉजिटरी `https://username.github.io` पर कंटेंट सर्व करती है।
- **Project Sites**: आपके व्यक्तिगत खाते की कोई भी अन्य रिपॉजिटरी एक Project Site के रूप में कॉन्फ़िगर की जा सकती है, जो `https://username.github.io/repository-name` (एक सबपाथ, सबडोमेन नहीं) पर सर्व होगी।
- **सबडोमेन सीमा**: GitHub Pages, `github.io` डोमेन के तहत `project1.username.github.io` जैसे सबडोमेन को नेटिवली सपोर्ट नहीं करता है। `github.io` डोमेन GitHub द्वारा मैनेज किया जाता है, और केवल `username.github.io` (यूजर्स के लिए) या `organization.github.io` (ऑर्गनाइजेशन के लिए) ही टॉप-लेवल सबडोमेन के रूप में सपोर्टेड हैं। `project1.username.github.io` जैसे कस्टम सबडोमेन के लिए एक कस्टम डोमेन और DNS कॉन्फ़िगरेशन की आवश्यकता होती है।

### क्या आप `username.github.io/project1` का उपयोग कर सकते हैं?
**हाँ**, आप एक Project Site के लिए `username.github.io/project1` का उपयोग कर सकते हैं। यह GitHub Pages द्वारा Project Sites को हैंडल करने का स्टैंडर्ड तरीका है:
- अपने खाते में एक रिपॉजिटरी बनाएँ (जैसे, `username/project1`)।
- उस रिपॉजिटरी के लिए GitHub Pages सक्षम करें:
  - रिपॉजिटरी के **Settings** टैब पर जाएँ।
  - **Pages** सेक्शन तक स्क्रॉल करें।
  - **Source** के तहत, पब्लिश करने के लिए ब्रांच चुनें (जैसे, `main` या `gh-pages`) और सेव करें।
- एक बार कॉन्फ़िगर हो जाने पर, साइट `https://username.github.io/project1` पर एक्सेसिबल हो जाएगी।
- आप अतिरिक्त रिपॉजिटरी (`username/project2`, `username/project3`, आदि) पर GitHub Pages को सक्षम करके मल्टीपल Project Sites (जैसे, `username.github.io/project2`, `username.github.io/project3`) बना सकते हैं।
- **कंटेंट**: प्रत्येक रिपॉजिटरी की पब्लिशिंग ब्रांच में एक `index.html` जोड़ें या Jekyll जैसे स्टैटिक साइट जनरेटर का उपयोग करें।

### क्या आप `project1.username.github.io` का उपयोग कर सकते हैं?
**नहीं**, GitHub Pages, `github.io` डोमेन के तहत `project1.username.github.io` जैसे सबडोमेन को नेटिवली सपोर्ट नहीं करता है। `github.io` डोमेन केवल अनुमति देता है:
- User Sites के लिए `username.github.io`।
- Organization Sites के लिए `organization.github.io`।
- Project Sites के लिए `username.github.io/repository-name` जैसे सबपाथ।

`project1.username.github.io` जैसे URL को प्राप्त करने के लिए, आपको चाहिए होगा:
1. **एक कस्टम डोमेन**: एक डोमेन (जैसे, `example.com`) Namecheap या GoDaddy जैसे रजिस्ट्रार से खरीदें।
2. **DNS कॉन्फ़िगरेशन**: एक सबडोमेन (जैसे, `project1.example.com`) को आपकी GitHub Pages साइट (जैसे, `username.github.io` या `username.github.io/project1`) की ओर पॉइंट करने के लिए एक CNAME रिकॉर्ड सेट अप करें।
3. **GitHub Pages सेटिंग्स**:
   - रिपॉजिटरी की **Pages** सेटिंग्स में, कस्टम डोमेन (जैसे, `project1.example.com`) कॉन्फ़िगर करें।
   - वैकल्पिक रूप से, सुरक्षा के लिए "Enforce HTTPS" सक्षम करें।
4. **परिणाम**: आप `project1.example.com` को `project1` रिपॉजिटरी के कंटेंट पर मैप कर सकते हैं, लेकिन `project1.username.github.io` पर नहीं, क्योंकि GitHub `github.io` डोमेन को कंट्रोल करता है और इसके तहत कस्टम सबडोमेन की अनुमति नहीं देता है।

### `username.github.io/project1` के लिए उदाहरण सेटअप
1. अपने खाते के तहत `project1` नाम की एक रिपॉजिटरी बनाएँ (`username/project1`)।
2. कंटेंट जोड़ें (जैसे, `index.html`):
   ```bash
   git clone https://github.com/username/project1
   cd project1
   echo "Hello from Project 1" > index.html
   git add --all
   git commit -m "Initial commit"
   git push origin main
   ```
3. GitHub Pages सक्षम करें:
   - `username/project1` → **Settings** → **Pages** पर जाएँ।
   - सोर्स को `main` (या किसी अन्य ब्रांच) पर सेट करें और सेव करें।
4. साइट को लाइव देखने के लिए `https://username.github.io/project1` पर जाएँ (प्रोपेगेट होने में कुछ मिनट लग सकते हैं)।

### कस्टम डोमेन के साथ कस्टम सबडोमेन के लिए उदाहरण
यदि आप `project1.example.com` चाहते हैं:
1. एक डोमेन के मालिक बनें (जैसे, `example.com`)।
2. अपने DNS प्रोवाइडर की सेटिंग्स में, एक CNAME रिकॉर्ड जोड़ें:
   - नाम: `project1`
   - वैल्यू: `username.github.io`
3. `project1` रिपॉजिटरी की **Pages** सेटिंग्स में, कस्टम डोमेन को `project1.example.com` पर सेट करें।
4. `project1` रिपॉजिटरी में कंटेंट पुश करें, और यह `project1.example.com` पर सर्व होगा।

### सीमाएँ
- **`github.io` के लिए केवल सबपाथ**: बिना कस्टम डोमेन के, Project Sites हमेशा सबपाथ (`username.github.io/project1`) के रूप में सर्व होते हैं, सबडोमेन (`project1.username.github.io`) के रूप में नहीं।
- **एक User Site**: आपकी `username.github.io` रिपॉजिटरी आपके User Site के लिए रिज़र्व्ड है। Project Sites अन्य रिपॉजिटरीज़ का उपयोग करती हैं और सबपाथ के रूप में दिखाई देती हैं।
- **कस्टम सबडोमेन के लिए कस्टम डोमेन चाहिए**: `project1.something` प्राप्त करने के लिए, आपको `something` (जैसे, `example.com`) का मालिक होना चाहिए और DNS कॉन्फ़िगर करना चाहिए।
- **प्राइवेट रिपॉजिटरीज़**: प्राइवेट रिपॉजिटरीज़ में Project Sites के लिए GitHub Pro, Team, या Enterprise की आवश्यकता होती है। फ्री अकाउंट्स के लिए, रिपॉजिटरीज़ पब्लिक होनी चाहिए।

### सारांश
- **`username.github.io/project1` का उपयोग करें**: हाँ, यह एक रिपॉजिटरी (`username/project1`) बनाकर और GitHub Pages सक्षम करके नेटिवली सपोर्टेड है। आप इस तरह से मल्टीपल Project Sites बना सकते हैं (जैसे, `username.github.io/project2`, आदि)।
- **`project1.username.github.io` का उपयोग करें**: नहीं, यह `github.io` के तहत सपोर्टेड नहीं है। इसी तरह का प्रभाव प्राप्त करने के लिए आपको एक कस्टम डोमेन (जैसे, `project1.example.com`) और DNS सेटअप की आवश्यकता होगी।
- **मल्टीपल सबडोमेन**: मल्टीपल `*.github.io` सबडोमेन प्राप्त करने के लिए, `org1.github.io`, `org2.github.io`, आदि के लिए GitHub ऑर्गनाइजेशन बनाएँ (जैसा कि पहले चर्चा की गई थी), या `project1.example.com` जैसे सबडोमेन के लिए एक कस्टम डोमेन का उपयोग करें।

यदि आपको किसी विशिष्ट Project Site को सेट अप करने, कस्टम डोमेन को कॉन्फ़िगर करने, या मल्टीपल साइट्स को मैनेज करने में मदद की आवश्यकता है, तो मुझे बताएं