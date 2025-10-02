---
audio: false
generated: false
image: true
lang: hi
layout: post
title: पिक्सेल यूएसबी, आईओएस डेवलपर टूल्स, स्वाइप टाइपिंग
translated: true
---

### विषयसूची

1. [Pixel के USB विकल्प](#pixels-usb-options)
   - Pixel को वेबकैम के रूप में उपयोग करें
   - सेटिंग्स में डेवलपर मोड सक्षम करें
   - कनेक्शन के लिए USB डिबगिंग सक्रिय करें
   - ADB कमांड से कनेक्शन सत्यापित करें

2. [iOS का डेवलपर मोड और ideviceinstaller](#developer-mode-of-ios-and-ideviceinstaller)
   - Xcode के माध्यम से इंस्टॉल किए गए ऐप्स देखें
   - स्क्रीनशॉट और लॉग के लिए Xcode का उपयोग करें
   - xcrun कमांड से ऐप्स सूचीबद्ध करें
   - ideviceinstaller टूल इंस्टॉल और उपयोग करें

3. [त्वरित स्वाइप टाइपिंग](#quick-swipe-typing)
   - अक्षरों पर स्वाइप करके शब्द इनपुट करें
   - यह सुविधा गलती से खोजी गई
   - तेज़ स्पर्श के दौरान रेखा दिखाई देती है


## Pixel के USB विकल्प

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel कई USB विकल्प प्रदान करता है, और एक विशेष रूप से दिलचस्प सुविधा वेबकैम के रूप में कार्य करने की इसकी क्षमता है। macOS पर, QuickTime Android वेबकैम को वीडियो स्रोत के रूप में एक्सेस कर सकता है, जो एक सरल और प्रभावी समाधान प्रदान करता है।

इसे सेटअप करने के लिए:

1. सेटिंग्स में अबाउट फोन पर जाएं और डेवलपर मोड सक्षम करने के लिए बिल्ड नंबर पर सात बार टैप करें।
2. डेवलपर ऑप्शन खोलें और USB डिबगिंग सक्षम करें।
3. अपने Pixel को USB के माध्यम से अपने कंप्यूटर से कनेक्ट करें और कनेक्शन सत्यापित करने के लिए टर्मिनल में निम्नलिखित कमांड चलाएँ:
   ```bash
   adb devices
   ```

---

## iOS का डेवलपर मोड और ideviceinstaller

*2024.12.03*

## डेवलपर मोड

मैं कुछ समय के लिए एक iOS डेवलपर था। लेकिन मेरे करियर का ध्यान अन्य तकनीकों पर केंद्रित हो गया है। हालांकि, iOS डेवलपमेंट ज्ञान को लागू करना अभी भी बहुत उपयोगी है, भले ही मैं अब एक पेशेवर iOS डेवलपर नहीं हूं।

हाल ही में, मैं अपने इंस्टॉल किए गए ऐप्स को साझा करना चाहता था। लेकिन अगर मैं होम स्क्रीन से या सेटिंग्स में ऐप सूची से सभी ऐप्स के स्क्रीनशॉट लेता, तो यह एक गड़बड़ होती। इसलिए मुझे सभी इंस्टॉल किए गए ऐप्स को देखने का एक तरीका खोजना पड़ा।

Xcode का उपयोग करके सभी इंस्टॉल किए गए ऐप्स को देखने के चरण यहां दिए गए हैं:

1. अपने iPhone को USB के माध्यम से अपने Mac से कनेक्ट करें
2. Xcode खोलें
3. Window → Devices and Simulators पर जाएं (या Shift + Cmd + 2 दबाएं)
4. बाईं साइडबार से अपना iPhone चुनें
5. मुख्य पैनल में, "Installed Apps" सेक्शन तक स्क्रॉल करें

इसके अन्य उपयोगी कार्य भी हैं:

1. स्क्रीनशॉट लेना
2. हाल के लॉग खोलना
3. कंसोल खोलना

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800 Enabling developer disk image services.
2024-12-03 16:24:18.637+0800 Acquired usage assertion.
Apps installed:
  - 0 elements

Command Completed, took 0.120 seconds
```


## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

```bash
(base) lzwjava@192 Downloads % ideviceinstaller -l
CFBundleIdentifier, CFBundleVersion, CFBundleDisplayName
com.huawei.smarthome-ios, "14.1.1.325", "HUAWEI AI Life"
com.sf-express.waybillcn, "9.70.0.1", "顺丰速运"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```

---

## त्वरित स्वाइप टाइपिंग

*2024.12.01*

यदि आप iOS में "threads" इनपुट करना चाहते हैं, तो आपको बस "threads" अक्षरों की स्थिति को कवर करने के लिए एक रेखा को तेज़ी से खींचना होगा ताकि परिणाम मिल सके। आइए देखें कि यह कैसे काम करता है।

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

यह मुझे गलती से मिला। जब मेरी उंगली इनपुट क्षेत्र को तेज़ी से छूती है, तो यह एक रेखा दिखाती है। मुझे नहीं पता था कि इसका क्या मतलब है। कुछ प्रयोगों के बाद, मैंने उपरोक्त खोज की।