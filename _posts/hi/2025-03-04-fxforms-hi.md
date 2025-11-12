---
audio: false
generated: true
lang: hi
layout: post
title: आईओएस में एफएक्सफॉर्म्स का उपयोग
translated: true
type: note
---

ऐसा लगता है कि आप CocoaPods का उपयोग करके `FXForms` लाइब्रेरी को एक iOS प्रोजेक्ट में इंटीग्रेट करने की बात कर रहे हैं। CocoaPods Swift और Objective-C प्रोजेक्ट्स के लिए एक लोकप्रिय डिपेंडेंसी मैनेजर है। आपके प्रोजेक्ट में `pod 'FXForms', '1.2.13'` का उपयोग करने में मदद के लिए यहां एक चरण-दर-चरण मार्गदर्शिका दी गई है:

---

### पूर्वापेक्षाएँ
1.  **CocoaPods इंस्टॉल करें**: यदि आपकी मशीन पर CocoaPods इंस्टॉल नहीं है, तो पहले इसे अपने टर्मिनल में यह कमांड चलाकर इंस्टॉल करें:
    ```bash
    sudo gem install cocoapods
    ```
2.  **Xcode प्रोजेक्ट**: सुनिश्चित करें कि आपके पास एक मौजूदा Xcode प्रोजेक्ट है जहां आप `FXForms` को इंटीग्रेट करना चाहते हैं।

---

### `pod 'FXForms', '1.2.13'` का उपयोग करने के चरण

#### 1. **अपने प्रोजेक्ट डायरेक्टरी में नेविगेट करें**
अपना टर्मिनल खोलें और उस डायरेक्टरी में जाएं जहां आपका Xcode प्रोजेक्ट (`.xcodeproj` फ़ाइल) मौजूद है:
```bash
cd /path/to/your/project
```

#### 2. **एक Podfile इनिशियलाइज़ करें (यदि पहले से मौजूद नहीं है)**
यदि आपकी प्रोजेक्ट डायरेक्टरी में पहले से कोई `Podfile` मौजूद नहीं है, तो इसे चलाकर बनाएं:
```bash
pod init
```
यह आपकी प्रोजेक्ट डायरेक्टरी में एक `Podfile` जेनरेट करेगा।

#### 3. **Podfile एडिट करें**
`Podfile` को एक टेक्स्ट एडिटर (जैसे `nano`, `vim`, या कोई कोड एडिटर जैसे VS Code) में खोलें और विशिष्ट वर्जन `1.2.13` के साथ `FXForms` पॉड एड करें। आपका `Podfile` कुछ इस तरह दिखना चाहिए:

```ruby
platform :ios, '9.0'  # न्यूनतम iOS वर्जन निर्दिष्ट करें (आवश्यकतानुसार समायोजित करें)
use_frameworks!       # वैकल्पिक, शामिल करें यदि आप Swift या फ़्रेमवर्क का उपयोग कर रहे हैं

target 'YourProjectName' do
  # YourProjectName के लिए Pods
  pod 'FXForms', '1.2.13'
end
```

- `'YourProjectName'` को अपने Xcode टार्गेट के वास्तविक नाम से बदलें (आप इसे Xcode में अपनी प्रोजेक्ट सेटिंग्स के तहत देख सकते हैं)।
- लाइन `pod 'FXForms', '1.2.13'` निर्दिष्ट करती है कि आप `FXForms` लाइब्रेरी का वर्जन `1.2.13` चाहते हैं।

#### 4. **पॉड इंस्टॉल करें**
`Podfile` को सेव करें, फिर `FXForms` के निर्दिष्ट वर्जन को इंस्टॉल करने के लिए अपने टर्मिनल में निम्नलिखित कमांड चलाएं:
```bash
pod install
```
यह आपके प्रोजेक्ट में `FXForms` वर्जन `1.2.13` को डाउनलोड और इंटीग्रेट कर देगा। यदि सफल होता है, तो आप आउटपुट देखेंगे जो इंगित करेगा कि पॉड्स इंस्टॉल हो गए हैं।

#### 5. **वर्कस्पेस खोलें**
`pod install` चलाने के बाद, आपकी प्रोजेक्ट डायरेक्टरी में एक `.xcworkspace` फ़ाइल बनेगी। इस फ़ाइल को (`.xcodeproj` नहीं) Xcode में खोलें:
```bash
open YourProjectName.xcworkspace
```

#### 6. **अपने कोड में FXForms का उपयोग करें**
`FXForms` एक Objective-C लाइब्रेरी है जो iOS ऐप्स में फॉर्म बनाना सरल बनाती है। इसे उपयोग करने का एक बेसिक उदाहरण यहां दिया गया है:

- **FXForms इम्पोर्ट करें**: अपनी Objective-C फ़ाइल (जैसे, एक व्यू कंट्रोलर) में, लाइब्रेरी को इम्पोर्ट करें:
  ```objective-c
  #import <FXForms/FXForms.h>
  ```

- **एक फॉर्म मॉडल बनाएं**: एक क्लास डिफाइन करें जो `FXForm` प्रोटोकॉल का पालन करती हो। उदाहरण के लिए:
  ```objective-c
  // MyForm.h
  #import <Foundation/Foundation.h>
  #import <FXForms/FXForms.h>

  @interface MyForm : NSObject <FXForm>
  @property (nonatomic, copy) NSString *name;
  @property (nonatomic, copy) NSString *email;
  @end

  // MyForm.m
  #import "MyForm.h"

  @implementation MyForm
  - (NSArray *)fields {
      return @[
          @{FXFormFieldKey: @"name", FXFormFieldTitle: @"Name"},
          @{FXFormFieldKey: @"email", FXFormFieldTitle: @"Email"}
      ];
  }
  @end
  ```

- **फॉर्म डिस्प्ले करें**: अपने व्यू कंट्रोलर में, `FXFormViewController` का उपयोग करके फॉर्म प्रस्तुत करें:
  ```objective-c
  #import "MyForm.h"

  - (void)viewDidLoad {
      [super viewDidLoad];
      FXFormViewController *formController = [[FXFormViewController alloc] init];
      formController.form = [[MyForm alloc] init];
      [self.navigationController pushViewController:formController animated:YES];
  }
  ```

#### 7. **बिल्ड और रन करें**
सब कुछ सही से सेट अप है यह सुनिश्चित करने के लिए Xcode में अपना प्रोजेक्ट बिल्ड करें (`Cmd + B`), फिर इसे सिम्युलेटर या डिवाइस पर रन करें (`Cmd + R`).

---

### समस्या निवारण
- **पॉड नहीं मिल रहा**: यदि आपको "Unable to find a specification for `FXForms`" जैसी कोई एरर आती है, तो सुनिश्चित करें कि लाइब्रेरी अभी भी CocoaPods रिपॉजिटरी में उपलब्ध है। मेरे अंतिम अपडेट के अनुसार, `FXForms` एक पुरानी लाइब्रेरी है, और इसकी उपलब्धता CocoaPods ट्रंक पर निर्भर हो सकती है।
- **वर्जन एरर**: यदि वर्जन `1.2.13` उपलब्ध नहीं है, तो आप यह कमांड चलाकर उपलब्ध वर्जन चेक कर सकते हैं:
  ```bash
  pod search FXForms
  ```
  फिर अपने `Podfile` में वर्जन को तदनुसार अपडेट करें।
- **बिल्ड एरर**: सुनिश्चित करें कि Xcode में आपका डिप्लॉयमेंट टार्गेट `FXForms` द्वारा आवश्यक न्यूनतम iOS वर्जन से मेल खाता है या उससे अधिक है (पुराने वर्जन के लिए आमतौर पर iOS 7.0+)।

---

### अतिरिक्त नोट्स
- **`FXForms` अवलोकन**: `FXForms` Nick Lockwood द्वारा बनाई गई एक लाइब्रेरी है जो iOS में फॉर्म क्रिएशन को ऑटोमेट करती है। यह न्यूनतम कोड के साथ टेबल-व्यू-आधारित फॉर्म जेनरेट करने के लिए विशेष रूप से उपयोगी है।
- **Swift प्रोजेक्ट**: यदि आप Swift का उपयोग कर रहे हैं, तो `FXForms` का उपयोग करने के लिए आपको एक Objective-C ब्रिजिंग हेडर बनाना होगा, क्योंकि यह एक Objective-C लाइब्रेरी है। हेडर में `#import <FXForms/FXForms.h>` एड करें।

यदि आपको इस प्रक्रिया के किसी विशिष्ट भाग में मदद की आवश्यकता है तो मुझे बताएं!