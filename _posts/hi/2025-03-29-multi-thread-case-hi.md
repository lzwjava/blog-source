---
audio: false
generated: true
lang: hi
layout: post
title: एक बहु-थ्रेडेड मामला
translated: true
type: note
---

Java Spring Boot प्रोजेक्ट में 10 नियमों के साथ मल्टी-थ्रेडेड वैलिडेशन को हैंडल करने के लिए, जहां कुछ नियम डेटाबेस तक पहुंच सकते हैं और आप बाकी को रद्द करना चाहते हैं जैसे ही कोई एक विफल होता है ताकि समय बर्बाद न हो, आप Spring की सुविधाओं के साथ Java के concurrency utilities का उपयोग कर सकते हैं। यहां एक पूर्ण और कुशल समाधान दिया गया है:

### दृष्टिकोण अवलोकन
- **वैलिडेशन को समवर्ती रूप से चलाएं**: सभी नियम पास होने पर प्रक्रिया को तेज करने के लिए 10 वैलिडेशन नियमों को समानांतर में निष्पादित करने के लिए कई थ्रेड्स का उपयोग करें।
- **विफलता पर रद्द करें**: जैसे ही कोई नियम विफल होता है, शेष वैलिडेशन को रोकें, अनावश्यक कार्य को कम से कम करें।
- **Spring का लाभ उठाएं**: डेटाबेस-एक्सेस करने वाले नियमों के लिए Spring की dependency injection और transaction management का उपयोग करें।

इसे प्राप्त करने का सबसे अच्छा तरीका `ExecutorService` को `CompletionService` के साथ जोड़ना है। `CompletionService` आपको कार्य परिणामों को उनके पूरा होने के रूप में प्रोसेस करने की अनुमति देता है, जो विफलता की तत्काल पहचान और लंबित कार्यों के रद्द होने को सक्षम बनाता है।

---

### चरण-दर-चरण समाधान

#### 1. वैलिडेशन नियमों को परिभाषित करें
10 नियमों में से प्रत्येक एक स्वतंत्र वैलिडेशन कार्य होना चाहिए। कुछ नियमों में डेटाबेस एक्सेस शामिल हो सकता है, इसलिए उन्हें transactional methods के साथ एक service में encapsulate करें।

```java
@Service
public class RuleValidator {
    // उदाहरण: डेटाबेस तक पहुंचने वाला नियम
    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // नियम वैलिडेशन का अनुकरण करें, उदा., डेटाबेस क्वेरी
        // यदि नियम पास होता है तो true लौटाएं, false यदि विफल होता है
        return performValidation(ruleId); // कार्यान्वयन आपके तर्क पर निर्भर करता है
    }

    private boolean performValidation(int ruleId) {
        // वास्तविक वैलिडेशन लॉजिक से बदलें
        return ruleId % 2 == 0; // उदाहरण: सम नियम ID पास होते हैं
    }
}
```

- डेटाबेस से केवल पढ़ने वाले नियमों के लिए `@Transactional(readOnly = true)` का उपयोग करें, यह सुनिश्चित करते हुए कि प्रत्येक थ्रेड-सुरक्षित तरीके से अपने स्वयं के transaction context में चलता है।

#### 2. एक ExecutorService कॉन्फ़िगर करें
वैलिडेशन कार्यों के समवर्ती निष्पादन को प्रबंधित करने के लिए एक थ्रेड पूल को परिभाषित करें। Spring में, आप इसे एक bean के रूप में बना सकते हैं:

```java
@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // 10 नियमों के लिए 10 थ्रेड्स
    }
}
```

- थ्रेड पूल का आकार अपने सिस्टम की क्षमताओं (जैसे, CPU cores, डेटाबेस कनेक्शन सीमाएं) के आधार पर समायोजित करें।

#### 3. मल्टी-थ्रेडेड वैलिडेशन लागू करें
`CompletionService` का उपयोग करके वैलिडेशन प्रक्रिया को orchestrate करने वाली एक service बनाएं:

```java
@Service
public class ValidationService {
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    public boolean validateAllRules() {
        // चरण 1: वैलिडेशन कार्य बनाएं
        List<Callable<Boolean>> tasks = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            tasks.add(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    // अपवादों को (जैसे, डेटाबेस त्रुटियां) विफलताओं के रूप में हैंडल करें
                    log.error("Validation failed for rule " + ruleId, e);
                    return false;
                }
            });
        }

        // चरण 2: CompletionService सेट अप करें और कार्य submit करें
        CompletionService<Boolean> completionService = new ExecutorCompletionService<>(executorService);
        List<Future<Boolean>> futures = new ArrayList<>();
        for (Callable<Boolean> task : tasks) {
            futures.add(completionService.submit(task));
        }

        // चरण 3: परिणामों को प्रोसेस करें जैसे ही वे पूरे होते हैं
        boolean hasFailed = false;
        for (int i = 0; i < 10; i++) {
            try {
                Future<Boolean> completed = completionService.take(); // अगले कार्य के पूरा होने तक ब्लॉक करता है
                boolean result = completed.get();
                if (!result) {
                    hasFailed = true;
                    break; // एक बार विफलता मिलने पर जांच रोकें
                }
            } catch (InterruptedException | ExecutionException e) {
                log.error("Error during validation", e);
                hasFailed = true;
                break;
            }
        }

        // चरण 4: यदि कोई विफलता हुई है तो शेष कार्यों को रद्द करें
        if (hasFailed) {
            for (Future<Boolean> future : futures) {
                if (!future.isDone()) {
                    future.cancel(true); // चल रहे कार्यों को इंटरप्ट करें
                }
            }
            return false; // वैलिडेशन विफल रहा
        }

        return true; // सभी नियम पास हुए
    }
}
```

#### यह कैसे काम करता है
- **कार्य निर्माण**: प्रत्येक वैलिडेशन नियम एक `Callable<Boolean>` में लपेटा जाता है जो `true` लौटाता है यदि नियम पास होता है और `false` यदि विफल होता है। अपवादों को पकड़ा जाता है और विफलताओं के रूप में माना जाता है।
- **समवर्ती निष्पादन**: कार्यों को `CompletionService` में submit किया जाता है, जो उन्हें थ्रेड पूल का उपयोग करके समानांतर में चलाता है। कार्य स्थिति को ट्रैक करने के लिए Futures एकत्र किए जाते हैं।
- **परिणाम प्रसंस्करण**: `completionService.take()` अगले पूरे हुए कार्य का परिणाम प्राप्त करता है। यदि कोई परिणाम `false` है, तो लूप टूट जाता है, और `hasFailed` सेट हो जाता है।
- **रद्द करना**: विफलता पर, `future.cancel(true)` का उपयोग करके सभी अधूरे कार्य रद्द कर दिए जाते हैं, जो चल रहे थ्रेड्स को इंटरप्ट करने का प्रयास करता है।
- **परिणाम**: `false` लौटाता है यदि कोई नियम विफल होता है, `true` यदि सभी पास होते हैं।

---

### मुख्य विचार
- **डेटाबेस एक्सेस**: चूंकि नियम डेटाबेस तक पहुंच सकते हैं, `@Transactional` थ्रेड-सुरक्षित ऑपरेशन सुनिश्चित करता है। प्रत्येक कार्य अपने स्वयं के transaction में चलता है, जो स्वतंत्र वैलिडेशन के लिए उपयुक्त है।
- **कार्य रद्दीकरण**: एक `Future` को रद्द करना थ्रेड को इंटरप्ट करता है, लेकिन चल रही डेटाबेस क्वेरीज तुरंत नहीं रुक सकती हैं। हालांकि, यह आगे की प्रोसेसिंग को रोकता है और मुख्य थ्रेड को आगे बढ़ने देता है।
- **अपवाद हैंडलिंग**: अपवादों (जैसे, डेटाबेस त्रुटियों) को कार्यों के भीतर पकड़ा जाता है और विफलताओं के रूप में माना जाता है, जिससे मजबूत व्यवहार सुनिश्चित होता है।
- **थ्रेड पूल आकार**: सादगी के लिए 10 पर सेट किया गया है (एक थ्रेड प्रति नियम), लेकिन अपने एप्लिकेशन की आवश्यकताओं और संसाधनों के आधार पर अनुकूलित करें।

---

### यह दृष्टिकोण सबसे अच्छा क्यों है
- **दक्षता**: वैलिडेशन समवर्ती रूप से चलते हैं, कुल समय कम करते हैं जब सभी पास होते हैं।
- **शीघ्र समाप्ति**: `CompletionService` तत्काल विफलता का पता लगाने की अनुमति देता है, और रद्दीकरण अनावश्यक कार्य को रोकता है।
- **सरलता**: मानक Java concurrency utilities का लाभ उठाता है और Spring Boot के साथ सहजता से एकीकृत होता है।
- **मापनीयता**: थ्रेड पूल और कार्य सूची को समायोजित करके अधिक नियमों के लिए आसानी से विस्तार योग्य।

वैकल्पिक दृष्टिकोण जैसे `CompletableFuture` या टाइमआउट के साथ `Future` परिणामों की पोलिंग पर विचार किया गया, लेकिन `CompletionService` इस उपयोग के मामले के लिए अधिक सीधा है, क्योंकि यह पूरा होने के क्रम में परिणामों को कुशलतापूर्वक संभालता है और रद्दीकरण का समर्थन करता है।

---

### उपयोग उदाहरण
अपने controller या business logic में service को inject करें और call करें:

```java
@RestController
public class ValidationController {
    private final ValidationService validationService;

    @Autowired
    public ValidationController(ValidationService validationService) {
        this.validationService = validationService;
    }

    @GetMapping("/validate")
    public ResponseEntity<String> validate() {
        boolean result = validationService.validateAllRules();
        return ResponseEntity.ok(result ? "All rules passed" : "Validation failed");
    }
}
```

यह समाधान आपकी आवश्यकताओं को पूरा करता है: यह 10 वैलिडेशन नियमों को समानांतर में चलाता है, शेष कार्यों को रद्द कर देता है जब कोई एक विफल होता है, और समय बर्बाद होने से बचाता है, यह सब Spring Boot के साथ साफ-सुथरे ढंग से एकीकृत होते हुए।