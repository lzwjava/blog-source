---
audio: false
generated: false
lang: hi
layout: post
title: iOS का डेवलपर मोड और ideviceinstaller
translated: true
---

## डेवलपर मोड

मैं कुछ समय के लिए एक iOS डेवलपर था। लेकिन मेरा करियर फोकस अब अन्य टेक्नोलॉजीज पर शिफ्ट हो गया है। हालांकि, अब भी iOS डेवलपमेंट का ज्ञान लागू करना बहुत उपयोगी है, भले ही मैं अब एक पेशेवर iOS डेवलपर नहीं हूं।

हाल ही में, मैं अपने इंस्टॉल किए गए ऐप्स को साझा करना चाहता था। लेकिन अगर मैं होम स्क्रीन से या सेटिंग्स में ऐप सूची से सभी ऐप्स की स्क्रीनशॉट लेता, तो यह बहुत अव्यवस्थित हो जाता। इसलिए मुझे सभी इंस्टॉल किए गए ऐप्स को देखने का एक तरीका खोजने की जरूरत थी।

यहां Xcode का उपयोग करके सभी इंस्टॉल किए गए ऐप्स को देखने के चरण दिए गए हैं:

1. अपने iPhone को USB के माध्यम से अपने Mac से कनेक्ट करें
2. Xcode खोलें
3. Window → Devices and Simulators पर जाएं (या Shift + Cmd + 2 दबाएं)
4. बाईं साइडबार से अपना iPhone चुनें
5. मुख्य पैनल में, "Installed Apps" सेक्शन तक स्क्रॉल करें

इसमें अन्य उपयोगी कार्य भी हैं:

1. स्क्रीनशॉट लेना  
2. हाल के लॉग खोलना  
3. कंसोल खोलना

## xcrun

`xcrun` एक कमांड-लाइन टूल है जो Xcode के साथ आता है और डेवलपर्स को Xcode टूलचेन के विभिन्न उपकरणों और उपयोगिताओं तक पहुंच प्रदान करता है। यह macOS पर डेवलपमेंट और बिल्ड प्रक्रियाओं को सरल बनाने के लिए उपयोग किया जाता है। `xcrun` का उपयोग करके, आप कंपाइलर, लिंकर, और अन्य टूल्स को सीधे टर्मिनल से एक्सेस कर सकते हैं।

### उदाहरण

```bash
xcrun clang -o hello hello.c
```

यह कमांड `clang` कंपाइलर का उपयोग करके `hello.c` फ़ाइल को कंपाइल करता है और `hello` नामक एक्जीक्यूटेबल फ़ाइल बनाता है।

`xcrun` का उपयोग करके आप Xcode के विभिन्न टूल्स को आसानी से एक्सेस कर सकते हैं और अपनी डेवलपमेंट वर्कफ़्लो को सुव्यवस्थित कर सकते हैं।

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
वर्बोस लॉगिंग का उपयोग कर रहे हैं।
2024-12-03 16:24:18.579+0800  डेवलपर डिस्क इमेज सेवाएं सक्षम कर रहे हैं।
2024-12-03 16:24:18.637+0800  उपयोग दावा प्राप्त किया।
इंस्टॉल किए गए ऐप्स:
  - 0 तत्व
```

कमांड पूर्ण हुई, 0.120 सेकंड लगे
```

## ideviceinstaller

`ideviceinstaller` एक कमांड-लाइन टूल है जो iOS डिवाइस पर एप्लिकेशन (.ipa फ़ाइलें) इंस्टॉल, अनइंस्टॉल, अपग्रेड, और उन्हें सूचीबद्ध करने के लिए उपयोग किया जाता है। यह टूल libimobiledevice लाइब्रेरी पर आधारित है और macOS, Linux, और Windows सहित विभिन्न प्लेटफॉर्म पर काम करता है।

### स्थापना (Installation)

macOS पर `ideviceinstaller` को Homebrew का उपयोग करके इंस्टॉल किया जा सकता है:

```bash
brew install ideviceinstaller
```

Linux पर, आप इसे निम्नलिखित कमांड का उपयोग करके इंस्टॉल कर सकते हैं:

```bash
sudo apt-get install ideviceinstaller
```

### उपयोग (Usage)

`ideviceinstaller` का उपयोग करने के लिए, आपको अपने iOS डिवाइस को कंप्यूटर से कनेक्ट करना होगा। निम्नलिखित कुछ सामान्य कमांड हैं:

1. **एप्लिकेशन सूचीबद्ध करना (List Applications):**

   ```bash
   ideviceinstaller -l
   ```

2. **एप्लिकेशन इंस्टॉल करना (Install Application):**

   ```bash
   ideviceinstaller -i /path/to/application.ipa
   ```

3. **एप्लिकेशन अनइंस्टॉल करना (Uninstall Application):**

   ```bash
   ideviceinstaller -U com.example.app
   ```

4. **एप्लिकेशन अपग्रेड करना (Upgrade Application):**

   ```bash
   ideviceinstaller -u /path/to/application.ipa
   ```

### सामान्य समस्याएं (Common Issues)

- **डिवाइस नहीं मिल रहा है (Device Not Found):** सुनिश्चित करें कि आपका डिवाइस कंप्यूटर से सही ढंग से कनेक्ट है और iTunes (या libimobiledevice) डिवाइस को पहचानता है।
  
- **अनुमति समस्याएं (Permission Issues):** Linux पर, आपको `usbmuxd` सेवा को सही ढंग से कॉन्फ़िगर करने की आवश्यकता हो सकती है।

`ideviceinstaller` iOS डेवलपर्स और टेस्टर्स के लिए एक उपयोगी टूल है, जो डिवाइस पर एप्लिकेशन प्रबंधन को सरल बनाता है।

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

(यह कोड ब्लॉक है, इसे अनुवादित नहीं किया जाना चाहिए।)

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