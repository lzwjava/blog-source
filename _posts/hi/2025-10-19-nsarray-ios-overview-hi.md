---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: आईओएस विकास के लिए एनएसएरे का अवलोकन
translated: true
type: note
---

### NSArray क्या है?

`NSArray` Apple के Foundation फ्रेमवर्क में एक क्लास है, जो iOS SDK (और macOS, आदि) का हिस्सा है। यह एक अपरिवर्तनीय, क्रमबद्ध ऑब्जेक्ट्स का संग्रह दर्शाता है, जो अन्य भाषाओं में array के समान है। इसका मतलब है कि एक बार `NSArray` बना लेने के बाद, आप उसमें एलिमेंट्स जोड़, हटा या बदल नहीं सकते—आप केवल उसे पढ़ सकते हैं। यह Objective-C में iOS ऐप डेवलपमेंट के लिए डेटा की सूचियों, जैसे यूजर प्रेफरेंसेज, डेटाबेस क्वेरी रिजल्ट्स, या UI एलिमेंट्स को स्टोर और मैनेज करने में आमतौर पर इस्तेमाल होता है।

मुख्य विशेषताएं:
- **अपरिवर्तनीय**: निर्माण के बाद फिक्स्ड साइज और कंटेंट्स (परिवर्तनशील वर्जन के लिए `NSMutableArray` का उपयोग करें)।
- **ऑब्जेक्ट्स के लिए टाइप-सेफ**: Objective-C ऑब्जेक्ट्स के पॉइंटर्स स्टोर करता है (जैसे, `NSString`, `NSNumber`, कस्टम क्लासेज)। यह प्रिमिटिव्स को सीधे सपोर्ट नहीं करता—उन्हें `NSNumber` या इसी तरह के में रैप करें।
- **इंडेक्स एक्सेस**: एलिमेंट्स को इंटीजर इंडेक्स (0-आधारित) द्वारा एक्सेस किया जाता है।
- **थ्रेड-सेफ**: समवर्ती रीड्स के लिए आम तौर पर सुरक्षित, लेकिन राइट्स के लिए नहीं (क्योंकि यह अपरिवर्तनीय है)।
- **एकीकरण**: अन्य Foundation क्लासेज जैसे `NSDictionary`, `NSString` और Cocoa Touch UI कंपोनेंट्स के साथ निर्बाध रूप से काम करता है।

Swift में, `NSArray` को `Array` में ब्रिज किया गया है, लेकिन अगर आप Objective-C में काम कर रहे हैं (लेगेसी iOS कोड के लिए आम), तो आप सीधे `NSArray` का उपयोग करेंगे।

### iOS में NSArray का उपयोग कैसे करें

iOS प्रोजेक्ट में `NSArray` का उपयोग करने के लिए:
1. Foundation फ्रेमवर्क को इम्पोर्ट करें (यह आमतौर पर iOS ऐप्स में डिफ़ॉल्ट रूप से शामिल होता है)।
   ```objc
   #import <Foundation/Foundation.h>
   ```

2. **NSArray बनाना**:
   - लिटरल सिंटैक्स (iOS 6+): `@[object1, object2, ...]`
   - इनिट मेथड: `[[NSArray alloc] initWithObjects:object1, object2, nil]`
   - C array से: `initWithArray:copyItems:`

   उदाहरण:
   ```objc
   NSArray *fruits = @[@"apple", @"banana", @"cherry"];
   // या:
   NSArray *numbers = [[NSArray alloc] initWithObjects:@1, @2, @3, nil];
   ```

3. **एलिमेंट्स तक पहुंचना**:
   - आइटम प्राप्त करने के लिए `objectAtIndex:`।
   - लंबाई के लिए `count`।
   - किनारों के लिए `firstObject` / `lastObject`।
   - अस्तित्व जांचने के लिए `containsObject:`।

   उदाहरण:
   ```objc
   NSString *firstFruit = [fruits objectAtIndex:0]; // "apple"
   NSUInteger count = [fruits count]; // 3
   BOOL hasOrange = [fruits containsObject:@"orange"]; // NO
   ```

4. **पुनरावृत्ति**:
   - फास्ट एन्युमरेशन: `for (id obj in array) { ... }`
   - ब्लॉक-आधारित पुनरावृत्ति के लिए `enumerateObjectsUsingBlock:` (iOS 4+)।

   उदाहरण:
   ```objc
   for (NSString *fruit in fruits) {
       NSLog(@"Fruit: %@", fruit);
   }
   ```

5. **सामान्य ऑपरेशन्स**:
   - सॉर्टिंग: `sortedArrayUsingSelector:` या `sortedArrayUsingComparator:`।
   - फिल्टरिंग: `filteredArrayUsingPredicate:` (NSPredicate के साथ)।
   - जोड़ना: स्ट्रिंग्स के लिए `componentsJoinedByString:`।
   - फाइल में लिखना: `writeToFile:atomically:`।

   उदाहरण (फिल्टरिंग):
   ```objc
   NSPredicate *predicate = [NSPredicate predicateWithFormat:@"length > 5"];
   NSArray *longFruits = [fruits filteredArrayUsingPredicate:predicate];
   // परिणाम: @[@"banana", @"cherry"]
   ```

6. **iOS Contexts में**:
   - **टेबल व्यू**: `NSArray` को `UITableView` के डेटा सोर्स मेथड्स जैसे `tableView:numberOfRowsInSection:` (`count` के माध्यम से) और `tableView:cellForRowAtIndexPath:` (`objectAtIndex:` के माध्यम से) में पास करें।
   - **यूजर डिफॉल्ट्स**: `NSUserDefaults` के साथ स्टोर/रिट्रीव करें: `[defaults setObject:array forKey:@"savedItems"];`।
   - **JSON हैंडलिंग**: `NSData` के साथ `JSONObjectWithData:options:error:` का उपयोग करके कन्वर्ट करें।

परिवर्तनशील जरूरतों के लिए (जैसे, आइटम्स डायनामिक रूप से जोड़ना), `NSMutableArray` पर स्विच करें:
```objc
NSMutableArray *mutableFruits = [NSMutableArray arrayWithArray:fruits];
[mutableFruits addObject:@"date"];
```

### टिप्स
- क्रैश से बचने के लिए हमेशा `nil` या बाउंड्स की जांच करें: इंडेक्स वैलिडेशन के साथ `objectAtIndex:` का उपयोग करें।
- परफॉर्मेंस: एक्सेस के लिए O(1), सर्च के लिए O(n)।
- मॉडर्न iOS: नए प्रोजेक्ट्स के लिए Swift के `Array` पर विचार करें—यह अधिक टाइप-सेफ है।

[NSArray Documentation](https://developer.apple.com/documentation/foundation/nsarray)  
[NSMutableArray Documentation](https://developer.apple.com/documentation/foundation/nsmutablearray)