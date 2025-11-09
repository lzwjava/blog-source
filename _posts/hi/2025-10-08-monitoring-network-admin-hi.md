---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एडमिन अधिकारों के साथ नेटवर्क गतिविधि की निगरानी
translated: true
type: note
---

### एडमिन अधिकारों के साथ HTTP अनुरोधों और TCP कनेक्शनों की निगरानी

मान लें कि आप एक Linux/Unix-जैसी सिस्टम (जैसे Ubuntu, CentOS) पर काम कर रहे हैं जहाँ root/एडमिन विशेषाधिकार हैं, आप नैतिक रूप से समस्या निवारण, सुरक्षा ऑडिटिंग, या पेंटेस्टिंग के लिए नेटवर्क गतिविधि की निगरानी कर सकते हैं। **महत्वपूर्ण: ऐसा केवल उन सिस्टम पर करें जिनके आप मालिक हैं या जिनके लिए आपके पास स्पष्ट अनुमति है—अनधिकृत निगरानी अवैध है।** मैं कमांड-लाइन टूल्स पर ध्यान केंद्रित करूंगा, जो हल्के होते हैं और GUI की आवश्यकता नहीं होती।

#### 1. **सभी TCP कनेक्शनों की निगरानी करें**
   रीयल-टाइम कैप्चर के लिए `ss` (`netstat` का आधुनिक प्रतिस्थापन) या `tcpdump` जैसे बिल्ट-इन टूल्स का उपयोग करें। ये सक्रिय कनेक्शन, पोर्ट और प्रक्रियाएं दिखाते हैं।

   - **सभी वर्तमान TCP कनेक्शनों की सूची बनाएं (स्थिर दृश्य):**
     ```
     sudo ss -tunap
     ```
     - `-t`: केवल TCP.
     - `-u`: UDP यदि आवश्यक हो (लेकिन आपने TCP के लिए कहा था)।
     - `-n`: न्यूमेरिक पोर्ट (कोई DNS रिज़ॉल्यूशन नहीं)।
     - `-a`: सभी स्थितियां (established, listening, आदि)।
     - `-p`: स्वामित्व वाली प्रक्रियाएं दिखाएं।
     आउटपुट उदाहरण:
     ```
     tcp   ESTAB  0      0      192.168.1.10:80     10.0.0.5:54321    users:(("nginx",pid=1234,fd=5))
     ```
     केवल लिसनिंग सॉकेट के लिए: `sudo ss -tlnp`.

   - **watch के साथ रीयल-टाइम निगरानी:**
     ```
     watch -n 1 'sudo ss -tunap'
     ```
     हर सेकंड रिफ्रेश होता है।

   - **लाइव TCP ट्रैफिक कैप्चर करें (पैकेट-स्तर):**
     यदि मौजूद नहीं है तो `tcpdump` इंस्टॉल करें: `sudo apt update && sudo apt install tcpdump` (Debian/Ubuntu) या `sudo yum install tcpdump` (RHEL/CentOS)।
     ```
     sudo tcpdump -i any tcp -n -v
     ```
     - `-i any`: सभी इंटरफेस।
     - `-n`: कोई नाम रिज़ॉल्यूशन नहीं।
     - `-v`: वर्बोज़।
     HTTP/HTTPS को फिल्टर करने के लिए `port 80 or port 443` जोड़ें: `sudo tcpdump -i any tcp port 80 or tcp port 443 -n -v -A` (`-A` ASCII पेलोड के लिए, HTTP हेडर देखने के लिए)।

     बाद में विश्लेषण के लिए फाइल में सेव करें: `sudo tcpdump -i any tcp -w capture.pcap`.

#### 2. **HTTP अनुरोध लॉग की निगरानी करें**
   HTTP लॉग आपके वेब सर्वर (Apache, Nginx, आदि) पर निर्भर करते हैं। यदि कोई वेब सर्वर नहीं चल रहा है, तो HTTP ट्रैफिक का निरीक्षण करने के लिए नेटवर्क कैप्चर (ऊपर) का उपयोग करें। सर्वर-विशिष्ट लॉग के लिए:

   - **Apache (httpd):**
     लॉग आमतौर पर `/var/log/apache2/access.log` (Ubuntu) या `/var/log/httpd/access_log` (CentOS) में होते हैं।
     ```
     sudo tail -f /var/log/apache2/access.log
     ```
     - रीयल-टाइम में अनुरोध दिखाता है: IP, टाइमस्टैम्प, विधि (GET/POST), URL, स्टेटस कोड।
     उदाहरण लाइन: `192.168.1.100 - - [08/Oct/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234`.

     सभी लॉग के लिए: `sudo grep "GET\|POST" /var/log/apache2/access.log | less`.

   - **Nginx:**
     लॉग `/var/log/nginx/access.log` में होते हैं।
     ```
     sudo tail -f /var/log/nginx/access.log
     ```
     Apache के समान प्रारूप।

   - **यदि कोई वेब सर्वर नहीं है (सामान्य HTTP स्निफिंग):**
     HTTP पेलोड डंप करने के लिए `-A` के साथ `tcpdump` का उपयोग करें, या regex मिलान के लिए `ngrep` इंस्टॉल करें:
     ```
     sudo apt install ngrep  # इंस्टॉल करें यदि आवश्यक हो
     sudo ngrep -d any 'GET|POST|HTTP' -O http_capture.pcap
     ```
     यह HTTP विधियों को फिल्टर और लॉग करता है।

   - **उन्नत: पूर्ण लॉगिंग के लिए एक पारदर्शी प्रॉक्सी सेटअप करें।**
     Squid proxy इंस्टॉल करें: `sudo apt install squid`.
     सभी HTTP को लॉग करने के लिए `/etc/squid/squid.conf` कॉन्फ़िगर करें (`access_log /var/log/squid/access.log squid` जोड़ें)।
     iptables के माध्यम से ट्रैफिक रीडायरेक्ट करें: `sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3128`.
     फिर Squid लॉग टेल करें: `sudo tail -f /var/log/squid/access.log`.

#### "हैकिंग" के लिए टिप्स (नैतिक पेंटेस्टिंग)
- **टूल्स को संयोजित करें:** विशिष्ट पैटर्न के लिए `tcpdump` को `grep` में पाइप करें, उदा., `sudo tcpdump -i any tcp port 80 -A | grep "User-Agent"`.
- **Wireshark के साथ विज़ुअलाइज़ करें:** GUI विश्लेषण के लिए, Wireshark इंस्टॉल करें (`sudo apt install wireshark`), रूट के रूप में रन करें, और अपनी `.pcap` फाइल खोलें।
- **सुरक्षा सख्त करना:** निगरानी के बाद, यदि संवेदनशील है तो लॉग साफ करें: `sudo truncate -s 0 /var/log/access.log`.
- **क्रॉस-प्लेटफ़ॉर्म नोट:** Windows (एडमिन के साथ) पर, TCP के लिए `netstat -anob` और लॉग के लिए Event Viewer का उपयोग करें। macOS पर, `netstat -an` और `tcpdump`.

यह सेटअप आपको बाहरी टूल्स के बिना व्यापक दृश्यता प्रदान करता है। पहले एक VM में परीक्षण करें।

[Linux ss कमांड मैन पेज](https://man7.org/linux/man-pages/man8/ss.8.html)  
[Tcpdump ट्यूटोरियल](https://www.tcpdump.org/manpages/tcpdump.1.html)  
[Apache एक्सेस लॉग फॉर्मेट](https://httpd.apache.org/docs/2.4/logs.html)