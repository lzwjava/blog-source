---
audio: false
generated: true
lang: hi
layout: post
title: आईओएस में एएफनेटवर्किंग का उपयोग
translated: true
type: note
---

ऐसा लगता है कि आप AFNetworking लाइब्रेरी के संस्करण 2.5.4 को CocoaPods का उपयोग करके एक iOS प्रोजेक्ट में इंटीग्रेट करने की बात कर रहे हैं। CocoaPods, Swift और Objective-C प्रोजेक्ट्स के लिए एक लोकप्रिय डिपेंडेंसी मैनेजर है। यहां एक चरण-दर-चरण गाइड दी गई है कि कैसे अपने प्रोजेक्ट में `pod 'AFNetworking', '2.5.4'` का उपयोग करें:

### पूर्वापेक्षाएँ
1.  **CocoaPods इंस्टॉल करें**: यदि आपके पास CocoaPods इंस्टॉल नहीं है, तो इसे टर्मिनल में यह कमांड चलाकर इंस्टॉल करें:
    ```bash
    sudo gem install cocoapods
    ```
2.  **Xcode प्रोजेक्ट**: सुनिश्चित करें कि आपके पास एक मौजूदा Xcode प्रोजेक्ट है जहां आप AFNetworking जोड़ना चाहते हैं।

### `pod 'AFNetworking', '2.5.4'` का उपयोग करने के चरण

1.  **अपने प्रोजेक्ट डायरेक्टरी में नेविगेट करें**  
    अपना टर्मिनल खोलें और अपने Xcode प्रोजेक्ट (`.xcodeproj` फ़ाइल) वाली डायरेक्टरी में जाएं:
    ```bash
    cd /path/to/your/project
    ```

2.  **एक Podfile इनिशियलाइज़ करें**  
    यदि आपके पास पहले से `Podfile` नहीं है, तो इसे चलाकर बनाएं:
    ```bash
    pod init
    ```
    यह आपकी प्रोजेक्ट डायरेक्टरी में एक `Podfile` जनरेट करता है।

3.  **Podfile एडिट करें**  
    `Podfile` को एक टेक्स्ट एडिटर में खोलें (जैसे `nano Podfile` या VS Code जैसे किसी भी कोड एडिटर का उपयोग करें)। अपने ऐप के लिए `target` ब्लॉक के अंदर निम्नलिखित लाइन जोड़ें:
    ```ruby
    target 'YourAppTargetName' do
      # Comment the next line if you don't want to use dynamic frameworks
      use_frameworks!

      # Add this line to specify AFNetworking version 2.5.4
      pod 'AFNetworking', '2.5.4'
    end
    ```
    `'YourAppTargetName'` को अपने ऐप के वास्तविक टार्गेट नाम से बदलें (आप इसे Xcode में अपनी प्रोजेक्ट सेटिंग्स के तहत देख सकते हैं)।

    उदाहरण `Podfile`:
    ```ruby
    platform :ios, '9.0'

    target 'MyApp' do
      use_frameworks!
      pod 'AFNetworking', '2.5.4'
    end
    ```

4.  **Pod इंस्टॉल करें**  
    `Podfile` को सेव करें, फिर AFNetworking 2.5.4 को इंस्टॉल करने के लिए टर्मिनल में निम्नलिखित कमांड चलाएं:
    ```bash
    pod install
    ```
    यह निर्दिष्ट संस्करण वाली AFNetworking को डाउनलोड करती है और आपके प्रोजेक्ट में सेट अप करती है। यदि यह काम करती है तो आपको सफलता का संदेश दिखाई देगा।

5.  **वर्कस्पेस खोलें**  
    इंस्टॉलेशन के बाद, CocoaPods एक `.xcworkspace` फ़ाइल बनाता है। इस फ़ाइल को (जैसे, `MyApp.xcworkspace`) Xcode में ओरिजिनल `.xcodeproj` फ़ाइल के बजाय खोलें:
    ```bash
    open MyApp.xcworkspace
    ```

6.  **AFNetworking इम्पोर्ट करें और उपयोग करें**  
    अपने Objective-C या Swift कोड में, AFNetworking इम्पोर्ट करें और इसका उपयोग शुरू करें। चूंकि संस्करण 2.5.4 पुराना है और Objective-C में लिखा गया है, इसका उपयोग कैसे करें यहां बताया गया है:

    - **Objective-C**:
      अपनी `.h` या `.m` फ़ाइल में:
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

    - **Swift (with Bridging Header)**:  
      यदि आप Swift का उपयोग कर रहे हैं, तो इस Objective-C लाइब्रेरी का उपयोग करने के लिए एक ब्रिजिंग हेडर बनाएं:
      - `YourApp-Bridging-Header.h` नाम की एक फ़ाइल जोड़ें (जैसे, `MyApp-Bridging-Header.h`)।
      - ब्रिजिंग हेडर में, यह जोड़ें:
        ```objective-c
        #import <AFNetworking/AFNetworking.h>
        ```
      - Xcode में, Build Settings > "Objective-C Bridging Header" पर जाएं और अपने ब्रिजिंग हेडर का पथ सेट करें (जैसे, `MyApp/MyApp-Bridging-Header.h`)।
      - फिर अपनी Swift फ़ाइल में:
        ```swift
        func makeRequest() {
            let manager = AFHTTPRequestOperationManager()
            manager.get("https://api.example.com/data", 
                        parameters: nil, 
                        success: { (operation, response) in
                            print("Success: \\(response)")
                        }, 
                        failure: { (operation, error) in
                            print("Error: \\(error)")
                        })
        }
        ```

7.  **बिल्ड और रन करें**  
    सुनिश्चित करने के लिए कि सब कुछ सही से सेट है, Xcode में अपना प्रोजेक्ट बिल्ड करें (`Cmd + B`)। यदि आपको कोई एरर आते हैं, तो अपने Podfile की सिंटैक्स जांचें या सुनिश्चित करें कि सही वर्कस्पेस खुला है।

### नोट्स
-   **संस्करण 2.5.4**: यह AFNetworking का एक पुराना संस्करण है (लगभग 2015 में रिलीज़ हुआ)। मार्च 2025 तक इसका नवीनतम संस्करण संभवतः काफी नया है (जैसे, 4.x या 5.x)। जब तक कि आपको कॉम्पैटिबिलिटी के लिए विशेष रूप से 2.5.4 की आवश्यकता न हो, नवीनतम संस्करण पाने के लिए `pod 'AFNetworking'` का उपयोग करने पर विचार करें।
-   **Deprecation**: AFNetworking के पुराने APIs (जैसे `AFHTTPRequestOperationManager`) नए संस्करणों में deprecated हैं। आधुनिक प्रोजेक्ट्स के लिए, Alamofire (एक Swift विकल्प) जैसी लाइब्रेरीज पर विचार करना उचित हो सकता है।
-   **प्लेटफ़ॉर्म**: सुनिश्चित करें कि आपका `Podfile` एक प्लेटफ़ॉर्म संस्करण निर्दिष्ट करता है जो AFNetworking 2.5.4 के साथ कॉम्पैटिबल है (जैसे, `platform :ios, '9.0'`)।

यदि आपको कोई विशेष समस्या आती है (जैसे, इंस्टॉलेशन एरर या कोड उदाहरण काम नहीं कर रहे), तो मुझे बताएं, और मैं और समस्या निवारण करूंगा! आपका अगला कदम या प्रश्न क्या है?