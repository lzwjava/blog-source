---
audio: false
generated: true
lang: hi
layout: post
title: गतिशील क्षेत्र-विशिष्ट बीन्स
translated: true
type: note
---

### आवश्यकता को समझना

ऐसा लगता है कि आप एक Spring Boot/Java Spring एप्लिकेशन बना रहे हैं जिसे कई क्षेत्रों (या "राष्ट्रीयताओं") जैसे कि सिंगापुर (SG), हांगकांग (HK), और ताइवान (TW) का समर्थन करने की आवश्यकता है। आप `@Autowired` और बीन प्रबंधन जैसी सुविधाओं का उपयोग करके, विशेष रूप से एक `CoreController` क्लास के लिए, विभिन्न बीन्स को डायनामिक रूप से लोड या इंजेक्ट करना चाहते हैं।

यह **मल्टी-टेनेंसी** या **क्षेत्र-विशिष्ट कॉन्फ़िगरेशन** के लिए एक सामान्य परिदृश्य है, जहां व्यवहार (जैसे, सेवाएं, कॉन्फ़िगरेशन, या कंट्रोलर) क्षेत्र के अनुसार भिन्न होता है। Spring में, आप रनटाइम पर पूरी कंट्रोलर क्लास को आसानी से स्विच नहीं कर सकते, लेकिन आप यह कर सकते हैं:

1. **Spring Profiles** का उपयोग पर्यावरण-विशिष्ट बीन लोडिंग के लिए करें (जैसे, प्रत्येक क्षेत्र के लिए अलग-अलग डिप्लॉयमेंट या एक्टिवेशन)। यह कंपाइल-टाइम या स्टार्टअप-टाइम होता है।
2. **रनटाइम चयन** का उपयोग Strategy Pattern के साथ करें, जहां आप कई बीन्स इंजेक्ट करते हैं (जैसे, एक Map के माध्यम से) और सही एक का चयन एक रिक्वेस्ट पैरामीटर, हेडर, या कॉन्टेक्स्ट (जैसे, उपयोगकर्ता का क्षेत्र) के आधार पर करते हैं।

चूंकि आपने "बहु-राष्ट्रीयता विकास" और SG/HK/TW जैसे उदाहरणों का उल्लेख किया है, मैं मानूंगा कि इसके लिए एक ही एप्लिकेशन इंस्टेंस में कई क्षेत्रों को हैंडल करने की आवश्यकता है (रनटाइम स्विचिंग)। यदि यह क्षेत्र के अनुसार अलग-अलग डिप्लॉयमेंट है, तो प्रोफाइल सरल हैं।

मैं दोनों दृष्टिकोणों को कोड उदाहरणों के साथ समझाऊंगा। हम मानेंगे कि `CoreController` एक क्षेत्र-विशिष्ट सेवा (जैसे, `CoreService` इंटरफेस जिसमें प्रत्येक क्षेत्र के लिए इम्प्लीमेंटेशन हैं) पर निर्भर करता है। इस तरह, कंट्रोलर वही रहता है, लेकिन इसका व्यवहार इंजेक्ट की गई बीन्स के माध्यम से बदल जाता है।

### दृष्टिकोण 1: क्षेत्र-विशिष्ट बीन लोडिंग के लिए Spring Profiles का उपयोग (स्टार्टअप-टाइम)

यह आदर्श है यदि आप प्रति क्षेत्र अलग-अलग इंस्टेंस डिप्लॉय करते हैं (जैसे, पर्यावरण चर या एप्लिकेशन गुणों के माध्यम से)। बीन्स सक्रिय प्रोफाइल के आधार पर सशर्त रूप से लोड होती हैं।

#### चरण 1: इंटरफेस और इम्प्लीमेंटेशन परिभाषित करें
क्षेत्र-विशिष्ट लॉजिक के लिए एक इंटरफेस बनाएं:

```java
public interface CoreService {
    String getRegionMessage();
}
```

प्रत्येक क्षेत्र के लिए इम्प्लीमेंटेशन:

```java
// SgCoreService.java
@Service
@Profile("sg")  // यह बीन केवल तभी लोड होगी जब 'sg' प्रोफाइल सक्रिय हो
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service
@Profile("hk")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service
@Profile("tw")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### चरण 2: CoreController में Autowire करें
```java
@RestController
public class CoreController {
    private final CoreService coreService;

    @Autowired
    public CoreController(CoreService coreService) {
        this.coreService = coreService;
    }

    @GetMapping("/message")
    public String getMessage() {
        return coreService.getRegionMessage();
    }
}
```

#### चरण 3: प्रोफाइल सक्रिय करें
- `application.properties` में या कमांड लाइन के माध्यम से:
  - सिंगापुर की बीन्स के लिए `--spring.profiles.active=sg` के साथ रन करें।
  - यह सुनिश्चित करता है कि केवल `SgCoreService` बीन बनाई और ऑटोवायर्ड हो।
- प्रोफाइल से परे कस्टम शर्तों के लिए, `@ConditionalOnProperty` का उपयोग करें (जैसे, `@ConditionalOnProperty(name = "app.region", havingValue = "sg")`)।

यह दृष्टिकोण सरल है लेकिन प्रति क्षेत्र एप्लिकेशन को रीस्टार्ट करने या अलग करने की आवश्यकता होती है। एक रनटाइम इंस्टेंस में सभी क्षेत्रों को हैंडल करने के लिए उपयुक्त नहीं है।

### दृष्टिकोण 2: @Autowired Map के साथ रनटाइम बीन चयन (Strategy Pattern)

एक ही एप्लिकेशन के लिए जो कई क्षेत्रों को डायनामिक रूप से हैंडल करता है (जैसे, HTTP रिक्वेस्ट हेडर जैसे `X-Region: sg` के आधार पर), बीन्स के एक Map का उपयोग करें। Spring सभी इम्प्लीमेंटेशन को एक Map<String, CoreService> में ऑटोवायर कर सकता है, जहां कुंजी बीन का नाम है।

#### चरण 1: इंटरफेस और इम्प्लीमेंटेशन परिभाषित करें
ऊपर के समान, लेकिन `@Profile` के बिना:

```java
public interface CoreService {
    String getRegionMessage();
}

// SgCoreService.java
@Service("sgCoreService")  // Map कुंजी के लिए स्पष्ट बीन नाम
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service("hkCoreService")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service("twCoreService")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### चरण 2: CoreController में एक Map ऑटोवायर करें
```java
@RestController
public class CoreController {
    private final Map<String, CoreService> coreServices;

    @Autowired  // Spring सभी CoreService बीन्स को Map में स्वचालित रूप से भर देता है, कुंजी बीन नाम से होती है
    public CoreController(Map<String, CoreService> coreServices) {
        this.coreServices = coreServices;
    }

    @GetMapping("/message")
    public String getMessage(@RequestHeader("X-Region") String region) {  // या @RequestParam का उपयोग करें यदि यह क्वेरी पैरामीटर है
        CoreService service = coreServices.get(region.toLowerCase() + "CoreService");
        if (service == null) {
            throw new IllegalArgumentException("Unsupported region: " + region);
        }
        return service.getRegionMessage();
    }
}
```

- यहां, Map पर `@Autowired` सभी `CoreService` इम्प्लीमेंटेशन को स्वचालित रूप से इंजेक्ट करता है।
- बीन नाम आपकी कुंजी लॉजिक से मेल खाने चाहिए (जैसे, "sgCoreService")।
- चयन के लिए: क्षेत्र निर्धारित करने के लिए एक रिक्वेस्ट हेडर/पैरामीटर का उपयोग करें। यह इसे प्रति रिक्वेस्ट डायनामिक बनाता है।

#### वैकल्पिक: विशिष्ट इंजेक्शन के लिए @Qualifier का उपयोग करना
यदि आप मैन्युअल रूप से एक विशिष्ट बीन इंजेक्ट करना चाहते हैं:

```java
@RestController
public class CoreController {
    @Autowired
    @Qualifier("sgCoreService")  // केवल SG बीन इंजेक्ट करता है
    private CoreService sgCoreService;

    // ... अन्य के लिए इसी तरह
}
```
लेकिन यह डायनामिक नहीं है; रनटाइम स्विचिंग के लिए Map का उपयोग करें।

#### चरण 3: कॉन्फ़िगरेशन और सर्वोत्तम अभ्यास
- आपकी Spring Boot मुख्य क्लास में: `@SpringBootApplication` पर्याप्त है; Spring `@Service` बीन्स के लिए स्कैन करता है।
- डिफ़ॉल्ट हैंडल करें: यदि कोई क्षेत्र मेल नहीं खाता है तो एक फॉलबैक सेवा जोड़ें।
- अधिक जटिल शर्तों के लिए, बीन्स पर `@ConditionalOnExpression` या कस्टम `@Conditional` एनोटेशन का उपयोग करें।
- थ्रेड सुरक्षा: चूंकि कंट्रोलर डिफ़ॉल्ट रूप से सिंगलटन होते हैं, Map तब तक सुरक्षित है जब तक सेवाएं स्टेटलेस हैं।
- परीक्षण: विभिन्न क्षेत्रों का परीक्षण करने के लिए मॉक रिक्वेस्ट के साथ `@SpringBootTest` का उपयोग करें।

### किस दृष्टिकोण को चुनना है?
- **प्रोफाइल** का उपयोग करें यदि क्षेत्र डिप्लॉयमेंट/पर्यावरण द्वारा अलग किए गए हैं (जैसे, SG/HK/TW के लिए अलग-अलग सर्वर)।
- **Map/Strategy** का उपयोग एक एकीकृत एप्लिकेशन के लिए करें जो रनटाइम पर सभी क्षेत्रों को हैंडल करता है (माइक्रोसर्विसेज के लिए अधिक लचीला)।

यदि यह आपके सटीक सेटअप से मेल नहीं खाता है (जैसे, यदि `CoreController` को स्वयं प्रति क्षेत्र अलग होने की आवश्यकता है), तो आप `@RequestMapping` शर्तों के साथ कई कंट्रोलर या कंट्रोलर को डायनामिक रूप से बनाने के लिए एक फैक्टरी का उपयोग कर सकते हैं - लेकिन यह दुर्लभ और अधिक जटिल है।

यदि आप अधिक विवरण प्रदान करते हैं (जैसे, क्षेत्र कैसे निर्धारित होता है), तो मैं इसे और परिष्कृत कर सकता हूं!