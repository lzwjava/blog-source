---
audio: false
generated: true
lang: hi
layout: post
title: लीनक्लाउड रियलटाइम आईओएस एसडीके
translated: true
type: note
---

`pod 'AVOSCloudIM', '3.1.6.2'` का उपयोग अपने iOS प्रोजेक्ट में CocoaPods के साथ करने के लिए, इन चरणों का पालन करें। यह मानता है कि आपके पास CocoaPods इंस्टॉल है और आप Xcode का उपयोग करके बुनियादी iOS डेवलपमेंट से परिचित हैं।

---

### चरण 1: CocoaPods सेट अप करें (यदि पहले से नहीं किया है)
यदि आपने अभी तक CocoaPods इंस्टॉल नहीं किया है, तो इसे टर्मिनल के माध्यम से इंस्टॉल करें:
```bash
sudo gem install cocoapods
```
इंस्टॉलेशन सत्यापित करें:
```bash
pod --version
```

---

### चरण 2: अपना Xcode प्रोजेक्ट बनाएं या खोलें
1. अपना मौजूदा Xcode प्रोजेक्ट खोलें या Xcode में एक नया बनाएं।
2. अभी के लिए Xcode बंद कर दें (हम इसे बाद में वर्कस्पेस के साथ फिर से खोलेंगे)।

---

### चरण 3: एक Podfile इनिशियलाइज़ करें
1. अपना टर्मिनल खोलें और अपने प्रोजेक्ट की रूट डायरेक्टरी पर नेविगेट करें (जहाँ `.xcodeproj` फ़ाइल स्थित है):
   ```bash
   cd /path/to/your/project
   ```
2. यदि आपके पास पहले से Podfile नहीं है, तो इसे चलाकर बनाएं:
   ```bash
   pod init
   ```
   यह आपकी प्रोजेक्ट डायरेक्टरी में एक बेसिक `Podfile` जनरेट करता है।

---

### चरण 4: Podfile एडिट करें
1. `Podfile` को एक टेक्स्ट एडिटर में खोलें (जैसे `nano`, `vim`, या कोई भी कोड एडिटर जैसे VS Code):
   ```bash
   open Podfile
   ```
2. `Podfile` को `AVOSCloudIM` पॉड को वर्जन `3.1.6.2` के साथ शामिल करने के लिए संशोधित करें। यहाँ एक उदाहरण है कि आपका `Podfile` कैसा दिख सकता है:
   ```ruby
   platform :ios, '9.0'  # न्यूनतम iOS वर्जन निर्दिष्ट करें (आवश्यकतानुसार समायोजित करें)
   use_frameworks!       # वैकल्पिक: यदि आपका प्रोजेक्ट Swift या फ्रेमवर्क का उपयोग करता है तो इसका उपयोग करें

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # AVOSCloudIM वर्जन 3.1.6.2 को शामिल करने के लिए यह लाइन जोड़ें
   end
   ```
   - `'YourAppName'` को अपने Xcode टार्गेट के वास्तविक नाम से बदलें (आमतौर पर आपके ऐप का नाम)।
   - `platform :ios, '9.0'` लाइन न्यूनतम iOS वर्जन निर्दिष्ट करती है; इसे अपने प्रोजेक्ट की आवश्यकताओं के आधार पर समायोजित करें।
   - `use_frameworks!` की आवश्यकता तब होती है जब आपका प्रोजेक्ट Swift का उपयोग करता है या पॉड को डायनामिक फ्रेमवर्क की आवश्यकता होती है।

3. `Podfile` को सेव करें और बंद करें।

---

### चरण 5: पॉड इंस्टॉल करें
1. टर्मिनल में, अपनी प्रोजेक्ट की रूट डायरेक्टरी से निम्नलिखित कमांड चलाएं:
   ```bash
   pod install
   ```
   - यह `AVOSCloudIM` लाइब्रेरी (वर्जन 3.1.6.2) को आपके प्रोजेक्ट में डाउनलोड और एकीकृत करता है।
   - यदि सफल होता है, तो आपको आउटपुट कुछ इस तरह दिखाई देगा:  
     ```
     Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
     ```

2. यदि आपको एरर्स आती हैं (जैसे, पॉड नहीं मिला), तो सुनिश्चित करें कि वर्जन `3.1.6.2` अभी भी CocoaPods रिपॉजिटरी में उपलब्ध है। पुराने वर्जन अब सपोर्टेड नहीं हो सकते हैं। आप [CocoaPods.org](https://cocoapods.org) पर `AVOSCloudIM` के अंतर्गत नवीनतम वर्जन चेक कर सकते हैं या नए वर्जन पर अपडेट कर सकते हैं (जैसे `pod 'AVOSCloudIM', '~> 12.3'`)।

---

### चरण 6: वर्कस्पेस खोलें
1. इंस्टॉलेशन के बाद, आपकी प्रोजेक्ट डायरेक्टरी में एक `.xcworkspace` फ़ाइल बनाई जाएगी (जैसे `YourAppName.xcworkspace`)।
2. इस फ़ाइल को Xcode में खोलें:
   ```bash
   open YourAppName.xcworkspace
   ```
   - अब से, अपने प्रोजेक्ट के साथ काम करने के लिए हमेशा `.xcworkspace` फ़ाइल का उपयोग करें, न कि `.xcodeproj` फ़ाइल का।

---

### चरण 7: अपने कोड में AVOSCloudIM इम्पोर्ट करें और उपयोग करें
1. अपनी Swift या Objective-C फ़ाइलों में, `AVOSCloudIM` मॉड्यूल इम्पोर्ट करें:
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. लाइब्रेरी की सुविधाओं का उपयोग शुरू करें। `AVOSCloudIM` LeanCloud SDK का एक हिस्सा है, जिसका उपयोग आमतौर पर रीयल-टाइम मैसेजिंग के लिए किया जाता है। विशिष्ट उपयोग उदाहरणों के लिए [LeanCloud डॉक्यूमेंटेशन](https://leancloud.app/docs/) देखें, जैसे कि एक चैट क्लाइंट सेट अप करना:
   - उदाहरण (Swift):
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connected to LeanCloud IM!")
         } else {
             print("Error: \\(error?.localizedDescription ?? "Unknown")")
         }
     }
     ```

---

### चरण 8: अपने प्रोजेक्ट को कॉन्फ़िगर करें (यदि आवश्यक हो)
- **App Key और इनिशियलाइज़ेशन**: LeanCloud SDKs को अक्सर एक app ID और key की आवश्यकता होती है। यह इनिशियलाइज़ेशन कोड जोड़ें (जैसे `AppDelegate` में):
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - `"yourAppID"` और `"yourAppKey"` को अपने LeanCloud अकाउंट से क्रेडेंशियल्स के साथ बदलें।
- **पर्मिशन्स**: सुनिश्चित करें कि आपके ऐप में `Info.plist` में आवश्यक पर्मिशन्स हैं (जैसे, इंटरनेट एक्सेस):
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### नोट्स
- **वर्जन स्पेसिफिसिटी**: `pod 'AVOSCloudIM', '3.1.6.2'` का उपयोग आपको उसी एक्सैक्ट वर्जन तक लॉक कर देता है। यदि आप माइनर अपडेट्स के लिए लचीलापन चाहते हैं, तो `~>` का उपयोग करें (जैसे `pod 'AVOSCloudIM', '~> 3.1.6'` 3.1.6.1 जैसे अपडेट्स की अनुमति देता है लेकिन 3.2 की नहीं)।
- **ट्रबलशूटिंग**: यदि `pod install` फेल हो जाता है, तो आज़माएँ:
  - CocoaPods अपडेट करना: `sudo gem install cocoapods`
  - कैशे क्लियर करना: `pod cache clean --all`
  - लोकल CocoaPods स्पेक रिपॉजिटरी को रिफ्रेश करने के लिए `pod repo update` चलाना।
- **LeanCloud SDK**: चूंकि `AVOSCloudIM` LeanCloud का एक हिस्सा है, सुनिश्चित करें कि आप अतिरिक्त कॉन्फ़िगरेशन (जैसे, उनके प्लेटफ़ॉर्म पर रजिस्टर करना) के लिए उनकी सेटअप गाइड का पालन करते हैं।

---

बस हो गया! अब आपने `AVOSCloudIM` वर्जन 3.1.6.2 को अपने iOS प्रोजेक्ट में एकीकृत कर लिया है। इसे टेस्ट करने के लिए Xcode में अपना ऐप बिल्ड और रन करें। यदि आपको विशिष्ट LeanCloud सुविधाओं के साथ सहायता की आवश्यकता है तो मुझे बताएं!