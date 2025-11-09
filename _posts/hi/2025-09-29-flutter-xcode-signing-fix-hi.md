---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: फ़्लटर एक्सकोड कोड साइनिंग विफलता ठीक करें
translated: true
type: note
---

आप Flutter / Xcode के सामान्य कोड-साइनिंग फेल्योर का सामना कर रहे हैं: Xcode/`security` को कोई वैध साइनिंग आइडेंटिटी नहीं मिली, इसलिए `flutter run` फिजिकल डिवाइस के लिए ऐप को साइन नहीं कर पा रहा है। नीचे मैं स्पष्ट, क्रमबद्ध फिक्स और ट्रबलशूटिंग कमांड्स दूंगा — आप जो भी रास्ता चुनना चाहते हैं, चुनें (अभी सिम्युलेटर पर चलाएं, या रियल डिवाइस पर चलाने के लिए साइनिंग सेट अप करें)। मैं और जानकारी नहीं मांगूंगा — मैं मानकर चलूंगा कि आप इसे अभी ठीक करना चाहते हैं।

---

# त्वरित विकल्प (एक चुनें)

**A — सिम्युलेटर पर चलाएं (कोड साइनिंग की आवश्यकता नहीं)**
अगर आप बिना सर्टिफिकेट की परेशानी के तेजी से ऐप चलाना चाहते हैं:

1. सिम्युलेटर खोलें: `open -a Simulator`
2. सिम्युलेटर को टार्गेट करते हुए Flutter चलाएं:
   `flutter run -d "$(xcrun simctl list devices | grep -m1 -o "iPhone.*(Simulator)" | sed 's/ (Simulator)//')"`
   या अधिक सरलता से: `flutter run -d iPhone-14` (`xcrun simctl list` से दिखने वाले उपलब्ध सिम्युलेटर नाम से बदलें)।

**B — रियल डिवाइस पर डिप्लॉय करने के लिए साइनिंग ठीक करें (डिवाइस टेस्टिंग के लिए रिकमेंडेड)**
नीचे दिए गए स्टेप्स को क्रम से फॉलो करें।

---

# डिवाइस डिप्लॉयमेंट के लिए साइनिंग ठीक करने के स्टेप्स

## 1) एनवायरनमेंट और बेसिक चेक्स कन्फर्म करें

इन्हें रन करें और आउटपुट नोट करें:

```bash
flutter doctor -v
xcode-select --print-path
xcodebuild -version
security find-identity -p codesigning -v
xcrun simctl list devices
```

`security find-identity -p codesigning -v` को कम से कम एक आइडेंटिटी दिखानी चाहिए। आपके केस में `0 valid identities found` दिखा — यही फेल्योर का कारण है।

## 2) Xcode ऑटोमैटिक साइनिंग का उपयोग करें (सबसे आसान)

1. वर्कस्पेस खोलें:
   `open ios/Runner.xcworkspace`
2. Xcode में: `Runner` प्रोजेक्ट → `Runner` टार्गेट → **Signing & Capabilities** चुनें।
3. **Team** को अपने Apple ID / Apple Developer अकाउंट पर सेट करें। अगर आपका Apple ID एड नहीं है:

   * Xcode → Preferences → Accounts → `+` → Apple ID एड करें।
4. **Automatically manage signing** को टिक करें।
5. सुनिश्चित करें कि **Bundle Identifier** यूनिक है (रिवर्स-डीएनएस स्टाइल, जैसे `com.yourname.yourapp`)।
6. Xcode एक डेवलपमेंट सर्टिफिकेट और प्रोविजनिंग प्रोफाइल बनाने का प्रयास करेगा; अगर आपको प्रॉम्प्ट दिखें, तो Xcode को इसे मैनेज करने दें।

> नोट: किसी भी डिवाइस पर फुल डिप्लॉयमेंट के लिए आपको Apple Developer मेम्बरशिप ($99/वर्ष) की आवश्यकता होती है। Xcode "फ्री प्रोविजनिंग" के लिए एक फ्री Apple ID का उपयोग कर सकता है, लेकिन यह सीमित है (डिवाइस काउंट, कुछ एंटाइटलमेंट्स नहीं)।

## 3) अपनी डिवाइस को रजिस्टर करें (अगर आवश्यक हो)

अगर Xcode आपकी डिवाइस को ऑटोमैटिकली रजिस्टर नहीं कर पा रहा है, तो Apple Developer Portal → Certificates, IDs & Profiles → Devices → डिवाइस UDID एड करें। आप डिवाइस को कनेक्ट करके और Xcode के Devices and Simulators विंडो में उसे सेलेक्ट करके UDID प्राप्त कर सकते हैं।

## 4) सर्टिफिकेट मैन्युअली जेनरेट/इम्पोर्ट करें (अगर आपके पास पहले से p12 है)

अगर आपके पास `.p12` सर्टिफिकेट और प्राइवेट की है:

```bash
security import /path/to/certificate.p12 -k ~/Library/Keychains/login.keychain-db -P "P12_PASSWORD" -T /usr/bin/codesign
```

फिर `security find-identity -p codesigning -v` को दोबारा रन करके कन्फर्म करें कि यह दिखाई दे रहा है।

## 5) अगर आप चाहते हैं कि Xcode आपके लिए सर्टिफिकेट बनाए

Xcode → Accounts → अपना Apple ID सेलेक्ट करें → Manage Certificates → `+` → **iOS Development** एड करें। यह आपकी कीचेन में एक सर्ट बनाता है और `security find-identity` में दिखाई देता है।

## 6) सुनिश्चित करें कि Command Line Tools सेट हैं

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

फिर लाइसेंस स्वीकार करें अगर जरूरत हो:

```bash
sudo xcodebuild -license accept
```

## 7) साइनिंग सेट होने के बाद, टर्मिनल से रन करें

प्रोजेक्ट रूट से:

```bash
flutter clean
flutter pub get
flutter run
```

अगर मल्टीपल डिवाइस हैं, तो `-d <device-id>` स्पेसिफाई करें।

---

# ट्रबलशूटिंग टिप्स और कॉमन पिटफॉल

* **"0 valid identities found" बनी रहती है** — कन्फर्म करें कि सर्टिफिकेट की प्राइवेट की लॉगिन कीचेन में है (Keychain Access → login खोलें)। अगर आपने सर्टिफिकेट तो इम्पोर्ट कर लिया लेकिन प्राइवेट की नहीं, तो साइनिंग फेल होगी।
* **Bundle ID मिसमैच** — Developer Portal में App ID, Xcode में bundle identifier से बिल्कुल मेल खाना चाहिए (कुछ केस के लिए वाइल्डकार्ड की अनुमति है)।
* **Team सेलेक्ट नहीं** — Xcode "No account" दिखा रहा है — Xcode Preferences → Accounts में Apple ID एड करें।
* **प्रोविजनिंग प्रोफाइल एक्सपायर्ड** — Developer Portal चेक करें और प्रोविजनिंग प्रोफाइल रीजेनरेट करें।
* **फ्री प्रोविजनिंग लिमिटेशन** — अगर फ्री Apple ID का उपयोग कर रहे हैं, तो आपको हर 7 दिन में री-प्रोविजन करना पड़ सकता है और डिवाइस सीमित हैं।
* **CI / ऑटोमेशन** — सर्ट्स और प्रोफाइल्स को सेंट्रली मैनेज करने के लिए `fastlane match` या App Store Connect APIs का उपयोग करें।
* **Codesign परमिशन एरर** — सुनिश्चित करें कि Keychain आइटम codesign एक्सेस ग्रांट करता है; कभी-कभी `/usr/bin/codesign` को Keychain में प्राइवेट की एक्सेस करने के लिए मैन्युअली अलाउ करना पड़ता है।
* **अगर `flutter run` अभी भी फेल होता है**, तो एक अधिक डिटेल्ड एरर देखने के लिए Xcode बिल्ड रन करें: वर्कस्पेस खोलें और Xcode में Run दबाएं; Signing & Capabilities में एरर चेक करें।

---

# उपयोगी कमांड्स कॉपी-पेस्ट

कोडसाइनिंग आइडेंटिटीज लिस्ट करें:

```bash
security find-identity -p codesigning -v
```

`.p12` इम्पोर्ट करें:

```bash
security import /path/to/yourcert.p12 -k ~/Library/Keychains/login.keychain-db -P "P12PASSWORD" -T /usr/bin/codesign
```

Xcode कमांड लाइन टूल्स सेट करें:

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

iOS वर्कस्पेस खोलें:

```bash
open ios/Runner.xcworkspace
```

---

# अगर आप चाहें, तो मैं यह कर सकता हूं

* सर्ट/प्रोफाइल बनाने के लिए Xcode क्लिक्स की सटीक सीक्वेंस दूं (मैंने कोर स्टेप्स पहले ही शामिल कर दिए हैं), या
* `fastlane`/`match` उदाहरण कमांड्स प्रदान करूं अगर आप मल्टीपल मशीन/CI के लिए ऑटोमेशन चाहते हैं, या
* Xcode ऑटोमैटिक साइनिंग रूट ट्राई करने के बाद किसी भी नए एरर आउटपुट को इंटरप्रेट करने में मदद करूं।

मुझे बताएं कि आपने कौन सा रास्ता चुना (अभी सिम्युलेटर / Xcode ऑटोमैटिक / मैन्युअल p12 इम्पोर्ट / CI) और अगर यह अभी भी फेल होता है तो कोई भी नया एरर पेस्ट करें — मैं अगले स्टेप्स दूंगा।