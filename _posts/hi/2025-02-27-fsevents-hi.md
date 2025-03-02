---
audio: false
generated: false
lang: hi
layout: post
title: डायरेक्टरी परिवर्तनों की निगरानी FSEvents API के साथ
translated: true
---

मैं एक Jekyll ब्लॉग का उपयोग कर रहा था, और जब मैंने `bundle exec jekyll serve --incremental` चलाया, तो टर्मिनल पर `fsevent_watch` दिखा। इसके बाद मैंने इसे एक AI के साथ पूछताछ की।

---

यह लगता है कि आप शायद `fsevent_watch` के बारे में बात कर रहे हैं, जो अधिकांश प्रोग्रामिंग संदर्भों में एक मानक, स्वतंत्र उपकरण या फंक्शन नहीं है। आपके सवाल और आम परंपराओं के आधार पर, मैं मानता हूँ कि आप macOS पर फाइल सिस्टम घटनाओं को निगरानी करने के लिए **FSEvents API** के साथ काम करने के बारे में पूछ रहे हैं—शायद आपने `fsevents` या किसी संबंधित यूटीलीटी के बारे में सोचा था। अगर मैंने गलत समझा है, तो कृपया स्पष्ट करें!

FSEvents API एक macOS-विशिष्ट फ्रेमवर्क है जो एप्लिकेशंस को डायरेक्टरी ट्री में परिवर्तन के बारे में सूचना प्राप्त करने की अनुमति देता है। यह आमतौर पर C, Objective-C, या Swift प्रोग्रामिंग में फाइल सिस्टम घटनाओं जैसे फाइल निर्माण, हटाना, या परिवर्तन को देखने के लिए उपयोग किया जाता है। क्योंकि `fsevent_watch` एक मान्य कमांड या फंक्शन नहीं है (यह एक टाइपो या एक तीसरे पक्ष के उपकरण हो सकता है), मैं FSEvents API का उपयोग करने के बारे में समझाता हूँ, जो शायद आपकी जरूरत है।

यह एक प्रैक्टिकल गाइड है FSEvents का उपयोग करके एक डायरेक्टरी को निगरानी करने के लिए:

### FSEvents का उपयोग C/Objective-C में
FSEvents API macOS पर CoreServices फ्रेमवर्क का हिस्सा है। नीचे एक बुनियादी उदाहरण है C में एक डायरेक्टरी को परिवर्तन के लिए निगरानी करने के लिए:

1. **आवश्यक हेडर्स को शामिल करें**:
   आपको CoreServices फ्रेमवर्क से FSEvents हेडर को शामिल करना होगा।

2. **इवेंट स्ट्रीम सेट अप करें**:
   एक इवेंट स्ट्रीम बनाएं एक विशेष डायरेक्टरी को देखें, एक कॉलबैक फंक्शन को घटनाओं को संभालने के लिए परिभाषित करें, और इसे एक रन लूप के साथ शेड्यूल करें।

3. **इवेंट्स को संभालें**:
   कॉलबैक घटनाओं को प्रोसेस करता है (उदाहरण के लिए, फाइल बदल गई, हटाई गई) और पथ और फ्लैग प्रदान करता है।

यह एक न्यूनतम उदाहरण है:

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// फाइल सिस्टम घटनाओं को संभालने के लिए कॉलबैक फंक्शन
void callback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[])
{
    char **paths = (char **)eventPaths;
    for (size_t i = 0; i < numEvents; i++) {
        printf("Change detected at: %s (Flags: 0x%x)\n", paths[i], eventFlags[i]);
    }
}

int main() {
    // निगरानी करने के लिए पथ (उदाहरण के लिए, आपका होम डायरेक्टरी)
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // इवेंट स्ट्रीम बनाएं
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // अलोकेटर
        &callback,      // कॉलबैक फंक्शन
        NULL,           // कॉलबैक इन्फो (संदर्भ)
        pathsToWatch,   // निगरानी करने के लिए पथ
        kFSEventStreamEventIdSinceNow, // अब से घटनाओं से शुरू करें
        1.0,            // लैटेंसी सेकंड में (बैचिंग देरी)
        kFSEventStreamCreateFlagNone // फ्लैग (किसी फाइल-स्तर घटनाओं के लिए kFSEventStreamCreateFlagFileEvents का उपयोग कर सकते हैं)
    );

    // स्ट्रीम को वर्तमान रन लूप पर शेड्यूल करें
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // स्ट्रीम को शुरू करें
    FSEventStreamStart(stream);

    // घटनाओं को सुनने के लिए लूप को चलाएं
    printf("Monitoring /Users/yourusername... Press Ctrl+C to stop.\n");
    CFRunLoopRun();

    // क्लीनअप (इस उदाहरण में पहुंचने योग्य नहीं है जब तक कि रोक दिया गया हो)
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### चरणों का स्पष्टीकरण:
- **निगरानी करने के लिए पथ**: आप एक या अधिक डायरेक्टरी (उदाहरण के लिए, `/Users/yourusername`) को एक `CFArray` में परिभाषित करते हैं।
- **कॉलबैक**: `callback` फंक्शन तब ट्रिगर होता है जब परिवर्तन होते हैं। यह प्रभावित पथों और फ्लैगों (उदाहरण के लिए, `kFSEventStreamEventFlagItemCreated`) का एक एरे प्राप्त करता है।
- **स्ट्रीम निर्माण**: `FSEventStreamCreate` वॉचर को सेट अप करता है। लैटेंसी (उदाहरण के लिए, `1.0` सेकंड) घटनाओं को बैच करता है ताकि कॉलबैक को ओवरव्हेल्म नहीं हो सके।
- **रन लूप**: स्ट्रीम एक रन लूप (जैसे `CFRunLoopRun`) के साथ एकीकृत होता है ताकि प्रोग्राम जीवित और प्रतिक्रियाशील रहे।
- **क्लीनअप**: जब काम हो जाए, तो स्ट्रीम को रोकें और रिलीज़ करें (इस अनंत लूप उदाहरण में दिखाया नहीं है).

#### कॉम्पाइलेशन:
CoreServices फ्रेमवर्क के साथ कॉम्पाइल करें:
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

इसको चलाएं:
```bash
./fsevents_example
```

### मुख्य बिंदु:
- **ग्रेन्यूलरिटी**: डिफ़ॉल्ट में, FSEvents डायरेक्टरी-स्तर परिवर्तन को निगरानी करता है। फाइल-स्तर घटनाओं (उदाहरण के लिए, विशेष फाइल परिवर्तन) के लिए, `kFSEventStreamCreateFlagFileEvents` फ्लैग जोड़ें।
- **लैटेंसी**: लैटेंसी पैरामीटर (उदाहरण के लिए, `1.0`) कॉलबैक को कितनी बार ट्रिगर होता है, यह नियंत्रित करता है। कम मान तेज़ अपडेट देते हैं, लेकिन अधिक कॉल होते हैं।
- **स्कोप**: FSEvents पूरी डायरेक्टरी ट्री को रिकर्सिव रूप से निगरानी करता है—उप-डायरेक्टरी को स्पष्ट रूप से परिभाषित करने की आवश्यकता नहीं है।

### विकल्प: एक उपकरण का उपयोग
अगर आप एक कमांड-लाइन उपकरण के बजाय खुद कोडिंग करना चाहते हैं, तो मानक macOS टूलकिट में `fsevent_watch` नहीं है। फिर भी, तीसरे पक्ष के उपकरण जैसे `fswatch` FSEvents का उपयोग करते हैं। `fswatch` का उपयोग करने के लिए:

1. **fswatch इंस्टॉल करें** (उदाहरण के लिए, Homebrew के माध्यम से):
   ```bash
   brew install fswatch
   ```

2. **इसको चलाएं**:
   ```bash
   fswatch /path/to/watch
   ```
   यह परिवर्तन होते समय पथों को आउटपुट करता है। उदाहरण के लिए:
   ```bash
   fswatch ~/Documents
   ```
   आप फाइल बदलने पर पंक्तियाँ देखेंगे जैसे `/Users/yourusername/Documents/file.txt`.

3. **एक स्क्रिप्ट के साथ**:
   इसे एक स्क्रिप्ट के साथ पाइप करें अपने कस्टम कार्यों के लिए:
   ```bash
   fswatch ~/Documents | while read -r file; do echo "Changed: $file"; done
   ```

### अगर आपने कुछ और सोचा था
अगर `fsevent_watch` किसी विशेष लाइब्रेरी, उपकरण, या टाइपो (उदाहरण के लिए, `fsevents-watch`) का संदर्भ देता है, तो कृपया अधिक संदर्भ प्रदान करें—जैसे प्रोग्रामिंग भाषा या वातावरण जिसमें आप काम कर रहे हैं—and मैं जवाब को और अधिक अनुकूलित कर सकता हूँ।

मुझे बताएं कि मैं इसे आपके लिए कैसे सुधार सकता हूँ!