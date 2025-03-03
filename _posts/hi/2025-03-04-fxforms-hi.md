---
audio: false
generated: true
lang: hi
layout: post
title: FXForms का उपयोग iOS में
translated: true
---

यह लगता है कि आप `FXForms` लाइब्रेरी को CocoaPods, एक लोकप्रिय Swift और Objective-C प्रोजेक्ट्स के लिए निर्भरता प्रबंधक का उपयोग करके iOS प्रोजेक्ट में एकीकृत करने के बारे में संदर्भ कर रहे हैं। यहाँ एक चरण-दर-चरण गाइड है जो आपको `pod 'FXForms', '1.2.13'` को अपने प्रोजेक्ट में उपयोग करने में मदद करेगा:

---

### पूर्वापेक्षाएँ
1. **CocoaPods इंस्टॉल करें**: अगर आपके मशीन पर CocoaPods इंस्टॉल नहीं है, तो इसे पहले इंस्टॉल करने के लिए टर्मिनल में इस कमांड को चलाएं:
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode प्रोजेक्ट**: सुनिश्चित करें कि आपके पास एक मौजूदा Xcode प्रोजेक्ट है जहां आप `FXForms` को एकीकृत करना चाहते हैं।

---

### `pod 'FXForms', '1.2.13'` का उपयोग करने के चरण

#### 1. **अपने प्रोजेक्ट डायरेक्टरी में जाएं**
टर्मिनल खोलें और अपने Xcode प्रोजेक्ट (`.xcodeproj` फ़ाइल) को रखने वाले डायरेक्टरी में जाएं:
```bash
cd /path/to/your/project
```

#### 2. **Podfile को प्रारंभ करें (अगर पहले से मौजूद नहीं है)**
अगर आपके प्रोजेक्ट डायरेक्टरी में पहले से कोई `Podfile` नहीं है, तो इसे बनाएं:
```bash
pod init
```
यह आपके प्रोजेक्ट डायरेक्टरी में एक `Podfile` पैदा करेगा।

#### 3. **Podfile को संपादित करें**
एक टेक्स्ट एडिटर (जैसे `nano`, `vim`, या किसी भी कोड एडिटर जैसे VS Code) में `Podfile` खोलें और `FXForms` पॉड को विशेष संस्करण `1.2.13` के साथ जोड़ें। आपके `Podfile` को कुछ इस तरह दिखना चाहिए:

```ruby
platform :ios, '9.0'  # न्यूनतम iOS संस्करण को निर्दिष्ट करें (अनुसार समायोजित करें)
use_frameworks!       # विकल्प, यदि आप Swift या फ्रेमवर्क का उपयोग कर रहे हैं तो शामिल करें

target 'YourProjectName' do
  # YourProjectName के लिए Pods
  pod 'FXForms', '1.2.13'
end
```

- `'YourProjectName'` को अपने Xcode टारगेट का वास्तविक नाम से बदलें (आप इसे Xcode में अपने प्रोजेक्ट सेटिंग्स के तहत पा सकते हैं).
- `pod 'FXForms', '1.2.13'` पंक्ति यह बताती है कि आप `FXForms` लाइब्रेरी का संस्करण `1.2.13` चाहते हैं।

#### 4. **Pod को इंस्टॉल करें**
`Podfile` को सेंधा कर, टर्मिनल में निम्न कमांड चलाएं ताकि `FXForms` संस्करण `1.2.13` को अपने प्रोजेक्ट में डाउनलोड और एकीकृत किया जा सके:
```bash
pod install
```
यदि सफल, तो आप पॉड्स को इंस्टॉल करने के बारे में आउटपुट देखेंगे।

#### 5. **वर्कस्पेस को खोलें**
`pod install` चलाने के बाद, आपके प्रोजेक्ट डायरेक्टरी में एक `.xcworkspace` फ़ाइल पैदा होगी। इस फ़ाइल (नहीं `.xcodeproj`) को Xcode में खोलें:
```bash
open YourProjectName.xcworkspace
```

#### 6. **अपने कोड में FXForms का उपयोग करें**
`FXForms` एक Objective-C लाइब्रेरी है जो iOS ऐप में फॉर्म बनाने को सरल बनाती है। यहाँ इसका उपयोग करने का एक बुनियादी उदाहरण है:

- **FXForms को आयात करें**: अपने Objective-C फ़ाइल (जैसे एक व्यू कंट्रोलर) में लाइब्रेरी को आयात करें:
  ```objective-c
  #import <FXForms/FXForms.h>
  ```

- **एक फॉर्म मॉडल बनाएं**: एक क्लास को `FXForm` प्रोटोकॉल से अनुपालन करने के लिए परिभाषित करें। उदाहरण के लिए:
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

- **फॉर्म को प्रदर्शित करें**: अपने व्यू कंट्रोलर में `FXFormViewController` का उपयोग करके फॉर्म को प्रस्तुत करें:
  ```objective-c
  #import "MyForm.h"

  - (void)viewDidLoad {
      [super viewDidLoad];
      FXFormViewController *formController = [[FXFormViewController alloc] init];
      formController.form = [[MyForm alloc] init];
      [self.navigationController pushViewController:formController animated:YES];
  }
  ```

#### 7. **बिल्ड और चलाएं**
Xcode में अपने प्रोजेक्ट को बिल्ड करें (`Cmd + B`) ताकि सुनिश्चित किया जा सके कि सब कुछ सही तरह से सेट अप है, फिर इसे एक सिमुलेटर या डिवाइस पर चलाएं (`Cmd + R`).

---

### समस्या निदान
- **Pod नहीं मिला**: अगर आप एक त्रुटि जैसे "`FXForms` के लिए एक स्पेसिफिकेशन नहीं मिला" पाते हैं, तो सुनिश्चित करें कि लाइब्रेरी अभी भी CocoaPods रिपोजिटरी में उपलब्ध है। मेरे अंतिम अपडेट के अनुसार, `FXForms` एक पुराना लाइब्रेरी है, और इसका उपलब्धता CocoaPods ट्रंक पर निर्भर करेगी।
- **संस्करण त्रुटि**: अगर संस्करण `1.2.13` उपलब्ध नहीं है, तो उपलब्ध संस्करणों को जांचने के लिए निम्न कमांड चलाएं:
  ```bash
  pod search FXForms
  ```
  फिर `Podfile` में संस्करण को अनुकूलित करें।

- **बिल्ड त्रुटियाँ**: सुनिश्चित करें कि आपके Xcode में डिप्लॉयमेंट टारगेट `FXForms` द्वारा आवश्यक न्यूनतम iOS संस्करण (आम तौर पर iOS 7.0+ के लिए पुराने संस्करणों के लिए) से मिलता है।

---

### अतिरिक्त टिप्पणियाँ
- **`FXForms` परिचय**: `FXForms` Nick Lockwood द्वारा एक लाइब्रेरी है जो iOS में फॉर्म निर्माण को स्वचालित करता है। यह विशेष रूप से कम कोड के साथ टेबल-व्यू आधारित फॉर्म पैदा करने में उपयोगी है।
- **Swift प्रोजेक्ट**: अगर आप Swift का उपयोग कर रहे हैं, तो `FXForms` का उपयोग करने के लिए एक Objective-C ब्रिजिंग हेडर बनाना होगा, क्योंकि यह एक Objective-C लाइब्रेरी है। हेडर में `#import <FXForms/FXForms.h>` जोड़ें।

मुझे बताएं अगर आपको इस प्रक्रिया के किसी खास हिस्से में मदद चाहिए!