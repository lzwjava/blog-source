---
audio: false
generated: true
lang: hi
layout: post
title: AFNetworking का उपयोग iOS में
translated: true
---

यह लगता है कि आप AFNetworking लाइब्रेरी का संस्करण 2.5.4 को CocoaPods, एक लोकप्रिय Swift और Objective-C प्रोजेक्ट्स के लिए निर्भरता प्रबंधक, का उपयोग करके एक iOS प्रोजेक्ट में एकीकृत करने की बात कर रहे हैं। यहाँ `pod 'AFNetworking', '2.5.4'` का उपयोग करने के लिए आपके प्रोजेक्ट में एक चरण-दर-चरण मार्गदर्शिका है:

### पूर्वापेक्षाएँ
1. **CocoaPods इंस्टॉल करें**: अगर आपके पास CocoaPods इंस्टॉल नहीं है, तो इसे इंस्टॉल करने के लिए अपने टर्मिनल में इस कमांड को चलाएं:
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode प्रोजेक्ट**: सुनिश्चित करें कि आपके पास एक मौजूदा Xcode प्रोजेक्ट है जहां आप AFNetworking जोड़ना चाहते हैं।

### `pod 'AFNetworking', '2.5.4'` का उपयोग करने के चरण

1. **अपने प्रोजेक्ट डायरेक्टरी में जाएं**
   अपने टर्मिनल खोलें और अपने Xcode प्रोजेक्ट (`.xcodeproj` फ़ाइल) को रखने वाले डायरेक्टरी में जाएं:
   ```bash
   cd /path/to/your/project
   ```

2. **एक Podfile शुरू करें**
   अगर आपके पास पहले से कोई `Podfile` नहीं है, तो इसे बनाने के लिए निम्नलिखित कमांड चलाएं:
   ```bash
   pod init
   ```
   यह आपके प्रोजेक्ट डायरेक्टरी में एक `Podfile` पैदा करता है।

3. **Podfile को संपादित करें**
   एक टेक्स्ट एडिटर (जैसे `nano Podfile` या किसी भी कोड एडिटर जैसे VS Code) में `Podfile` खोलें। अपने ऐप के लिए `target` ब्लॉक के अंदर निम्नलिखित लाइन जोड़ें:
   ```ruby
   target 'YourAppTargetName' do
     # अगले लाइन को टिप्पणी करें अगर आप डायनामिक फ्रेमवर्क का उपयोग नहीं करना चाहते
     use_frameworks!

     # इस लाइन को AFNetworking संस्करण 2.5.4 को स्पष्ट करने के लिए जोड़ें
     pod 'AFNetworking', '2.5.4'
   end
   ```
   `'YourAppTargetName'` को अपने ऐप का वास्तविक टारगेट नाम से बदलें (आप इसे Xcode में अपने प्रोजेक्ट सेटिंग्स के तहत पा सकते हैं)।

   उदाहरण `Podfile`:
   ```ruby
   platform :ios, '9.0'

   target 'MyApp' do
     use_frameworks!
     pod 'AFNetworking', '2.5.4'
   end
   ```

4. **Pod को इंस्टॉल करें**
   `Podfile` को सेभ करें, फिर निम्नलिखित कमांड को टर्मिनल में चलाएं AFNetworking 2.5.4 को इंस्टॉल करने के लिए:
   ```bash
   pod install
   ```
   यह निर्दिष्ट संस्करण AFNetworking को डाउनलोड करता है और इसे आपके प्रोजेक्ट में सेट अप करता है। अगर यह काम करता है, तो आप सफलता का संदेश देखेंगे।

5. **वर्कस्पेस को खोलें**
   इंस्टॉलेशन के बाद, CocoaPods एक `.xcworkspace` फ़ाइल पैदा करता है। इस फ़ाइल (जैसे `MyApp.xcworkspace`) को खोलें (Xcode में) मूल `.xcodeproj` फ़ाइल के बजाय:
   ```bash
   open MyApp.xcworkspace
   ```

6. **AFNetworking को आयात और उपयोग करें**
   अपने Objective-C या Swift कोड में AFNetworking को आयात करें और इसका उपयोग शुरू करें। संस्करण 2.5.4 पुराना है और Objective-C में लिखा गया है, इसलिए इसका उपयोग करने के लिए:

   - **Objective-C**:
     अपने `.h` या `.m` फ़ाइल में:
     ```objective-c
     #import <AFNetworking/AFNetworking.h>

     - (void)makeRequest {
         AFHTTPRequestOperationManager *manager = [AFHTTPRequestOperationManager manager];
         [manager GET:@"https://api.example.com/data"
           parameters:nil
              success:^(AFHTTPRequestOperation *operation, id responseObject) {
                  NSLog(@"Success: %@", responseObject);
              }
              failure:^(AFHTTPRequestOperation *operation, NSError *error) {
                  NSLog(@"Error: %@", error);
              }];
     }
     ```

   - **Swift (साथ ब्रिजिंग हेडर)**:
     अगर आप Swift का उपयोग कर रहे हैं, तो इस Objective-C लाइब्रेरी का उपयोग करने के लिए एक ब्रिजिंग हेडर बनाएं:
     - एक फ़ाइल का नाम `YourApp-Bridging-Header.h` (जैसे `MyApp-Bridging-Header.h`) जोड़ें।
     - ब्रिजिंग हेडर में, निम्नलिखित जोड़ें:
       ```objective-c
       #import <AFNetworking/AFNetworking.h>
       ```
     - Xcode में, Build Settings > “Objective-C Bridging Header” पर जाएं और अपने ब्रिजिंग हेडर के पथ को सेट करें (जैसे `MyApp/MyApp-Bridging-Header.h`).
     - फिर अपने Swift फ़ाइल में:
       ```swift
       func makeRequest() {
           let manager = AFHTTPRequestOperationManager()
           manager.get("https://api.example.com/data",
                       parameters: nil,
                       success: { (operation, response) in
                           print("Success: \(response)")
                       },
                       failure: { (operation, error) in
                           print("Error: \(error)")
                       })
       }
       ```

7. **बनाएं और चलाएं**
   Xcode में अपना प्रोजेक्ट बनाएं (`Cmd + B`) सुनिश्चित करने के लिए कि सब कुछ सही से सेट अप है। अगर आप किसी भी त्रुटि से जूझ रहे हैं, तो अपने Podfile सिंटैक्स को जांचें या सुनिश्चित करें कि सही वर्कस्पेस खुला है।

### टिप्पणियाँ
- **संस्करण 2.5.4**: यह AFNetworking का एक पुराना संस्करण है (2015 के आसपास रिलीज़ किया गया था)। मार्च 2025 तक की तारीख के अनुसार, नवीनतम संस्करण बहुत नया हो सकता है (जैसे 4.x या 5.x)। जब तक आप 2.5.4 के लिए संगतता की आवश्यकता नहीं है, `pod 'AFNetworking'` को बिना संस्करण के उपयोग करने की सोचें ताकि नवीनतम संस्करण प्राप्त हो सके।
- **विलुप्त**: AFNetworking के पुराने एपीआई (जैसे `AFHTTPRequestOperationManager`) नए संस्करणों में विलुप्त हैं। आधुनिक प्रोजेक्टों के लिए, जैसे Alamofire (एक Swift विकल्प) का पता लगाने का विचार करें।
- **प्लेटफॉर्म**: सुनिश्चित करें कि आपके `Podfile` में AFNetworking 2.5.4 के साथ संगत प्लेटफॉर्म संस्करण स्पष्ट किया गया है (जैसे `platform :ios, '9.0'`).

अगर आप किसी विशेष समस्या से जूझ रहे हैं (जैसे इंस्टॉलेशन त्रुटियाँ या कोड उदाहरण काम नहीं करते), तो मुझे बताएं, और मैं आगे की समस्या सुलझाने में मदद करूँगा! आपका अगला कदम या सवाल क्या है?