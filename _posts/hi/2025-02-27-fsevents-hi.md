---
audio: false
generated: true
lang: hi
layout: post
title: FSEvents API के साथ डायरेक्टरी परिवर्तनों की निगरानी
translated: true
type: note
---

मैं एक Jekyll ब्लॉग का उपयोग कर रहा था, और जब मैंने `bundle exec jekyll serve --incremental` चलाया, तो टर्मिनल ने `fsevent_watch` प्रदर्शित किया। नतीजतन, मैंने इसके बारे में एक AI से पूछा।

---

ऐसा लगता है कि आपका मतलब `fsevent_watch` से हो सकता है, जो अधिकांश प्रोग्रामिंग संदर्भों में एक मानक, स्टैंडअलोन टूल या फ़ंक्शन नहीं है। आपके प्रश्न और सामान्य परंपराओं के आधार पर, मैं मानूंगा कि आप फ़ाइल सिस्टम इवेंट्स की निगरानी करने के लिए macOS पर **FSEvents API** के साथ काम करने के बारे में पूछ रहे हैं—शायद आपका मतलब `fsevents` या संबंधित यूटिलिटी से था। यदि मैंने गलत समझा है, तो कृपया स्पष्ट करें!

FSEvents API एक macOS-विशिष्ट फ्रेमवर्क है जो एप्लिकेशन को एक डायरेक्टरी ट्री में परिवर्तनों के बारे में नोटिफिकेशन प्राप्त करने की अनुमति देता है। इसका उपयोग आमतौर पर C, Objective-C, या Swift प्रोग्रामिंग में फ़ाइल सिस्टम इवेंट्स जैसे फ़ाइल निर्माण, विलोपन, या संशोधन की निगरानी के लिए किया जाता है। चूंकि `fsevent_watch` एक मान्यता प्राप्त कमांड या फ़ंक्शन नहीं है (यह एक टाइपो या थर्ड-पार्टी टूल हो सकता है), मैं समझाऊंगा कि सीधे FSEvents API का उपयोग कैसे करें, जो संभवतः आपका लक्ष्य है।

यहां एक डायरेक्टरी की निगरानी के लिए FSEvents का उपयोग करने का एक व्यावहारिक मार्गदर्शिका दी गई है:

### C/Objective-C में FSEvents का उपयोग करना
FSEvents API macOS पर CoreServices फ्रेमवर्क का हिस्सा है। परिवर्तनों के लिए एक डायरेक्टरी की निगरानी करने के लिए C में एक बुनियादी उदाहरण नीचे दिया गया है:

1. **आवश्यक हेडर शामिल करें**:
   आपको CoreServices फ्रेमवर्क से FSEvents हेडर को शामिल करने की आवश्यकता होगी।

2. **इवेंट स्ट्रीम सेट अप करें**:
   एक विशिष्ट डायरेक्टरी को देखने के लिए एक इवेंट स्ट्रीम बनाएं, इवेंट्स को हैंडल करने के लिए एक कॉलबैक फ़ंक्शन परिभाषित करें, और इसे एक रन लूप के साथ शेड्यूल करें।

3. **इवेंट्स को हैंडल करें**:
   कॉलबैक इवेंट्स (जैसे, फ़ाइल बदली गई, हटाई गई) को प्रोसेस करता है और पाथ और फ्लैग प्रदान करता है।

यहां एक न्यूनतम उदाहरण दिया गया है:

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// फ़ाइल सिस्टम इवेंट्स को हैंडल करने के लिए कॉलबैक फ़ंक्शन
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
    // मॉनिटर करने के लिए पाथ (उदाहरण के लिए, आपकी होम डायरेक्टरी)
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // इवेंट स्ट्रीम बनाएं
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // अलोकेटर
        &callback,      // कॉलबैक फ़ंक्शन
        NULL,           // कॉलबैक जानकारी (संदर्भ)
        pathsToWatch,   // देखने के लिए पाथ
        kFSEventStreamEventIdSinceNow, // अब से इवेंट्स के साथ शुरू करें
        1.0,            // लेटेंसी सेकंड में (बैचिंग देरी)
        kFSEventStreamCreateFlagNone // फ्लैग (फ़ाइल-लेवल इवेंट्स के लिए kFSEventStreamCreateFlagFileEvents का उपयोग कर सकते हैं)
    );

    // वर्तमान रन लूप पर स्ट्रीम शेड्यूल करें
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // स्ट्रीम शुरू करें
    FSEventStreamStart(stream);

    // इवेंट्स सुनने के लिए लूप चलाएं
    printf("Monitoring /Users/yourusername... Press Ctrl+C to stop.\n");
    CFRunLoopRun();

    // क्लीनअप (इस उदाहरण में रुकने तक पहुंच से बाहर)
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### चरणों की व्याख्या:
- **देखने के लिए पाथ**: आप एक `CFArray` में एक या अधिक डायरेक्टरीज़ (जैसे, `/Users/yourusername`) निर्दिष्ट करते हैं।
- **कॉलबैक**: `callback` फ़ंक्शन तब ट्रिगर होता है जब परिवर्तन होते हैं। यह प्रभावित पाथ और फ्लैग (जैसे, `kFSEventStreamEventFlagItemCreated`) की एक सरणी प्राप्त करता है।
- **स्ट्रीम निर्माण**: `FSEventStreamCreate` वॉचर सेट करता है। लेटेंसी (जैसे, `1.0` सेकंड) कॉलबैक को अभिभूत करने से बचाने के लिए इवेंट्स को बैच करती है।
- **रन लूप**: स्ट्रीम एक रन लूप (जैसे `CFRunLoopRun`) के साथ एकीकृत होती है ताकि प्रोग्राम सक्रिय और उत्तरदायी बना रहे।
- **क्लीनअप**: जब काम पूरा हो जाए तो स्ट्रीम को रोकें और रिलीज़ करें (इस अनंत लूप उदाहरण में नहीं दिखाया गया है)।

#### कंपाइलेशन:
CoreServices फ्रेमवर्क के साथ कंपाइल करें:
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

इसे चलाएं:
```bash
./fsevents_example
```

### मुख्य बिंदु:
- **ग्रैन्युलैरिटी**: डिफ़ॉल्ट रूप से, FSEvents डायरेक्टरी-लेवल परिवर्तनों की निगरानी करता है। फ़ाइल-लेवल इवेंट्स (जैसे, विशिष्ट फ़ाइल संशोधन) के लिए, `kFSEventStreamCreateFlagFileEvents` फ्लैग जोड़ें।
- **लेटेंसी**: लेटेंसी पैरामीटर (जैसे, `1.0`) नियंत्रित करता है कि कॉलबैक कितनी बार फायर होता है। कम मान तेज़ अपडेट देते हैं लेकिन अधिक कॉल करते हैं।
- **स्कोप**: FSEvents पूरी डायरेक्टरी ट्री को रिकर्सिवली देखता है—सबडायरेक्टरीज़ निर्दिष्ट करने की आवश्यकता नहीं है।

### विकल्प: एक टूल का उपयोग करना
यदि आप स्वयं कोडिंग करने के बजाय एक कमांड-लाइन टूल ढूंढ रहे हैं, तो मानक macOS टूलकिट में `fsevent_watch` नहीं है। हालाँकि, थर्ड-पार्टी टूल जैसे `fswatch` FSEvents का लाभ उठाते हैं। `fswatch` का उपयोग करने के लिए:

1. **fswatch इंस्टॉल करें** (उदाहरण के लिए, Homebrew के माध्यम से):
   ```bash
   brew install fswatch
   ```

2. **इसे चलाएं**:
   ```bash
   fswatch /path/to/watch
   ```
   यह परिवर्तन होने पर पाथ आउटपुट करता है। उदाहरण के लिए:
   ```bash
   fswatch ~/Documents
   ```
   जब फाइलें बदलती हैं तो आपको `/Users/yourusername/Documents/file.txt` जैसी लाइनें दिखाई देंगी।

3. **एक स्क्रिप्ट के साथ**:
   कस्टम एक्शन के लिए इसे एक स्क्रिप्ट में पाइप करें:
   ```bash
   fswatch ~/Documents | while read -r file; do echo "Changed: $file"; done
   ```

### यदि आपका कुछ और मतलब था
यदि `fsevent_watch` किसी विशिष्ट लाइब्रेरी, टूल, या टाइपो (जैसे, `fsevents-watch`) को संदर्भित करता है, तो कृपया अधिक संदर्भ प्रदान करें—जैसे कि प्रोग्रामिंग भाषा या वातावरण जिसमें आप काम कर रहे हैं—और मैं प्रतिक्रिया को और परिष्कृत करूंगा।

मुझे बताएं कि मैं इसे आपके लिए और कैसे बेहतर बना सकता हूं!