---
audio: false
generated: false
image: false
lang: hi
layout: post
title: आईओएस का डेवलपर मोड और आइडिवाइसइंस्टॉलर
translated: true
---

## डेवलपर मोड

मैं कभी कुछ समय के लिए एक iOS डेवलपर था। लेकिन मेरा करियर फोकस अन्य तकनीकों पर शिफ्ट हो गया है। हालांकि, अब भी iOS डेवलपमेंट का ज्ञान लागू करना बहुत उपयोगी है, भले ही मैं अब एक पेशेवर iOS डेवलपर न हो।

हाल ही में, मैंने अपनी इंस्टॉल्ड ऐप्स शेयर करना चाहा। लेकिन अगर मैंने होम स्क्रीन से सभी ऐप्स के स्क्रीनशॉट लिए या सेटिंग्स में ऐप लिस्ट से, तो यह गड़बड़ हो जाता। इसलिए मुझे सभी इंस्टॉल्ड ऐप्स देखने का कोई तरीका खोजने की जरूरत थी।

यहाँ Xcode का उपयोग करके सभी इंस्टॉल्ड ऐप्स देखने के चरण दिए गए हैं:

1. अपने iPhone को USB के माध्यम से अपने Mac से कनेक्ट करें
2. Xcode खोलें
3. Window → Devices and Simulators पर जाएं (या Shift + Cmd + 2 दबाएं)
4. बाएं साइडबार से अपने iPhone का चयन करें
5. मुख्य पैनल में, "Installed Apps" सेक्शन तक स्क्रॉल करें

इसके और भी उपयोगी फंक्शन हैं:

1. स्क्रीनशॉट लेने
2. हालिया लॉग खोलना
3. कंसोल खोलना

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800  Enabling developer disk image services.
2024-12-03 16:24:18.637+0800  Acquired usage assertion.
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

## क्विक स्वाइप टाइपिंग

*2024.12.01*

अगर आप iOS में "threads" इनपुट करना चाहते हैं, तो आपको बस तेज़ी से लाइन खींचकर अक्षरों "threads" के स्थानों को कवर करना होगा और परिणाम मिल जाएगा। आइए देखते हैं यह कैसे काम करता है।

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  आपका ब्राउज़र वीडियो टैग सपोर्ट नहीं करता।
</video>

मैंने इसे अनजाने में खोजा। जब मेरी उंगली तेज़ी से इनपुट एरिया को टच करती है, तो एक लाइन दिखाई देती है। मुझे नहीं पता था कि इसका मतलब क्या है। कुछ प्रयोगों के बाद, मैंने ऊपर दी गई खोज की।