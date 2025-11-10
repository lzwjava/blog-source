---
audio: false
generated: true
image: false
lang: hi
layout: post
title: मैकओएस होमब्रू पर एन्जिन्क्स कॉन्फ़िग
translated: true
type: note
---

macOS पर Homebrew के माध्यम से इंस्टॉल किए गए Nginx (जैसा कि बाइनरी पथ `/opt/homebrew/bin/nginx` से संकेत मिलता है) के लिए, मुख्य कॉन्फ़िगरेशन फ़ाइल आमतौर पर इस स्थान पर होती है:

```
/opt/homebrew/etc/nginx/nginx.conf
```

यह डायरेक्टरी अन्य संबंधित फ़ाइलें भी रखती है, जैसे कि `servers/` सबडायरेक्टरी में सर्वर ब्लॉक (उदाहरण के लिए, `/opt/homebrew/etc/nginx/servers/`).

आपके Nginx इंस्टेंस द्वारा उपयोग की जा रही सटीक कॉन्फ़िग फ़ाइल के पथ की पुष्टि करने के लिए, अपने टर्मिनल में निम्नलिखित कमांड चलाएं:

```
nginx -t
```

यह कॉन्फ़िगरेशन का परीक्षण करेगा और उस `nginx.conf` फ़ाइल का पथ आउटपुट करेगा जिसका वह उपयोग कर रहा है। वैकल्पिक रूप से, कॉन्फ़िग पथ प्रीफ़िक्स सहित कंपाइल-टाइम विवरण देखने के लिए `nginx -V` का उपयोग करें।

यदि आप एक पुराने Intel-आधारित Mac पर हैं जहाँ Homebrew `/usr/local` में इंस्टॉल होता है, तो पथ `/usr/local/etc/nginx/nginx.conf` होगा, लेकिन आपके प्रदान किए गए बाइनरी पथ से `/opt/homebrew` लोकेशन की पुष्टि होती है।

**संदर्भ**  
[Locate the nginx.conf file my nginx is actually using - Stack Overflow](https://stackoverflow.com/questions/19910042/locate-the-nginx-conf-file-my-nginx-is-actually-using)  
[Installing nginx in macOS using homebrew | by Ram - Medium](https://medium.com/@rprprasath05/installing-nginx-in-macos-ventura-using-homebrew-12b87a900a03)  
[Simple Configuration of NGINX on Mac - DEV Community](https://dev.to/arjavdave/simple-configuration-of-nginx-on-mac-3cg3)