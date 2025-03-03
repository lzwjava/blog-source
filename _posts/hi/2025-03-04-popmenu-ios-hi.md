---
audio: false
generated: true
lang: hi
layout: post
title: PopMenu का उपयोग iOS में
translated: true
---

आपके iOS प्रोजेक्ट में `pod 'PopMenu', '2.4'` का उपयोग करने के लिए, आप CocoaPods, एक लोकप्रिय iOS निर्भरता प्रबंधक के माध्यम से PopMenu लाइब्रेरी (वर्जन 2.4) को एकीकृत कर रहे हैं। यह लाइब्रेरी Sina Weibo या NetEase जैसी ऐप्स से प्रेरित एक पॉप-अप एनिमेशन मेनू प्रदान करता है। नीचे दिए गए कदमों को सेट अप और प्रोजेक्ट में इसका उपयोग करने के लिए पालन करें:

---

### कदम 1: CocoaPods की स्थापना (अगर पहले से स्थापित नहीं है)
अगर आपके सिस्टम पर CocoaPods स्थापित नहीं है, तो पहले इसे स्थापित करें:
1. अपने टर्मिनल खोलें।
2. इस कमांड को चलाएं:
   ```bash
   sudo gem install cocoapods
   ```
3. स्थापना की पुष्टि करें:
   ```bash
   pod --version
   ```

---

### कदम 2: Podfile सेट अप करें
1. टर्मिनल में अपने Xcode प्रोजेक्ट डायरेक्टरी पर जाएं:
   ```bash
   cd /path/to/your/project
   ```
2. अगर आपके पास पहले से Podfile नहीं है, तो इसे बनाएं:
   ```bash
   pod init
   ```
3. एक टेक्स्ट एडिटर में `Podfile` खोलें (जैसे `nano Podfile` या Xcode का उपयोग करें).
4. अपने टारगेट के लिए PopMenu पॉड को निर्दिष्ट करने के लिए निम्नलिखित लाइनें जोड़ें:
   ```ruby
   platform :ios, '8.0'  # आवश्यकता के अनुसार iOS वर्जन को समायोजित करें
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - `YourAppName` को अपने Xcode टारगेट का नाम से बदलें।
   - `use_frameworks!` लाइन आवश्यक है क्योंकि PopMenu संभवतः एक फ्रेमवर्क आधारित लाइब्रेरी है।

5. Podfile को बचाएं और बंद करें।

---

### कदम 3: Pod को स्थापित करें
1. टर्मिनल में चलाएं:
   ```bash
   pod install
   ```
2. यह PopMenu वर्जन 2.4 को आपके प्रोजेक्ट में डाउनलोड और एकीकृत करता है। जब तक आप एक संदेश देखते हैं जैसे:
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. अगर खुला है, तो अपने Xcode प्रोजेक्ट को बंद करें, फिर नए रूप से उत्पन्न `.xcworkspace` फ़ाइल (जैसे `YourAppName.xcworkspace`) खोलें, न कि `.xcodeproj` फ़ाइल।

---

### कदम 4: आपके कोड में आधारभूत उपयोग
PopMenu Objective-C में लिखा गया है, इसलिए आप इसे अनुरूप उपयोग करेंगे। यहां आपके ऐप में इसे लागू करने का एक उदाहरण है:

1. **लाइब्रेरी को आयात करें**:
   - अपने Objective-C फ़ाइल में (जैसे `ViewController.m`):
     ```objective-c
     #import "PopMenu.h"
     ```
   - अगर आप Swift का उपयोग कर रहे हैं, तो एक ब्रिजिंग हेडर बनाएं:
     - `File > New > File > Header File` पर जाएं (जैसे `YourAppName-Bridging-Header.h`).
     - जोड़ें:
       ```objective-c
       #import "PopMenu.h"
       ```
     - Xcode में `Build Settings > Swift Compiler - General > Objective-C Bridging Header` के तहत ब्रिजिंग हेडर को सेट करें, अपने हेडर फ़ाइल के पथ तक (जैसे `YourAppName/YourAppName-Bridging-Header.h`).

2. **मेनू आइटम बनाएं**:
   पॉप-अप मेनू में आप चाहे जो आइटम को परिभाषित करें। प्रत्येक आइटम का एक शीर्षक, आइकन और ग्लो कॉलर हो सकता है।
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

3. **मेनू को प्रारंभ करें और दिखाएं**:
   एक `PopMenu` इंस्टेंस बनाएं और इसे आपके दृश्य में प्रदर्शित करें।
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // विकल्प: kPopMenuAnimationTypeSina या kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // प्रत्येक पंक्ति में आइटम की संख्या
   [popMenu showMenuAtView:self.view];
   ```

4. **चयन को संभालें (वैकल्पिक)**:
   आप तप को पता लगाने के लिए उपश्रेणी या कार्यक्षमता को बढ़ा सकते हैं, हालांकि PopMenu के आधारभूत संस्करण (लगभग 2.4) को नैसर्गिक रूप से एक डिलीगेट का समर्थन नहीं हो सकता है। GitHub पर लाइब्रेरी के दस्तावेज़ (`xhzengAIB/PopMenu`) में किसी भी अपडेट या अनुकूलन की जांच करें।

---

### कदम 5: अपने प्रोजेक्ट को चलाएं
Xcode में अपने प्रोजेक्ट को बनाएं और चलाएं (`Cmd + R`). अगर आइकन (जैसे `post_type_bubble_flickr`) आपके एसेट कैटलॉग का हिस्सा हैं, तो सुनिश्चित करें कि वे आपके प्रोजेक्ट में जोड़े गए हैं। अगर नहीं, तो आपको उन्हें स्रोत या बनाना होगा।

---

### नोट्स
- **वर्जन विशिष्टता**: `pod 'PopMenu', '2.4'` आपको वर्जन 2.4 पर लॉक करता है। अगर आप नवीनतम वर्जन चाहते हैं, तो वर्जन संख्या के बिना `pod 'PopMenu'` का उपयोग करें, लेकिन यह तोड़ने वाले परिवर्तन ला सकता है।
- **संगतता**: सुनिश्चित करें कि आपके प्रोजेक्ट का डिप्लॉयमेंट टारगेट कम से कम iOS 8.0 है (या Podfile में `platform` को समायोजित करें).
- **अनुकूलन**: PopMenu एनिमेशन प्रकार और लेआउट समायोजन (जैसे `perRowItemCount`) की अनुमति देता है। अधिक विकल्पों के लिए स्रोत कोड का अन्वेषण करें।
- **संघर्ष समाधान**: अगर आप "फ़ाइल नहीं मिली" जैसी त्रुटियों का सामना करते हैं, तो सुनिश्चित करें कि आपके Pods सही तरह से स्थापित हैं और आपके वर्कस्पेस का उपयोग किया जा रहा है।

यह आपको अपने iOS ऐप में PopMenu 2.4 के साथ शुरू करने में मदद करेगा! अगर आपको और अधिक स्पष्टीकरण की आवश्यकता है, तो मुझे बता दें।