---
audio: false
generated: true
lang: hi
layout: post
title: LeanCloud Realtime iOS SDK का अनुवाद
translated: true
---

`pod 'AVOSCloudIM', '3.1.6.2'` को अपने iOS प्रोजेक्ट में CocoaPods के साथ उपयोग करने के लिए, इन चरणों का पालन करें। यह मानता है कि आपके पास CocoaPods इंस्टॉल है और आप Xcode के साथ बुनियादी iOS विकास से परिचित हैं।

---

### चरण 1: CocoaPods सेट अप करें (अगर पहले से नहीं किया गया है)
अगर आपने अभी तक CocoaPods इंस्टॉल नहीं किया है, तो टर्मिनल के माध्यम से इसे इंस्टॉल करें:
```bash
sudo gem install cocoapods
```
इंस्टॉलेशन की पुष्टि करें:
```bash
pod --version
```

---

### चरण 2: अपने Xcode प्रोजेक्ट को खोलें या बनाएं
1. अपने मौजूदा Xcode प्रोजेक्ट को खोलें या Xcode में नया बनाएं।
2. अभी के लिए Xcode को बंद करें (हम बाद में वर्कस्पेस के साथ इसे फिर से खोलेंगे).

---

### चरण 3: एक Podfile को प्रारंभ करें
1. अपने टर्मिनल को खोलें और अपने प्रोजेक्ट के रूट डायरेक्टरी में जाएं (जहां `.xcodeproj` फ़ाइल है):
   ```bash
   cd /path/to/your/project
   ```
2. अगर आपके पास पहले से Podfile नहीं है, तो इसे बनाएं:
   ```bash
   pod init
   ```
   यह आपके प्रोजेक्ट डायरेक्टरी में एक बुनियादी `Podfile` बनाता है।

---

### चरण 4: Podfile को संपादित करें
1. एक टेक्स्ट एडिटर में `Podfile` को खोलें (जैसे `nano`, `vim`, या किसी भी कोड एडिटर जैसे VS Code):
   ```bash
   open Podfile
   ```
2. `Podfile` को `AVOSCloudIM` पॉड के साथ संस्करण `3.1.6.2` शामिल करने के लिए संपादित करें। यहाँ आपके `Podfile` का उदाहरण है:
   ```ruby
   platform :ios, '9.0'  # न्यूनतम iOS संस्करण को निर्दिष्ट करें (अनुसार समायोजित करें)
   use_frameworks!       # विकल्प: इसको तब उपयोग करें जब आपके प्रोजेक्ट में Swift या फ्रेमवर्क हैं

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # इस लाइन को `AVOSCloudIM` संस्करण 3.1.6.2 को शामिल करने के लिए जोड़ें
   end
   ```
   - `'YourAppName'` को अपने Xcode टारगेट का वास्तविक नाम से बदलें (आम तौर पर आपके ऐप का नाम होता है).
   - `platform :ios, '9.0'` लाइन न्यूनतम iOS संस्करण को निर्दिष्ट करती है; इसे अपने प्रोजेक्ट के आवश्यकताओं के अनुसार समायोजित करें।
   - `use_frameworks!` तब आवश्यक है जब आपके प्रोजेक्ट में Swift है या जब पॉड डायनामिक फ्रेमवर्क की आवश्यकता होती है।

3. `Podfile` को बचाएं और बंद करें।

---

### चरण 5: पॉड को इंस्टॉल करें
1. टर्मिनल में अपने प्रोजेक्ट के रूट डायरेक्टरी से निम्नलिखित कमांड चलाएं:
   ```bash
   pod install
   ```
   - यह `AVOSCloudIM` लाइब्रेरी (संस्करण 3.1.6.2) को आपके प्रोजेक्ट में डाउनलोड और एकीकृत करता है।
   - अगर सफल, तो आप निम्नलिखित प्रकार के आउटपुट देखेंगे:
     ```
     Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
     ```

2. अगर आप किसी त्रुटि से सामना करते हैं (जैसे पॉड नहीं मिला), तो सुनिश्चित करें कि संस्करण `3.1.6.2` अभी भी CocoaPods रिपॉजिटरी में उपलब्ध है। पुराने संस्करण संभवतः अब समर्थित नहीं हैं। आप [CocoaPods.org](https://cocoapods.org) पर `AVOSCloudIM` के नीचे नवीनतम संस्करण की जांच कर सकते हैं या नवीनतम संस्करण पर अपडेट कर सकते हैं (जैसे `pod 'AVOSCloudIM', '~> 12.3'`).

---

### चरण 6: वर्कस्पेस को खोलें
1. इंस्टॉलेशन के बाद, आपके प्रोजेक्ट डायरेक्टरी में एक `.xcworkspace` फ़ाइल बन जाएगी (जैसे `YourAppName.xcworkspace`).
2. इस फ़ाइल को Xcode में खोलें:
   ```bash
   open YourAppName.xcworkspace
   ```
   - अब से, हमेशा `.xcworkspace` फ़ाइल का उपयोग करके अपने प्रोजेक्ट के साथ काम करें, न कि `.xcodeproj` फ़ाइल का।

---

### चरण 7: अपने कोड में AVOSCloudIM को आयात और उपयोग करें
1. अपने Swift या Objective-C फ़ाइलों में `AVOSCloudIM` मॉड्यूल को आयात करें:
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. लाइब्रेरी के विशेषताओं का उपयोग शुरू करें। `AVOSCloudIM` LeanCloud SDK का हिस्सा है, आम तौर पर वास्तविक समय संदेशवाहक के लिए उपयोग किया जाता है। विशेष उपयोग उदाहरणों के लिए [LeanCloud दस्तावेज़](https://leancloud.app/docs/) पर संदर्भ करें, जैसे एक चैट क्लाइंट सेट अप:
   - उदाहरण (Swift):
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connected to LeanCloud IM!")
         } else {
             print("Error: \(error?.localizedDescription ?? "Unknown")")
         }
     }
     ```

---

### चरण 8: अपने प्रोजेक्ट को सेट अप करें (अगर आवश्यक है)
- **App Key और प्रारंभिकरण**: LeanCloud SDKs अक्सर एक ऐप आईडी और कुंजी की आवश्यकता होती हैं। इस प्रारंभिकरण कोड को जोड़ें (जैसे `AppDelegate` में):
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - `"yourAppID"` और `"yourAppKey"` को अपने LeanCloud खाते से क्रेडेंशियल्स से बदलें।
- **अनुमतियाँ**: सुनिश्चित करें कि आपके ऐप में `Info.plist` में आवश्यक अनुमतियाँ हैं (जैसे इंटरनेट एक्सेस):
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### नोट्स
- **संस्करण विशेषता**: `pod 'AVOSCloudIM', '3.1.6.2'` का उपयोग उस विशिष्ट संस्करण पर लॉक करता है। अगर आप छोटे अपडेट के लिए लचीलापन चाहते हैं, तो `~>` का उपयोग करें (जैसे `pod 'AVOSCloudIM', '~> 3.1.6'` 3.1.6.1 जैसे अपडेट को अनुमति देता है लेकिन 3.2 नहीं).
- **संघर्ष**: अगर `pod install` विफल हो जाता है, तो कोशिश करें:
  - CocoaPods को अपडेट करें: `sudo gem install cocoapods`
  - कैश को साफ करें: `pod cache clean --all`
  - `pod repo update` चलाएं ताकि स्थानीय CocoaPods spec रिपॉजिटरी को नवीनीकृत करें।
- **LeanCloud SDK**: क्योंकि `AVOSCloudIM` LeanCloud का हिस्सा है, सुनिश्चित करें कि आप उनके सेट अप गाइड का पालन करते हैं (जैसे उनके प्लेटफॉर्म पर पंजीकरण करना).

---

यह है! अब आपने `AVOSCloudIM` संस्करण 3.1.6.2 को अपने iOS प्रोजेक्ट में एकीकृत कर लिया है। अपने ऐप को Xcode में बनाएं और चलाएं ताकि इसे टेस्ट किया जा सके। अगर आपको LeanCloud विशेषताओं के साथ मदद चाहिए, तो मुझे बताएं!