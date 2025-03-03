---
audio: false
generated: true
lang: hi
layout: post
title: LeanCloud iOS SDK का उपयोग
translated: true
---

`pod 'AVOSCloud', '3.1.6.2'` को एक iOS प्रोजेक्ट में उपयोग करने के लिए, आप CocoaPods, एक iOS प्रोजेक्ट के लिए एक निर्भरता प्रबंधक, के माध्यम से AVOSCloud SDK (संभावित LeanCloud के लिए क्लाउड सर्विसेज के लिए SDK) को एकीकृत करने की ओर इशारा कर रहे हैं। यहां एक चरण-दर-चरण गाइड है इसे सेट अप करने के लिए:

---

### पूर्वापेक्षाएँ
1. **CocoaPods इंस्टॉल करें**: अगर आपके पास CocoaPods इंस्टॉल नहीं है, तो इसे पहले इंस्टॉल करें, अपने टर्मिनल में यह चलाएं:
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode प्रोजेक्ट**: सुनिश्चित करें कि आपके पास एक मौजूदा iOS प्रोजेक्ट Xcode में है।

---

### `pod 'AVOSCloud', '3.1.6.2'` का उपयोग करने के चरण

1. **अपने प्रोजेक्ट डायरेक्टरी में जाएं**:
   अपने टर्मिनल खोलें और `.xcodeproj` फ़ाइल को रखने वाले डायरेक्टरी में जाएं:
   ```bash
   cd /path/to/your/project
   ```

2. **एक Podfile को प्रारंभ करें** (अगर आपके पास पहले से कोई नहीं है):
   एक `Podfile` बनाने के लिए निम्नलिखित कमांड चलाएं:
   ```bash
   pod init
   ```

3. **Podfile को संपादित करें**:
   एक टेक्स्ट एडिटर में `Podfile` खोलें (जैसे `nano Podfile` या `open Podfile`) और `AVOSCloud` पॉड को विशिष्ट संस्करण `3.1.6.2` के साथ जोड़ें। आपके `Podfile` को कुछ इस तरह दिखना चाहिए:
   ```ruby
   platform :ios, '9.0'  # न्यूनतम iOS संस्करण को निर्दिष्ट करें (अनुसार समायोजित करें)

   target 'YourAppName' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # AVOSCloud SDK के लिए यह लाइन जोड़ें
   end
   ```
   - `'YourAppName'` को अपने Xcode टारगेट के वास्तविक नाम से बदलें।
   - `use_frameworks!` आवश्यक है अगर आप Swift या डायनामीक फ्रेमवर्क का उपयोग कर रहे हैं।

4. **पॉड को इंस्टॉल करें**:
   `Podfile` को सेभ करें, फिर इस कमांड को टर्मिनल में चलाएं `3.1.6.2` संस्करण के AVOSCloud को इंस्टॉल करने के लिए:
   ```bash
   pod install
   ```
   - यह संस्करण `3.1.6.2` को डाउनलोड करेगा AVOSCloud SDK और आपके प्रोजेक्ट को एक `.xcworkspace` फ़ाइल के साथ सेट अप करेगा।

5. **वर्कस्पेस को खोलें**:
   इंस्टॉलेशन के बाद, अगर खुला है तो अपने `.xcodeproj` को बंद करें, और नए बनाए गए `.xcworkspace` फ़ाइल को खोलें:
   ```bash
   open YourAppName.xcworkspace
   ```

6. **AVOSCloud को अपने कोड में आयात और उपयोग करें**:
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
   - `"your_app_id"` और `"your_client_key"` को LeanCloud के डैशबोर्ड से अपने ऐप क्रेडेंशियल्स से बदलें।

7. **ऐप क्रेडेंशियल्स को कॉन्फ़िगर करें**:
   - [LeanCloud](https://leancloud.app) (या संबंधित AVOSCloud सेवा प्रदाता) पर साइन अप करें।
   - अपने ऐप के सेटिंग्स से अपना `App ID` और `Client Key` प्राप्त करें और अपने कोड में सेट करें (उपरोक्त दिखाया गया है)।

8. **बिल्ड और चलाएं**:
   Xcode में अपना प्रोजेक्ट बिल्ड करें (`Cmd + B`) सुनिश्चित करने के लिए कि सब कुछ सही से सेट अप है। अगर कोई त्रुटियां हैं, तो अपने Podfile सिंटैक्स या नेटवर्क कनेक्शन की जांच करें।

---

### नोट्स
- **वर्सन विशिष्ट**: `'3.1.6.2'` को निर्दिष्ट करके, आप SDK को उस विशिष्ट संस्करण पर लॉक कर रहे हैं। यह 03 मार्च, 2025 तक पुराना हो सकता है। नवीनतम संस्करण का उपयोग करने के लिए, बस `pod 'AVOSCloud'` संस्करण संख्या के बिना लिखें।
- **संगतता**: सुनिश्चित करें कि संस्करण `3.1.6.2` आपके iOS डिप्लॉयमेंट टारगेट (जैसे iOS 9.0 या ऊपर) को समर्थन करता है। [LeanCloud दस्तावेज़](https://leancloud.app/docs) के लिए विवरण देखें।
- **Pod अपडेट**: अगर आपको CocoaPods को अपडेट करना है या समस्या का समाधान करना है, तो चलाएं:
  ```bash
  pod update
  ```
- **समस्या निपटान**: अगर `pod install` विफल हो जाता है, तो कोशिश करें:
  ```bash
  pod repo update
  pod install --verbose
  ```

---

मुझे बताएं अगर आपको किसी विशेष हिस्से में मदद चाहिए, जैसे कि AVOSCloud से एक विशेषताओं (जैसे पुश नोटिफिकेशन, रियल-टाइम मैसेजिंग) को एकीकृत करने में!