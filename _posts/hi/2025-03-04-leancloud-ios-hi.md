---
audio: false
generated: true
lang: hi
layout: post
title: लीनक्लाउड आईओएस एसडीके
translated: true
type: note
---

`pod 'AVOSCloud', '3.1.6.2'` का उपयोग iOS प्रोजेक्ट में करने के लिए, आप AVOSCloud SDK (संभवतः LeanCloud का क्लाउड सेवाओं के लिए SDK) को CocoaPods के माध्यम से इंटीग्रेट कर रहे हैं। यहाँ इसे सेट अप करने के लिए चरण-दर-चरण मार्गदर्शिका दी गई है:

---

### पूर्वापेक्षाएँ
1.  **CocoaPods इंस्टॉल करें**: यदि आपके पास CocoaPods इंस्टॉल नहीं है, तो पहले इसे अपने टर्मिनल में यह चलाकर इंस्टॉल करें:
    ```bash
    sudo gem install cocoapods
    ```
2.  **Xcode प्रोजेक्ट**: सुनिश्चित करें कि आपके पास Xcode में एक मौजूदा iOS प्रोजेक्ट है।

---

### `pod 'AVOSCloud', '3.1.6.2'` का उपयोग करने के चरण

1.  **अपने प्रोजेक्ट डायरेक्टरी में नेविगेट करें**:
    अपना टर्मिनल खोलें और उस डायरेक्टरी पर जाएँ जिसमें आपकी `.xcodeproj` फ़ाइल है:
    ```bash
    cd /path/to/your/project
    ```

2.  **एक Podfile इनिशियलाइज़ करें** (यदि आपके पास पहले से एक नहीं है):
    एक `Podfile` बनाने के लिए निम्नलिखित कमांड चलाएँ:
    ```bash
    pod init
    ```

3.  **Podfile एडिट करें**:
    `Podfile` को एक टेक्स्ट एडिटर में खोलें (जैसे, `nano Podfile` या `open Podfile`) और विशिष्ट वर्जन `3.1.6.2` के साथ `AVOSCloud` पॉड एड करें। आपका `Podfile` कुछ इस तरह दिखना चाहिए:
    ```ruby
    platform :ios, '9.0'  # न्यूनतम iOS वर्जन निर्दिष्ट करें (आवश्यकतानुसार समायोजित करें)

    target 'YourAppName' do
      use_frameworks!
      pod 'AVOSCloud', '3.1.6.2'  # AVOSCloud SDK के लिए यह लाइन एड करें
    end
    ```
    - `'YourAppName'` को अपने Xcode टार्गेट के वास्तविक नाम से बदलें।
    - `use_frameworks!` आवश्यक है यदि आप Swift या डायनामिक फ्रेमवर्क्स का उपयोग कर रहे हैं।

4.  **पॉड इंस्टॉल करें**:
    `Podfile` को सेव करें, फिर AVOSCloud के निर्दिष्ट वर्जन को इंस्टॉल करने के लिए टर्मिनल में यह कमांड चलाएँ:
    ```bash
    pod install
    ```
    - यह AVOSCloud SDK का वर्जन `3.1.6.2` डाउनलोड करेगा और आपके प्रोजेक्ट को एक `.xcworkspace` फ़ाइल के साथ सेट अप करेगा।

5.  **वर्कस्पेस खोलें**:
    इंस्टॉलेशन के बाद, अपना `.xcodeproj` बंद करें यदि यह खुला है, और नई बनाई गई `.xcworkspace` फ़ाइल खोलें:
    ```bash
    open YourAppName.xcworkspace
    ```

6.  **अपने कोड में AVOSCloud इम्पोर्ट और उपयोग करें**:
    - Objective-C में:
      ```objc
      #import <AVOSCloud/AVOSCloud.h>

      - (void)example {
          [AVOSCloud setApplicationId:@"your_app_id" clientKey:@"your_client_key"];
          AVObject *testObject = [AVObject objectWithClassName:@"TestObject"];
          [testObject setObject:@"Hello" forKey:@"message"];
          [testObject save];
      }
      ```
    - Swift में:
      ```swift
      import AVOSCloud

      func example() {
          AVOSCloud.setApplicationId("your_app_id", clientKey: "your_client_key")
          let testObject = AVObject(className: "TestObject")
          testObject["message"] = "Hello"
          try? testObject.save()
      }
      ```
    - `"your_app_id"` और `"your_client_key"` को LeanCloud डैशबोर्ड से प्राप्त अपनी ऐप क्रेडेंशियल्स से बदलें।

7.  **ऐप क्रेडेंशियल्स कॉन्फ़िगर करें**:
    - [LeanCloud](https://leancloud.app) (या संबंधित AVOSCloud सेवा प्रदाता) पर साइन अप करें।
    - अपनी ऐप की सेटिंग्स से अपना `App ID` और `Client Key` प्राप्त करें और उन्हें अपने कोड में सेट करें (जैसा ऊपर दिखाया गया है)।

8.  **बिल्ड और रन करें**:
    सुनिश्चित करने के लिए कि सब कुछ सही से सेट अप हो गया है, Xcode में अपना प्रोजेक्ट बिल्ड करें (`Cmd + B`)। यदि कोई एरर हैं, तो अपने Podfile की सिंटैक्स या नेटवर्क कनेक्शन जांचें।

---

### नोट्स
-   **वर्जन विशिष्ट**: `'3.1.6.2'` निर्दिष्ट करके, आप SDK को उसी सटीक वर्जन पर लॉक कर रहे हैं। 03 मार्च, 2025 तक यह पुराना हो सकता है। नवीनतम वर्जन का उपयोग करने के लिए, बिना वर्जन नंबर के केवल `pod 'AVOSCloud'` लिखें।
-   **कम्पैटिबिलिटी**: सुनिश्चित करें कि वर्जन `3.1.6.2` आपके iOS डिप्लॉयमेंट टार्गेट (जैसे, iOS 9.0 या उच्चतर) को सपोर्ट करता है। विवरण के लिए [LeanCloud डॉक्यूमेंटेशन](https://leancloud.app/docs) जांचें।
-   **पॉड अपडेट**: यदि आपको CocoaPods को अपडेट करने या ट्रबलशूट करने की आवश्यकता है, तो चलाएँ:
    ```bash
    pod update
    ```
-   **ट्रबलशूटिंग**: यदि `pod install` फेल हो जाता है, तो यह कोशिश करें:
    ```bash
    pod repo update
    pod install --verbose
    ```

---

मुझे बताएं यदि आपको किसी विशिष्ट भाग, जैसे AVOSCloud से किसी फीचर (जैसे, पुश नोटिफिकेशन, रियल-टाइम मैसेजिंग) को इंटीग्रेट करने में सहायता की आवश्यकता है!