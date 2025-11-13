---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एन्जिन्क्स सीओआरएस और एचटीटीपीएस कॉन्फ़िगरेशन
translated: true
type: note
---

```nginx
# अनुमत उत्पत्ति स्रोतों को संभालने के लिए एक मैप परिभाषित करें
map $http_origin $cors_origin {
    default "https://example.com";
    "http://localhost:3000" "http://localhost:3000";
    "https://example.com" "https://example.com";
    "https://www.example.com" "https://www.example.com";
}
```

### यह क्या करता है
- आने वाले `Origin` हेडर (`$http_origin`) के मान के आधार पर एक वेरिएबल `$cors_origin` बनाता है।
- यदि अनुरोध `http://localhost:3000`, `https://example.com`, या `https://www.example.com` से आता है, तो यह उसी सटीक उत्पत्ति स्रोत को वापस लौटाता है।
- किसी भी अन्य उत्पत्ति स्रोत (या बिना उत्पत्ति स्रोत के) के लिए, यह डिफ़ॉल्ट रूप से `https://example.com` पर सेट हो जाता है।
- इसका उपयोग बाद में `Access-Control-Allow-Origin` हेडर को डायनामिक रूप से सेट करने के लिए किया जाता है, जो केवल विश्वसनीय फ्रंट-एंड डोमेन के लिए CORS सक्षम करता है।

---

```nginx
# HTTP को HTTPS पर रीडायरेक्ट करें
server {
    listen 80;
    server_name example.com api.example.com;
    return 301 https://$host$request_uri;
}
```

### यह क्या करता है
- पोर्ट 80 (HTTP) पर लिसन करता है।
- `example.com` या `api.example.com` के अनुरोधों से मेल खाता है।
- सभी ट्रैफ़िक को उसी URL के HTTPS वर्जन पर स्थायी रूप से रीडायरेक्ट (301) करता है।
- सुरक्षित कनेक्शन को बाध्य करता है; सादा HTTP एक्सेस की अनुमति नहीं है।

---

```nginx
# example.com के लिए मुख्य साइट कॉन्फ़िगरेशन
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    root /home/project/project-web;
    index index.html index.htm index.php default.html default.htm default.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$ {
        expires 30d;
    }

    location ~ .*\.(js|css)?$ {
        expires 12h;
    }

    error_page 404 /index.html;
}
```

### यह क्या करता है
- `example.com` के लिए पोर्ट 443 पर **HTTPS सर्वर** SSL सक्षम के साथ।
- **Let’s Encrypt** सर्टिफिकेट्स (ऑटो-रिन्यूएबल, मुफ्त) का उपयोग करता है।
- सुरक्षा के लिए आधुनिक TLS वर्जन (`TLSv1.2`, `TLSv1.3`) और मजबूत सिफर्स लागू करता है।
- `/home/project/project-web` से स्टैटिक फाइलें सर्व करता है।
- अनुरोधित फाइल → डायरेक्टरी → 404 को सर्व करने का प्रयास करता है।
- **कैश हेडर्स** सेट करता है:
  - इमेजेज: 30 दिनों के लिए कैश।
  - JS/CSS: 12 घंटों के लिए कैश।
- सभी 404 एरर्स को `index.html` पर रूट किया जाता है → **SPA (सिंगल पेज ऐप)** रूटिंग सक्षम करता है (जैसे, React, Vue)।

---

```nginx
# api.example.com के लिए API कॉन्फ़िगरेशन
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com-0001/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com-0001/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    location / {
        # किसी भी पहले से मौजूद Access-Control हेडर्स को साफ करें
        more_clear_headers 'Access-Control-Allow-Origin';

        # CORS प्रीफ्लाइट अनुरोधों को संभालें
        if ($request_method = 'OPTIONS') {
            add_header 'Access-Control-Allow-Origin' $cors_origin;
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE';
            add_header 'Access-Control-Allow-Headers' 'Origin, Content-Type, Accept, Authorization, X-Client-Info, X-Trace-Id, X-Requested-With, X-HTTP-Method-Override, DNT, Keep-Alive, User-Agent, If-Modified-Since, Cache-Control, Content-Range, Range';
            add_header 'Access-Control-Max-Age' 3600;
            return 204;
        }

        add_header 'Access-Control-Allow-Origin' $cors_origin always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE' always;
        add_header 'Access-Control-Allow-Headers' '...' always;

        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 600s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
        send_timeout 600s;
    }
}
```

### यह क्या करता है
- `api.example.com` के लिए **HTTPS रिवर्स प्रॉक्सी**।
- एक **अलग Let’s Encrypt सर्टिफिकेट** का उपयोग करता है (संभवतः मल्टीपल डोमेन/SANs के कारण)।
- सभी ट्रैफ़िक `localhost:5000` पर चल रहे **लोकल बैकएंड** पर प्रॉक्सी की जाती है (जैसे, Flask, Node.js, आदि)।

#### CORS हैंडलिंग
- केवल अनुमोदित उत्पत्ति स्रोतों को **डायनामिक रूप से अनुमति** देने के लिए `$cors_origin` मैप का उपयोग करता है।
- कॉन्फ्लिक्ट रोकने के लिए किसी भी मौजूदा `Access-Control-Allow-Origin` को **साफ करता है**।
- **OPTIONS प्रीफ्लाइट** को संभालता है:
  - तुरंत `204 No Content` रिटर्न करता है।
  - सामान्य मेथड्स और हेडर्स की अनुमति देता है।
  - प्रीफ्लाइट को 1 घंटे के लिए कैश करता है (`Max-Age: 3600`)।
- वास्तविक अनुरोधों के लिए, CORS हेडर्स को `always` के साथ जोड़ता है ताकि वे एरर रिस्पॉन्स पर भी दिखाई दें।

#### प्रॉक्सी सेटिंग्स
- रियल क्लाइंट IP और प्रोटोकॉल जानकारी को बैकएंड तक फॉरवर्ड करता है।
- हाई टाइमआउट (10 मिनट) → लंबे समय तक चलने वाले API ऑपरेशन के लिए उपयुक्त (जैसे, फाइल अपलोड, भारी कम्प्यूटेशन)।

---

### आर्किटेक्चर सारांश

| कंपोनेंट           | उद्देश्य |
|---------------------|--------|
| `example.com`       | स्टैटिक SPA (React/Vue/आदि) सर्व करता है |
| `api.example.com`   | सिक्योर API गेटवे → पोर्ट 5000 पर बैकएंड |
| HTTP → HTTPS        | सभी ट्रैफ़िक TLS पर बाध्य |
| CORS                | `example.com`, `www`, और `localhost:3000` तक सीमित |
| कैशिंग             | परफॉर्मेंस के लिए ऑप्टिमाइज़्ड |
| SSL                 | Let’s Encrypt, मॉडर्न सिफर्स |

### सुरक्षा नोट्स
- मजबूत TLS कॉन्फ़िग (SSL Labs पर A+ रेटिंग संभावित)।
- CORS **वाइल्डकार्ड नहीं** है → अनअथॉराइज्ड साइट्स को API कॉल करने से रोकता है।
- प्रीफ्लाइट कुशलता से संभाला गया है।
- रियल IP फॉरवर्ड किया गया → बैकएंड में लॉगिंग/रेट-लिमिटिंग के लिए उपयोगी।

मुझे बताएं अगर आपको डायग्राम या Dockerized वर्जन चाहिए!