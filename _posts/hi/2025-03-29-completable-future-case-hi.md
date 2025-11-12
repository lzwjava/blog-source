---
audio: false
generated: true
lang: hi
layout: post
title: मल्टी-थ्रेडेड वैलिडेशन को कंप्लीटेबलफ्यूचर के साथ लागू करना
translated: true
type: note
---

अगर हम Spring Boot एप्लिकेशन में मल्टी-थ्रेडेड वैलिडेशन के लिए `CompletableFuture` का उपयोग करते हैं, तो यह एसिंक्रोनस टास्क्स को हैंडल करने का एक आधुनिक और लचीला तरीका प्रदान करता है। नीचे, मैं समझाऊंगा कि इसे कैसे इम्प्लीमेंट किया जाए, इसके फायदों और चुनौतियों को हाइलाइट करूंगा, और कई नियमों को एक साथ वैलिडेट करने के लिए तैयार किया गया एक पूरा सॉल्यूशन दूंगा।

### CompletableFuture के साथ मल्टी-थ्रेडेड वैलिडेशन को इम्प्लीमेंट करना

`CompletableFuture` Java की कंकरेंसी API का हिस्सा है और आपको एसिंक्रोनस रूप से टास्क्स को एक्जीक्यूट करने, ऑपरेशंस को चेन करने और रिजल्ट्स या एक्सेप्शंस को सुरुचिपूर्ण तरीके से हैंडल करने की अनुमति देता है। यहां बताया गया है कि हम इसका उपयोग कई नियमों को समानांतर रूप से वैलिडेट करने के लिए कैसे कर सकते हैं, जैसे ही एक फेल होता है वैसे ही रुक जाते हैं।

#### चरण 1: वैलिडेशन लॉजिक को डिफाइन करें

पहले, मान लें कि हमारे पास एक सर्विस है जो अलग-अलग वैलिडेशन नियमों को डिफाइन करती है। प्रत्येक नियम में डेटाबेस एक्सेस या कॉम्प्लेक्स लॉजिक शामिल हो सकता है, इसलिए हम उचित ट्रांजैक्शन मैनेजमेंट के लिए Spring के `@Transactional` एनोटेशन का उपयोग करेंगे।

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class RuleValidator {

    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // वैलिडेशन लॉजिक का सिमुलेशन (जैसे, डेटाबेस क्वेरी)
        return performValidation(ruleId);
    }

    private boolean performValidation(int ruleId) {
        // उदाहरण: सम rule ID पास होते हैं, विषम फेल
        return ruleId % 2 == 0;
    }
}
```

#### चरण 2: CompletableFuture के साथ वैलिडेशन सर्विस को इम्प्लीमेंट करें

अब, आइए एक सर्विस बनाएं जो `CompletableFuture` का उपयोग करके कई वैलिडेशन नियमों को एक साथ चलाती है। हम थ्रेड्स को मैनेज करने के लिए एक `ExecutorService` का उपयोग करेंगे और यह सुनिश्चित करेंगे कि अगर कोई नियम फेल होता है, तो हम बाकी के प्रोसेसिंग को रोक सकें।

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;

@Service
public class ValidationService {
    private static final Logger log = LoggerFactory.getLogger(ValidationService.class);
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    public boolean validateAllRules() {
        // सभी futures को होल्ड करने के लिए एक लिस्ट बनाएं
        List<CompletableFuture<Boolean>> futures = new ArrayList<>();

        // 10 वैलिडेशन नियम सबमिट करें (उदाहरण के लिए)
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            CompletableFuture<Boolean> future = CompletableFuture.supplyAsync(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    log.error("Validation failed for rule " + ruleId, e);
                    return false; // एक्सेप्शंस को फेलियर मानें
                }
            }, executorService);
            futures.add(future);
        }

        // समग्र रिजल्ट को ट्रैक करने के लिए एक future बनाएं
        CompletableFuture<Boolean> resultFuture = new CompletableFuture<>();

        // फेलियर के लिए प्रत्येक future को मॉनिटर करें
        for (CompletableFuture<Boolean> future : futures) {
            future.thenAccept(result -> {
                if (!result && !resultFuture.isDone()) {
                    // पहली फेलियर डिटेक्ट हो गई
                    resultFuture.complete(false);
                    // बचे हुए टास्क्स को कैंसल करें
                    futures.forEach(f -> {
                        if (!f.isDone()) {
                            f.cancel(true);
                        }
                    });
                }
            });
        }

        // अगर सभी futures सफलतापूर्वक कंप्लीट हो जाते हैं, तो true मार्क करें
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                .thenRun(() -> {
                    if (!resultFuture.isDone()) {
                        resultFuture.complete(true);
                    }
                });

        try {
            return resultFuture.get(); // रिजल्ट उपलब्ध होने तक ब्लॉक करें
        } catch (InterruptedException | ExecutionException e) {
            log.error("Error during validation", e);
            return false;
        }
    }
}
```

#### यह कैसे काम करता है

1. **टास्क सबमिशन**:
   - हम `supplyAsync()` का उपयोग करके प्रत्येक नियम के लिए एक `CompletableFuture` बनाते हैं, जो वैलिडेशन लॉजिक को एसिंक्रोनस रूप से चलाता है।
   - `executorService` (Spring के माध्यम से इंजेक्ट किया गया) थ्रेड पूल को मैनेज करता है।

2. **फेलियर डिटेक्शन**:
   - प्रत्येक future को `thenAccept()` का उपयोग करके मॉनिटर किया जाता है। अगर कोई नियम `false` रिटर्न करता है, तो हम `resultFuture` को `false` के साथ कंप्लीट करते हैं और बाकी futures को कैंसल कर देते हैं।

3. **सक्सेस केस**:
   - `CompletableFuture.allOf()` सभी futures के कंप्लीट होने का इंतज़ार करता है। अगर कोई फेलियर नहीं होती है, तो यह `resultFuture` को `true` के साथ कंप्लीट करता है।

4. **रिजल्ट रिट्रीवल**:
   - हम फाइनल रिजल्ट प्राप्त करने के लिए `resultFuture.get()` पर ब्लॉक करते हैं, और होने वाले किसी भी एक्सेप्शन को हैंडल करते हैं।

### CompletableFuture का उपयोग करने के फायदे

- **लचीलापन**: आप रिजल्ट्स को आगे प्रोसेस करने के लिए ऑपरेशंस को चेन कर सकते हैं (जैसे, `thenApply`, `thenCompose`)।
- **एक्सेप्शन हैंडलिं**: `exceptionally()` या `handle()` जैसी बिल्ट-इन मेथड्स एरर्स को मैनेज करना आसान बनाती हैं।
- **नॉन-ब्लॉकिंग डिजाइन**: यह रिएक्टिव प्रोग्रामिंग स्टाइल को सपोर्ट करता है, जिसे और अधिक कॉम्प्लेक्स वर्कफ़्लो के लिए एक्सटेंड किया जा सकता है।

### चुनौतियां

- **कैंसलेशन**: `ExecutorService` के साथ `CompletionService` (जहां आप आसानी से पहले रिजल्ट के लिए पोल कर सकते हैं और बाकी को कैंसल कर सकते हैं) के विपरीत, `CompletableFuture` में एक के फेल होने पर दूसरे futures को मैन्युअल रूप से कैंसल करने की आवश्यकता होती है। इससे कॉम्प्लेक्सिटी बढ़ जाती है।
- **जटिलता**: `ExecutorService` के साथ सरल लूप-आधारित दृष्टिकोण की तुलना में कोड पढ़ने और मेंटेन करने में कठिन हो सकता है।

### उदाहरण उपयोग

इसे Spring Boot एप्लिकेशन में उपयोग करने के लिए, आप एक `ExecutorService` बीन कॉन्फ़िगर करेंगे:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // आवश्यकतानुसार साइज एडजस्ट करें
    }
}
```

फिर, कंट्रोलर या किसी अन्य कंपोनेंट से सर्विस को कॉल करें:

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

### निष्कर्ष

Spring Boot में मल्टी-थ्रेडेड वैलिडेशन के लिए `CompletableFuture` का उपयोग एक व्यवहार्य दृष्टिकोण है, खासकर यदि आप इसकी एसिंक्रोनस, चेन करने योग्य प्रकृति को महत्व देते हैं। यह आपको वैलिडेशन नियमों को एक साथ चलाने और रिजल्ट्स को लचीले ढंग से हैंडल करने की अनुमति देता है। हालांकि, अगर आपका प्राथमिक लक्ष्य सरलता है—खासकर पहली फेलियर को डिटेक्ट करने और बाकी टास्क्स को कैंसल करने के लिए—तो पारंपरिक `ExecutorService` के साथ `CompletionService` को इम्प्लीमेंट और मेंटेन करना आसान हो सकता है। `CompletableFuture` के साथ, आपको थोड़ी अधिक जटिल कैंसलेशन लॉजिक की कीमत पर शक्ति और लचीलापन मिलता है।