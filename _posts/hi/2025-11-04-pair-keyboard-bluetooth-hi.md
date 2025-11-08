---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ब्लूटूथ सीएलआई के जरिए लॉजिटेक कीबोर्ड को पेयर करें
translated: true
type: note
---

### पूर्वापेक्षाएँ
- सुनिश्चित करें कि आपका Bluetooth 5.3 एमिटर (डोंगल) USB 3.0 पोर्ट में लगा है और Ubuntu द्वारा पहचाना गया है। जाँचने के लिए टर्मिनल में `lsusb` चलाएँ (कुछ "Bluetooth" या वेंडर ID जैसा दिखे)। यदि नहीं दिखे, तो कोई दूसरा USB पोर्ट आज़माएँ या रीबूट करें।
- यदि पहले से मौजूद नहीं हैं तो Bluetooth टूल्स इंस्टॉल करें:  
  ```
  sudo apt update
  sudo apt install bluez bluetooth bluez-tools
  ```
- यदि आवश्यक हो तो Bluetooth को अनब्लॉक करें:  
  ```
  rfkill unblock bluetooth
  ```
- Bluetooth सर्विस को रीस्टार्ट करें:  
  ```
  sudo systemctl restart bluetooth
  ```

### bluetoothctl का उपयोग करके पेयरिंग स्टेप्स (CLI के लिए अनुशंसित)
`bluetoothctl` टूल Linux/Ubuntu में Bluetooth प्रबंधित करने का मानक तरीका है। Logitech कीबोर्ड (जैसे MX Keys, K380, या इसी तरह) को अक्सी स्वयं कीबोर्ड पर एक पेयरिंग PIN डालने की आवश्यकता होती है।

1. **Bluetooth कंसोल खोलें**:  
   ```
   bluetoothctl
   ```
   यह एक इंटरैक्टिव शेल में प्रवेश करता है (प्रॉम्प्ट `[bluetooth]#` में बदल जाता है)।

2. **एडाप्टर सक्षम करें**:  
   ```
   power on
   ```
   (यदि यह "No default controller available" कहता है, तो अपना एडाप्टर देखने के लिए `list` चलाएँ और यदि कई हैं तो `select <adapter_MAC>` चलाएँ।)

3. **पेयरिंग एजेंट सेट अप करें**:  
   ```
   agent on
   default-agent
   ```
   यह PIN हैंडलिंग सक्षम करता है और आपकी सेशन को पेयरिंग के लिए डिफ़ॉल्ट बनाता है।

4. **डिवाइसों के लिए स्कैनिंग शुरू करें**:  
   ```
   scan on
   ```
   इसे चलते रहने दें। आपका Logitech कीबोर्ड लगभग 10-20 सेकंड के बाद दिखाई देना चाहिए (जैसे, "Logitech K380" या इसी तरह, MAC एड्रेस के साथ जैसे `XX:XX:XX:XX:XX:XX`)।

5. **अपने Logitech कीबोर्ड को पेयरिंग मोड में डालें**:  
   - इसे चालू करें (यदि इसमें पावर स्विच है)।  
   - Bluetooth पेयरिंग बटन को दबाकर रखें (आमतौर पर साइड या ऊपर—अपने मॉडल की जाँच करें; मल्टी-डिवाइस मॉडल जैसे MX Keys के लिए, चैनल बटन 1/2/3 को 3-5 सेकंड तक तब तक दबाए रखें जब तक LED तेजी से न ब्लिंक करने लगे)।  
   - यदि यह सिंगल-डिवाइस मॉडल है, तो मुख्य पेयरिंग बटन को दबाए रखें।

6. **डिवाइस को पेयर करें**:  
   एक बार यह स्कैन में दिख जाए (ताज़ा करने के लिए Enter दबाएँ), चलाएँ:  
   ```
   pair <MAC_ADDRESS>
   ```
   - उदाहरण: `pair 12:34:56:78:9A:BC`  
   - Ubuntu एक PIN के लिए प्रॉम्प्ट करेगा (अक्सर Logitech के लिए 0000 या 1234—पहले डिफ़ॉल्ट आज़माएँ)।  
   - **Logitech के लिए महत्वपूर्ण कदम**: PIN सीधे *फिजिकल कीबोर्ड* पर टाइप करें और Enter दबाएँ। (यदि कोई GUI नोटिफिकेशन नहीं दिखता है, तो यह महत्वपूर्ण है—कुछ उपयोगकर्ता `gnome-control-center` > Notifications के माध्यम से सिस्टम नोटिफिकेशन सक्षम करने की रिपोर्ट करते हैं, लेकिन CLI अक्सर इसे बायपास कर देता है।)

7. **ट्रस्ट और कनेक्ट करें**:  
   ```
   trust <MAC_ADDRESS>
   connect <MAC_ADDRESS>
   ```
   - यह भविष्य में उपयोग पर ऑटो-कनेक्ट करेगा।

8. **कंसोल से बाहर निकलें**:  
   ```
   exit
   ```

### समस्या निवारण
- **डिवाइस स्कैन नहीं हो रही**: सुनिश्चित करें कि कीबोर्ड पेयरिंग मोड में है (ब्लिंकिंग LED)। `scan off` फिर `scan on` दोबारा चलाएँ। 30 सेकंड तक प्रतीक्षा करें।
- **पेयरिंग विफल हो जाती है (जैसे, "AuthenticationCanceled")**: पहले डिवाइस को हटाएँ (`remove <MAC>`), फिर दोबारा प्रयास करें। जिद्दी Logitech मॉडल के लिए, पेयरिंग बटन को अधिक देर तक दबाए रखने या चैनल टॉगल करने का प्रयास करें।
- **कोई PIN प्रॉम्प्ट नहीं**: कुछ कीबोर्ड बिना PIN के पेयर हो जाते हैं—कनेक्ट करने के लिए आगे बढ़ें। यदि अटक जाएँ, तो लॉग जाँचें: पेयरिंग के दौरान `sudo journalctl -u bluetooth -f`।
- **एडाप्टर समस्याएँ**: यदि USB Bluetooth 5.3 डोंगल का उपयोग कर रहे हैं, तो कर्नेल सपोर्ट की पुष्टि करें (Ubuntu 22.04+ BT 5.3 को अच्छी तरह संभालता है)। यदि पुराने Ubuntu पर हैं तो कर्नेल अपडेट करें: `sudo apt install linux-generic-hwe-22.04`।
- **GUI विकल्प**: Settings > Bluetooth खोलें, टॉगल ऑन करें, और वहाँ से पेयर करें—लेकिन Logitech की खासियतों के लिए CLI अधिक विश्वसनीय है।
- टेस्ट: पेयरिंग के बाद, टर्मिनल में टाइप करें। यदि काम करता है, तो `bluetoothctl` या crontab के माध्यम से स्टार्टअप ऑटो-कनेक्ट में जोड़ें।

यदि आपके विशिष्ट Logitech मॉडल (जैसे, MX Keys Mini) में अद्वितीय समस्याएँ हैं, तो विशिष्ट स्टेप्स के लिए सटीक मॉडल प्रदान करें।

### संदर्भ
- [Pairing LOGITECH K380 in Ubuntu 20.04](https://unix.stackexchange.com/questions/590221/pairing-logitech-k380-in-ubuntu-20-04)  
- [Logitech MX Keys won't pair with Bluetooth](https://askubuntu.com/questions/1270419/20-04-logitech-mx-keys-wont-pair-with-bluetooth)  
- [Pair Logitech MX Keys with Xubuntu via Bluetooth](https://zroupas.github.io/linux/2021/08/25/pair_mxkeys_xubuntu_bt.html)  
- [Ubuntu 20.04 cannot pair Bluetooth Keyboard](https://askubuntu.com/questions/1398096/ubuntu-20-04-cannot-pair-bluetooth-keyboard)