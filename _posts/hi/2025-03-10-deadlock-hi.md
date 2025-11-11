---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट में गतिरोध
translated: true
type: note
---

आइए एक Spring Boot प्रोजेक्ट में डेडलॉक समस्या को हल करने पर गौर करें, जब एक बीन की मेथड पर कई requests एक साथ पहुंचती हैं। डेडलॉक तब होता है जब दो या दो से अधिक threads एक-दूसरे को अनिश्चित काल के लिए ब्लॉक कर देते हैं, जो अक्सर डेटाबेस लॉक, synchronized blocks, या thread-safe डेटा स्ट्रक्चर जैसे साझा संसाधनों के लिए प्रतिस्पर्धा के कारण होता है। चूंकि आपने एक बीन की मेथड का जिक्र किया है जो कई requests को हैंडल कर रही है, मैं मानकर चलूंगा कि यह एक singleton-scoped बीन (Spring का डिफॉल्ट स्कोप) है और सामान्य कारणों और समाधानों का पता लगाऊंगा।

पहले, इस संदर्भ में संभावित डेडलॉक परिदृश्यों की पहचान करते हैं:
1.  **डेटाबेस लॉक**: यदि बीन की मेथड डेटाबेस के साथ इंटरैक्ट करती है (जैसे, JPA/Hibernate के माध्यम से), तो एक साथ चलने वाले transactions पंक्तियों या टेबलों को विरोधाभासी क्रम में लॉक कर सकते हैं।
2.  **Synchronized Blocks**: यदि मेथड `synchronized` कीवर्ड या लॉक (जैसे, `ReentrantLock`) का उपयोग करती है, तो अनुचित लॉक ऑर्डरिंग के कारण threads एक-दूसरे की प्रतीक्षा कर सकते हैं।
3.  **साझा संसाधन**: यदि बीन एक साझा in-memory संसाधन (जैसे, static variable या collection) को संशोधित करती है, तो होड़ (contention) डेडलॉक का कारण बन सकती है।
4.  **बाहरी कॉल**: यदि मेथड बाहरी सेवाओं या APIs को कॉल करती है, तो देरी या ब्लॉकिंग व्यवहार समवर्तीता (concurrency) समस्याओं को बढ़ा सकता है।

चूंकि आपने विशिष्ट कोड साझा नहीं किया है, मैं समस्या का निदान और समाधान करने के लिए एक सामान्य दृष्टिकोण प्रदान करूंगा, और फिर एक ठोस उदाहरण दूंगा।

### चरण 1: डेडलॉक का निदान करें
- **लॉगिंग सक्षम करें**: मेथड के प्रवेश, निकास और संसाधन एक्सेस का पता लगाने के लिए लॉगिंग (जैसे, SLF4J with Logback) जोड़ें। इससे यह पहचानने में मदद मिलती है कि threads कहां अटकती हैं।
- **Thread Dump**: जब डेडलॉक होता है, तो एक thread dump कैप्चर करें (जैसे, `jstack` या VisualVM का उपयोग करके)। `BLOCKED` या `WAITING` स्थिति वाले threads को देखें और लॉक होड़ (contention) के लिए उनके stack traces की जांच करें।
- **मॉनिटरिंग**: लोड के तहत thread व्यवहार का अवलोकन करने के लिए Spring Actuator या profiler (जैसे, YourKit) जैसे टूल्स का उपयोग करें।

### चरण 2: सामान्य समाधान
संभावित कारणों के आधार पर डेडलॉक को ठीक करने का तरीका यहां बताया गया है:

#### केस 1: डेटाबेस-संबंधी डेडलॉक
यदि बीन की मेथड डेटाबेस ऑपरेशन करती है, तो डेडलॉक अक्सर transaction conflicts से उत्पन्न होता है।
- **समाधान**: transaction की सीमाओं और लॉक अधिग्रहण के क्रम को अनुकूलित करें।
  - एक उचित isolation level (जैसे, `SERIALIZABLE` की बजाय `READ_COMMITTED` जब तक कि सख्त जरूरत न हो) के साथ `@Transactional` का उपयोग करें।
  - संसाधन एक्सेस के सुसंगत क्रम को सुनिश्चित करें (जैसे, हमेशा टेबल B से पहले टेबल A को अपडेट करें)।
  - गैर-लेनदेन तर्क (non-transactional logic) को `@Transactional` के बाहर ले जाकर transaction scope को कम करें।
- **उदाहरण**:
  ```java
  @Service
  public class MyService {
      @Autowired
      private MyRepository repo;

      @Transactional
      public void processRequest(Long id1, Long id2) {
          // डेडलॉक से बचने के लिए सुसंगत क्रम सुनिश्चित करें
          if (id1 < id2) {
              repo.updateEntity(id1);
              repo.updateEntity(id2);
          } else {
              repo.updateEntity(id2);
              repo.updateEntity(id1);
          }
      }
  }
  ```
- **बोनस**: लंबे समय तक चलने वाले transactions को रोकने और अनिश्चितकालीन प्रतीक्षा को रोकने के लिए एक transaction timeout सेट करें (जैसे, `@Transactional(timeout = 5)`).

#### केस 2: Synchronized Blocks या लॉक
यदि मेथड स्पष्ट लॉकिंग (explicit locking) का उपयोग करती है, तो डेडलॉक तब हो सकता है जब लॉक विभिन्न threads में अलग-अलग क्रम में प्राप्त किए जाते हैं।
- **समाधान**: एकल लॉक का उपयोग करें या लॉक ऑर्डरिंग लागू करें।
  - यदि संभव हो तो कई `synchronized` blocks को एक single coarse-grained lock से बदलें।
  - अनिश्चितकालीन ब्लॉकिंग से बचने के लिए timeout के साथ `ReentrantLock` का उपयोग करें।
- **उदाहरण**:
  ```java
  @Service
  public class MyService {
      private final ReentrantLock lock = new ReentrantLock();

      public void processRequest(String resourceA, String resourceB) {
          try {
              if (lock.tryLock(2, TimeUnit.SECONDS)) {
                  // Critical section
                  System.out.println("Processing " + resourceA + " and " + resourceB);
              } else {
                  throw new RuntimeException("Could not acquire lock in time");
              }
          } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
          } finally {
              if (lock.isHeldByCurrentThread()) {
                  lock.unlock();
              }
          }
      }
  }
  ```

#### केस 3: साझा In-Memory संसाधन
यदि बीन एक साझा collection या variable को संशोधित करती है, तो समवर्ती एक्सेस (concurrent access) समस्याएं पैदा कर सकती है।
- **समाधान**: thread-safe विकल्पों का उपयोग करें या साझा state से बचें।
  - `ArrayList` को `CopyOnWriteArrayList` या `Collections.synchronizedList` से बदलें।
  - maps के लिए `ConcurrentHashMap` का उपयोग करें।
  - इससे भी बेहतर, बीन को stateless बनाएं या request-scoped beans (`@Scope("request")`) का उपयोग करें।
- **उदाहरण**:
  ```java
  @Service
  @Scope("prototype") // stateful होने पर singleton से बचें
  public class MyService {
      private final ConcurrentHashMap<String, Integer> cache = new ConcurrentHashMap<>();

      public void processRequest(String key, int value) {
          cache.put(key, value); // Thread-safe
      }
  }
  ```

#### केस 4: उच्च समवर्तीता लोड (High Concurrency Load)
यदि डेडलॉक बीन पर बहुत अधिक requests के कारण होता है, तो thread contention मूल कारण हो सकता है।
- **समाधान**: asynchronous processing या rate limiting शुरू करें।
  - काम को thread pool में ऑफलोड करने के लिए `@Async` का उपयोग करें।
  - समवर्तीता (concurrency) को प्रबंधित करने के लिए `TaskExecutor` के साथ एक thread pool कॉन्फ़िगर करें।
- **उदाहरण**:
  ```java
  @Service
  public class MyService {
      @Async
      public CompletableFuture<String> processRequest(String input) {
          // काम का अनुकरण करें
          Thread.sleep(1000);
          return CompletableFuture.completedFuture("Done: " + input);
      }
  }

  @Configuration
  @EnableAsync
  public class AsyncConfig {
      @Bean
      public TaskExecutor taskExecutor() {
          ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
          executor.setCorePoolSize(10);
          executor.setMaxPoolSize(50);
          executor.setQueueCapacity(100);
          return executor;
      }
  }
  ```
- **उपयोग**: `processRequest` को कॉल करें और controller में `CompletableFuture` को हैंडल करें।

### चरण 3: भविष्य की समस्याओं को रोकें
- **लोड टेस्टिंग**: डेडलॉक को जल्दी पकड़ने के लिए JMeter या Gatling जैसे टूल्स के साथ उच्च समवर्तीता (high concurrency) का अनुकरण करें।
- **कोड रिव्यू**: nested locks, लंबे समय तक चलने वाले transactions, या साझा mutable state की जांच करें।
- **टाइमआउट**: लॉक, transactions, या बाहरी कॉल के लिए हमेशा timeouts सेट करें।

### अंतिम विचार
आपके बीन के कोड को देखे बिना, मैंने एक singleton बीन को भारी लोड के तहत माना है जिसमें संभावित डेटाबेस या लॉक contention है। यदि आप अधिक जानकारी साझा करते हैं (जैसे, मेथड का कोड, stack traces, या यह किन संसाधनों तक पहुंचता है), तो मैं समाधान को और अनुकूलित कर सकता हूं। अभी के लिए, thread dump के साथ निदान शुरू करें और relevant fix लागू करें—डेटाबेस ऑप्टिमाइजेशन, लॉक प्रबंधन, या async processing। मुझे बताएं कि यह कैसे जाता है!