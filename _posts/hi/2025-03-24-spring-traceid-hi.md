---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट लॉग4ज रिक्वेस्ट ट्रेसिंग
translated: true
type: note
---

एक Java Spring Boot एप्लिकेशन में जो Log4j का उपयोग करता है और जिसमें बिल्ट-इन ट्रेस ID डिज़ाइन नहीं है, किसी विशिष्ट लॉग एंट्री को फ्रंटएंड-इनिशिएटेड रिक्वेस्ट से वापस जोड़ना वाकई चुनौतीपूर्ण हो सकता है। आप सही हैं कि Log4j में `%t` (थ्रेड नाम) उन लॉग्स की पहचान करने में मदद कर सकता है जो किसी विशिष्ट थ्रेड से जुड़े हैं, लेकिन जैसा कि आपने नोट किया है, यह तब कम विश्वसनीय हो जाता है जब रिक्वेस्ट्स कई थ्रेड्स में फैल जाती हैं (उदाहरण के लिए, एसिंक्रोनस प्रोसेसिंग, थ्रेड पूल, या डाउनस्ट्रीम कॉल्स के कारण)। लॉग्स को खोजने के लिए टाइम रेंज का उपयोग करना एक वर्कअराउंड है, लेकिन यह अशुद्ध और बोझिल है, खासकर हाई-ट्रैफिक सिस्टम में। आइए अपनी पूरी सेटअप को बदले बिना इस स्थिति को सुधारने के लिए कुछ प्रैक्टिकल सलाह पर गौर करें।

### त्वरित और व्यावहारिक सुझाव
1. **Log4j के साथ MDC (Mapped Diagnostic Context) का लाभ उठाएं**
   - Log4j MDC को सपोर्ट करता है, जो आपको एक थ्रेड के भीतर (और कुछ सावधानी के साथ थ्रेड सीमाओं के पार भी) लॉग्स से जुड़े कॉन्टेक्स्चुअल की-वैल्यू पेयर जोड़ने की अनुमति देता है।
   - एक यूनिक रिक्वेस्ट ID जनरेट करें जब फ्रंटएंड रिक्वेस्ट आपके Spring Boot एप्लिकेशन पर आती है (उदाहरण के लिए, एक UUID), और इसे MDC में स्टोर करें। फिर, इस ID को अपने लॉग पैटर्न में शामिल करें।
   - **कैसे इम्प्लीमेंट करें:**
     - एक Spring Boot फिल्टर या इंटरसेप्टर में (उदाहरण के लिए, `OncePerRequestFilter`), ID जनरेट करें:
       ```java
       import org.slf4j.MDC;
       import javax.servlet.FilterChain;
       import javax.servlet.http.HttpServletRequest;
       import javax.servlet.http.HttpServletResponse;
       import java.util.UUID;

       public class RequestTracingFilter extends OncePerRequestFilter {
           @Override
           protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) {
               try {
                   String traceId = UUID.randomUUID().toString();
                   MDC.put("traceId", traceId);
                   filterChain.doFilter(request, response);
               } finally {
                   MDC.clear(); // रिक्वेस्ट के बाद क्लीन अप
               }
           }
       }
       ```
     - अपने Spring Boot कॉन्फ़िग में फिल्टर रजिस्टर करें:
       ```java
       @Bean
       public FilterRegistrationBean<RequestTracingFilter> tracingFilter() {
           FilterRegistrationBean<RequestTracingFilter> registrationBean = new FilterRegistrationBean<>();
           registrationBean.setFilter(new RequestTracingFilter());
           registrationBean.addUrlPatterns("/*");
           return registrationBean;
       }
       ```
     - अपने Log4j पैटर्न को `log4j.properties` या `log4j.xml` में `traceId` शामिल करने के लिए अपडेट करें:
       ```properties
       log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p %c{1} - %m [traceId=%X{traceId}]%n
       ```
     - अब, उस रिक्वेस्ट से जुड़ी हर लॉग लाइन में `traceId` शामिल होगी, जिससे इसे फ्रंटएंड बटन क्लिक से वापस ट्रेस करना आसान हो जाएगा।

2. **थ्रेड्स के पार ट्रेस ID को प्रोपेगेट करें**
   - यदि आपकी ऐप थ्रेड पूल या एसिंक कॉल्स (उदाहरण के लिए, `@Async`) का उपयोग करती है, तो MDC कॉन्टेक्स्ट स्वचालित रूप से प्रोपेगेट नहीं हो सकता है। इसे हैंडल करने के लिए:
     - एसिंक टास्क्स को एक कस्टम एक्जीक्यूटर के साथ रैप करें जो MDC कॉन्टेक्स्ट को कॉपी करता हो:
       ```java
       import java.util.concurrent.Executor;
       import org.springframework.context.annotation.Bean;
       import org.springframework.context.annotation.Configuration;
       import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

       @Configuration
       public class AsyncConfig {
           @Bean(name = "taskExecutor")
           public Executor taskExecutor() {
               ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
               executor.setCorePoolSize(10);
               executor.setMaxPoolSize(20);
               executor.setQueueCapacity(100);
               executor.setTaskDecorator(task -> {
                   Map<String, String> context = MDC.getCopyOfContextMap();
                   return () -> {
                       try {
                           if (context != null) MDC.setContextMap(context);
                           task.run();
                       } finally {
                           MDC.clear();
                       }
                   };
               });
               executor.initialize();
               return executor;
           }
       }
       ```
     - यह सुनिश्चित करता है कि `traceId` थ्रेड सीमाओं के पार भी रिक्वेस्ट के साथ बनी रहे।

3. **फ्रंटएंड Correlation जोड़ें**
   - यदि संभव हो, तो फ्रंटएंड को एक कस्टम हेडर (उदाहरण के लिए, `X-Request-ID`) एक यूनिक ID के साथ भेजने दें जब बटन क्लिक किया जाता है। आपका बैकएंड अपना खुद का UUID जनरेट करने के बजाय इसे उठा सकता है। यह लॉग को सीधे फ्रंटएंड एक्शन से बिना अतिरिक्त अटकलों के जोड़ देता है।

4. **फॉलबैक: कॉन्टेक्स्चुअल डेटा के साथ लॉगिंग को एन्हांस करें**
   - यदि MDC अभी बहुत अधिक ओवरहेड लगता है, तो मुख्य बिंदुओं पर अधिक कॉन्टेक्स्ट के साथ अपने लॉग्स को समृद्ध करें (उदाहरण के लिए, यूजर ID, सेशन ID, या एंडपॉइंट नाम)। उदाहरण के लिए:
     ```java
     logger.info("Button clicked, endpoint=/api/example, user={}", userId);
     ```
   - इसे `%t` (थ्रेड नाम) और एक टाइट टाइम रेंज के साथ मिलाकर लॉग्स को मैन्युअल रूप से नैरो डाउन करें। यह आदर्श नहीं है लेकिन जरूरत पड़ने पर काम करता है।

### सिर्फ टाइम रेंज क्यों नहीं?
केवल टाइमस्टैम्प पर निर्भर रहना नाजुक है क्योंकि:
- समवर्ती रिक्वेस्ट्स से लॉग ओवरलैप होते हैं, खासकर व्यस्त सिस्टम में।
- टाइम प्रिसिजन (उदाहरण के लिए, मिलीसेकंड) किसी एकल रिक्वेस्ट को अलग करने के लिए पर्याप्त नहीं हो सकती है।
- सर्विसेज या गहरी कॉल स्टैक्स में लॉग्स को सहसंबंधित करना थकाऊ होता है।

### लॉन्ग-टर्म रिकमंडेशन
यदि यह ट्रेसिंग आवश्यकता बढ़ती है, तो Spring Boot के बिल्ट-इन सपोर्ट को अपनाने पर विचार करें जो डिस्ट्रीब्यूटेड ट्रेसिंग के लिए है (उदाहरण के लिए, Sleuth या Micrometer with Zipkin के माध्यम से)। Sleuth स्वचालित रूप से ट्रेस और span ID जनरेट करता है और Log4j के साथ सीमलेसली इंटीग्रेट होता है, लेकिन इसे सेट अप करना अधिक जटिल है। अभी के लिए, MDC एक लाइटवेट, प्रभावी मध्यम मार्ग है।

### अंतिम सलाह
MDC दृष्टिकोण से शुरुआत करें—यह सरल है, Log4j की नेटिव क्षमताओं का लाभ उठाता है, और आपको लॉग्स को फ्रंटएंड-इनिशिएटेड रिक्वेस्ट से जोड़ने का एक स्पष्ट तरीका देता है। आप उस रिक्वेस्ट के लिए हर लॉग लाइन में `[traceId=123e4567-e89b-12d3-a456-426614174000]` जैसा कुछ देखेंगे, जिससे इसे खोजना और ट्रेस करना तुच्छ हो जाएगा। यदि आपको इसे और ट्वीक करने में मदद की आवश्यकता हो तो मुझे बताएं!