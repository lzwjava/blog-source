---
audio: false
generated: true
lang: hi
layout: post
title: MBProgressHUD का उपयोग iOS में
translated: true
---

यह लगता है कि आप iOS प्रोजेक्ट में `MBProgressHUD` लाइब्रेरी का उपयोग करने के बारे में पूछ रहे हैं, विशेष रूप से `0.9.1` संस्करण, एक Podfile के माध्यम से CocoaPods में। मुझे आपको इस प्रक्रिया को कदम दर कदम समझाने दो।

### MBProgressHUD क्या है?
`MBProgressHUD` एक लोकप्रिय तीसरा पक्ष लाइब्रेरी है जो iOS के लिए एक आसान तरीका प्रदान करता है एक HUD (Heads-Up Display) को प्रदर्शित करने के लिए, जिसमें गतिविधि संकेतक, प्रगति पट्टियाँ, या कस्टम व्यू शामिल हैं, आमतौर पर लोडिंग स्टेट या संक्षिप्त संदेश दिखाने के लिए उपयोग किया जाता है।

### `pod 'MBProgressHUD', '0.9.1'` का उपयोग करने के कदम

#### 1. **CocoaPods इंस्टॉल करें (यदि पहले से इंस्टॉल नहीं है)**
CocoaPods एक निर्भरता प्रबंधक है iOS प्रोजेक्टों के लिए। अगर आपने इसे इंस्टॉल नहीं किया है, तो अपने टर्मिनल में इस कमांड को चलाएं:
```bash
sudo gem install cocoapods
```

#### 2. **Podfile सेट अप करें**
- अपने Xcode प्रोजेक्ट डायरेक्टरी में टर्मिनल में जाएं:
  ```bash
  cd /path/to/your/project
  ```
- अगर आपके पास पहले से Podfile नहीं है, तो इसे बनाएं इस कमांड को चलाकर:
  ```bash
  pod init
  ```
- `Podfile` को एक टेक्स्ट एडिटर में खोलें (जैसे `nano Podfile` या `open Podfile`).

#### 3. **Podfile में MBProgressHUD जोड़ें**
अपने `Podfile` में, `MBProgressHUD` संस्करण `0.9.1` के लिए लाइन को अपने ऐप के लिए टारगेट ब्लॉक के भीतर जोड़ें। यह कुछ इस तरह दिखना चाहिए:
```ruby
platform :ios, '9.0'  # अपने डिप्लॉयमेंट टारगेट को निर्दिष्ट करें

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- `'YourAppName'` को अपने Xcode टारगेट के वास्तविक नाम से बदलें।
- `platform :ios, '9.0'` लाइन आपके प्रोजेक्ट की आवश्यकताओं के आधार पर iOS का न्यूनतम संस्करण सेट करता है; इसे अनुकूलित करें।

#### 4. **Pod इंस्टॉल करें**
- `Podfile` को सेभ करें और टर्मिनल में इस कमांड को चलाएं:
  ```bash
  pod install
  ```
- यह `MBProgressHUD` संस्करण `0.9.1` को आपके प्रोजेक्ट में डाउनलोड और इंटीग्रेट करता है। अगर सफल, तो आप इंस्टॉलेशन की पुष्टि करने वाले आउटपुट देखेंगे।

#### 5. **वर्कस्पेस खोलें**
- इंस्टॉलेशन के बाद, अपने Xcode प्रोजेक्ट को बंद करें (यदि खुला है) और नए बनाए गए `.xcworkspace` फ़ाइल (जैसे `YourAppName.xcworkspace`) को खोलें `.xcodeproj` फ़ाइल के बजाय। CocoaPods इस वर्कस्पेस को निर्भरताओं को प्रबंधित करने के लिए बनाता है।

#### 6. **कोड में MBProgressHUD का उपयोग करें**
- **Swift**: मॉड्यूल को इम्पोर्ट करें और अपने कोड में इसका उपयोग करें:
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()

          // एक सरल HUD को एक लोडिंग इंडिकेटर के साथ दिखाएं
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Loading..."

          // इसे कुछ समय के बाद छिपाएं (जैसे, 2 सेकंड)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: हेडर को इम्पोर्ट करें और इसका उपयोग करें:
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];

      // एक सरल HUD को एक लोडिंग इंडिकेटर के साथ दिखाएं
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Loading...";

      // इसे कुछ समय के बाद छिपाएं (जैसे, 2 सेकंड)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **MBProgressHUD के सामान्य फीचर्स**
- **बेसिक HUD**: ऊपर दिखाए गए, एक चक्कर इंडिकेटर के साथ एक अनुपस्थित टेक्स्ट के साथ प्रदर्शित करें।
- **कस्टम टेक्स्ट केवल**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Done!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **प्रगति पट्टी**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% प्रगति
  ```

#### नोट्स
- **संस्करण 0.9.1**: यह एक पुराना संस्करण है (2015 के आसपास जारी किया गया था)। मार्च 2025 तक का नवीनतम संस्करण बहुत अधिक नवीन है (जैसे 1.2.0 या उससे अधिक)। नवीनतम संस्करण का उपयोग करने के लिए, केवल `pod 'MBProgressHUD'` लिखें बिना किसी संस्करण संख्या के। अपडेट करने की सोचें, जब तक कि आप 0.9.1 के लिए विशेष रूप से अनुकूलता की आवश्यकता नहीं है।
- **दस्तावेज़ीकरण**: अधिक विकल्प और उदाहरणों के लिए [MBProgressHUD GitHub पेज](https://github.com/jdg/MBProgressHUD) पर जांच करें। संस्करण 0.9.1 में आधुनिक रिलीजों से कम फीचर्स हो सकते हैं।

मुझे बताएं अगर आपको किसी समस्या का समाधान करने में मदद चाहिए या अधिक विशिष्ट उदाहरणों की आवश्यकता है!