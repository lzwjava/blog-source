---
audio: false
generated: true
lang: hi
layout: post
title: आईओएस में एमबीप्रोग्रेसएचयूडी का उपयोग
translated: true
type: note
---

ऐसा लगता है कि आप CocoaPods में Podfile के माध्यम से एक iOS प्रोजेक्ट में `MBProgressHUD` लाइब्रेरी, विशेष रूप से version `0.9.1`, का उपयोग करने के बारे में पूछ रहे हैं। मैं आपको इस प्रक्रिया के चरण-दर-चरण मार्गदर्शन देता हूँ।

### MBProgressHUD क्या है?
`MBProgressHUD` iOS के लिए एक लोकप्रिय तृतीय-पक्ष लाइब्रेरी है जो एक्टिविटी इंडिकेटर्स, प्रोग्रेस बार, या कस्टम व्यू के साथ एक HUD (हैड्स-अप डिस्प्ले) दिखाने का एक आसान तरीका प्रदान करती है, जिसका उपयोग आमतौर पर लोडिंग स्टेट्स या संक्षिप्त संदेशों को दिखाने के लिए किया जाता है।

### `pod 'MBProgressHUD', '0.9.1'` का उपयोग करने के चरण

#### 1. **CocoaPods इंस्टॉल करें (यदि पहले से इंस्टॉल नहीं है)**
CocoaPods iOS प्रोजेक्ट्स के लिए एक डिपेंडेंसी मैनेजर है। यदि आपके पास यह इंस्टॉल नहीं है, तो अपने टर्मिनल में यह कमांड चलाएँ:
```bash
sudo gem install cocoapods
```

#### 2. **Podfile सेट अप करें**
- टर्मिनल में अपने Xcode प्रोजेक्ट डायरेक्टरी में नेविगेट करें:
  ```bash
  cd /path/to/your/project
  ```
- यदि आपके पास पहले से Podfile नहीं है, तो इसे चलाकर बनाएँ:
  ```bash
  pod init
  ```
- एक टेक्स्ट एडिटर (जैसे, `nano Podfile` या `open Podfile`) में `Podfile` खोलें।

#### 3. **अपने Podfile में MBProgressHUD जोड़ें**
अपने `Podfile` में, अपने ऐप के लिए टार्गेट ब्लॉक के अंदर `MBProgressHUD` version `0.9.1` के लिए लाइन जोड़ें। यह कुछ इस तरह दिखना चाहिए:
```ruby
platform :ios, '9.0'  # अपना डिप्लॉयमेंट टार्गेट निर्दिष्ट करें

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- `'YourAppName'` को अपने Xcode टार्गेट के वास्तविक नाम से बदलें।
- `platform :ios, '9.0'` लाइन न्यूनतम iOS वर्जन सेट करती है; इसे अपने प्रोजेक्ट की आवश्यकताओं के आधार पर समायोजित करें।

#### 4. **Pod इंस्टॉल करें**
- `Podfile` सेव करें और टर्मिनल में यह कमांड चलाएँ:
  ```bash
  pod install
  ```
- यह आपके प्रोजेक्ट में `MBProgressHUD` version `0.9.1` को डाउनलोड और एकीकृत करता है। यदि सफल होता है, तो आपको इंस्टॉलेशन की पुष्टि करने वाला आउटपुट दिखाई देगा।

#### 5. **वर्कस्पेस खोलें**
- इंस्टॉलेशन के बाद, अपना Xcode प्रोजेक्ट (यदि खुला है तो) बंद करें और नई बनाई गई `.xcworkspace` फ़ाइल (जैसे, `YourAppName.xcworkspace`) को `.xcodeproj` फ़ाइल के बजाय खोलें। CocoaPods डिपेंडेंसीज़ को प्रबंधित करने के लिए यह वर्कस्पेस जनरेट करता है।

#### 6. **अपने कोड में MBProgressHUD का उपयोग करना**
- **Swift**: मॉड्यूल इम्पोर्ट करें और अपने कोड में इसका उपयोग करें:
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()
          
          // एक लोडिंग इंडिकेटर के साथ एक साधारण HUD दिखाएँ
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Loading..."
          
          // कुछ समय बाद (जैसे, 2 सेकंड) इसे छिपाएँ
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: हैडर इम्पोर्ट करें और इसका उपयोग करें:
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];
      
      // एक लोडिंग इंडिकेटर के साथ एक साधारण HUD दिखाएँ
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Loading...";
      
      // कुछ समय बाद (जैसे, 2 सेकंड) इसे छिपाएँ
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **MBProgressHUD की सामान्य विशेषताएँ**
- **बेसिक HUD**: जैसा ऊपर दिखाया गया है, वैकल्पिक टेक्स्ट के साथ एक स्पिनिंग इंडिकेटर दिखाएँ।
- **कस्टम टेक्स्ट ओनली**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Done!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **प्रोग्रेस बार**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% प्रोग्रेस
  ```

#### नोट्स
- **वर्जन 0.9.1**: यह एक पुराना वर्जन है (लगभग 2015 में रिलीज़ हुआ)। मार्च 2025 तक नवीनतम वर्जन इससे कहीं अधिक नया है (जैसे, 1.2.0 या उच्चतर)। नवीनतम का उपयोग करने के लिए, बिना वर्जन नंबर के सिर्फ `pod 'MBProgressHUD'` लिखें। जब तक कि आपको कॉम्पैटिबिलिटी के लिए विशेष रूप से 0.9.1 की आवश्यकता न हो, अपडेट करने पर विचार करें।
- **डॉक्यूमेंटेशन**: अधिक विकल्पों और उदाहरणों के लिए [MBProgressHUD GitHub पेज](https://github.com/jdg/MBProgressHUD) देखें। वर्जन 0.9.1 में आधुनिक रिलीज़ की तुलना में कम सुविधाएँ हो सकती हैं।

यदि आपको ट्रबलशूटिंग में सहायता या अधिक विशिष्ट उदाहरणों की आवश्यकता है तो मुझे बताएं!