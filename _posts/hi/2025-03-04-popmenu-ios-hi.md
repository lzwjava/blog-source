---
audio: false
generated: true
lang: hi
layout: post
title: आईओएस में पॉपमेन्यू का उपयोग
translated: true
type: note
---

`pod 'PopMenu', '2.4'` का उपयोग करने के लिए, आप PopMenu लाइब्रेरी (version 2.4) को CocoaPods के माध्यम से अपने iOS प्रोजेक्ट में integrate कर रहे हैं। यह एक pop-up animation menu प्रदान करती है जो Sina Weibo या NetEase जैसे ऐप्स से प्रेरित है। इसे अपने प्रोजेक्ट में सेट अप और उपयोग करने के चरण नीचे दिए गए हैं:

---

### चरण 1: CocoaPods इंस्टॉल करें (यदि पहले से इंस्टॉल नहीं है)
यदि आपके सिस्टम पर CocoaPods इंस्टॉल नहीं है, तो पहले इसे इंस्टॉल करें:
1. अपना टर्मिनल खोलें।
2. यह कमांड चलाएं:
   ```bash
   sudo gem install cocoapods
   ```
3. इंस्टॉलेशन verify करें:
   ```bash
   pod --version
   ```

---

### चरण 2: अपना Podfile सेट अप करें
1. टर्मिनल में अपने Xcode प्रोजेक्ट डायरेक्टरी में नेविगेट करें:
   ```bash
   cd /path/to/your/project
   ```
2. यदि आपके पास पहले से Podfile नहीं है, तो इसे चलाकर बनाएं:
   ```bash
   pod init
   ```
3. `Podfile` को एक टेक्स्ट एडिटर में खोलें (जैसे, `nano Podfile` या Xcode का उपयोग करें)।
4. अपने target के लिए PopMenu pod निर्दिष्ट करने के लिए निम्नलिखित पंक्तियाँ जोड़ें:
   ```ruby
   platform :ios, '8.0'  # यदि आवश्यक हो तो iOS version adjust करें
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - `YourAppName` को अपने Xcode target के नाम से बदलें।
   - `use_frameworks!` लाइन आवश्यक है क्योंकि PopMenu एक framework-based लाइब्रेरी है।

5. Podfile को सेव करें और बंद करें।

---

### चरण 3: Pod इंस्टॉल करें
1. टर्मिनल में, चलाएं:
   ```bash
   pod install
   ```
2. यह PopMenu version 2.4 को आपके प्रोजेक्ट में डाउनलोड और integrate करता है। जब तक आपको ऐसा संदेश न दिखे प्रतीक्षा करें:
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. यदि आपका Xcode प्रोजेक्ट खुला है तो उसे बंद करें, फिर नई जेनरेट की गई `.xcworkspace` फ़ाइल (जैसे, `YourAppName.xcworkspace`) खोलें, `.xcodeproj` फ़ाइल के बजाय।

---

### चरण 4: अपने कोड में बेसिक उपयोग
PopMenu Objective-C में लिखी गई है, इसलिए आपको इसका उपयोग उसी के अनुसार करना होगा। अपने ऐप में इसे implement करने का एक उदाहरण यहां दिया गया है:

1. **लाइब्रेरी Import करें**:
   - अपनी Objective-C फ़ाइल में (जैसे, `ViewController.m`):
     ```objective-c
     #import "PopMenu.h"
     ```
   - यदि आप Swift का उपयोग कर रहे हैं, तो एक bridging header बनाएं:
     - `File > New > File > Header File` पर जाएं (जैसे, `YourAppName-Bridging-Header.h`)।
     - जोड़ें:
       ```objective-c
       #import "PopMenu.h"
       ```
     - Xcode में, bridging header को `Build Settings > Swift Compiler - General > Objective-C Bridging Header` के अंतर्गत अपनी header फ़ाइल के पथ पर सेट करें (जैसे, `YourAppName/YourAppName-Bridging-Header.h`)।

2. **Menu Items बनाएं**:
   Pop-up menu में वे items परिभाषित करें जिन्हें आप चाहते हैं। प्रत्येक item में एक title, icon और glow color हो सकता है।
   ```objective-c
   NSMutableArray *items = [[NSMutableArray alloc] init];
   
   MenuItem *menuItem1 = [[MenuItem alloc] initWithTitle:@"Flickr" 
                                               iconName:@"post_type_bubble_flickr" 
                                              glowColor:[UIColor grayColor] 
                                                  index:0];
   [items addObject:menuItem1];
   
   MenuItem *menuItem2 = [[MenuItem alloc] initWithTitle:@"Twitter" 
                                               iconName:@"post_type_bubble_twitter" 
                                              glowColor:[UIColor blueColor] 
                                                  index:1];
   [items addObject:menuItem2];
   ```

3. **Menu को Initialize और Show करें**:
   एक `PopMenu` instance बनाएं और इसे अपने view में display करें।
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // विकल्प: kPopMenuAnimationTypeSina या kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // प्रति पंक्ति items की संख्या
   [popMenu showMenuAtView:self.view];
   ```

4. **Selection को हैंडल करें (वैकल्पिक)**:
   आप टैप का पता लगाने के लिए functionality को subclass या extend कर सकते हैं, हालांकि PopMenu के बेसिक version (circa 2.4) में मूल रूप से एक delegate सपोर्ट नहीं हो सकता है। किसी भी अपडेट या कस्टमाइजेशन के लिए लाइब्रेरी के documentation (`xhzengAIB/PopMenu`) को GitHub पर चेक करें।

---

### चरण 5: अपना प्रोजेक्ट रन करें
Xcode में अपने प्रोजेक्ट को बिल्ड और रन करें (`Cmd + R`)। यदि आइकन (जैसे, `post_type_bubble_flickr`) आपके asset catalog का हिस्सा हैं, तो सुनिश्चित करें कि वे आपके प्रोजेक्ट में जोड़े गए हैं। यदि नहीं, तो आपको उन्हें source करना या बनाना होगा।

---

### नोट्स
- **Version Specificity**: `pod 'PopMenu', '2.4'` आपको version 2.4 पर लॉक कर देता है। यदि आप latest version चाहते हैं, तो version number के बिना `pod 'PopMenu'` का उपयोग करें, लेकिन इससे breaking changes आ सकती हैं।
- **Compatibility**: सुनिश्चित करें कि आपके प्रोजेक्ट का deployment target कम से कम iOS 8.0 है (या Podfile में `platform` adjust करें)।
- **Customization**: PopMenu animation type और layout tweaks (जैसे, `perRowItemCount`) की अनुमति देती है। अधिक विकल्पों के लिए source code को explore करें।
- **Troubleshooting**: यदि आपको "file not found" जैसी errors आती हैं, तो सुनिश्चित करें कि आपके Pods सही ढंग से इंस्टॉल हैं और आपका workspace उपयोग में है।

यह आपको अपने iOS ऐप में PopMenu 2.4 के साथ शुरुआत करने में मदद करेगा! यदि आपको और स्पष्टीकरण की आवश्यकता हो तो मुझे बताएं।