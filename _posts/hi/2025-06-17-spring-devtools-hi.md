---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट डेवटूल्स ऑटो रीस्टार्ट के लिए
translated: true
type: note
---

जब आप `mvn spring-boot:run` का उपयोग करके Spring Boot एप्लिकेशन चलाते हैं, तो फाइल वॉचर्स और ऑटो-रिस्टार्ट या हॉट-रीलोड क्षमताएं डिफ़ॉल्ट रूप से सक्षम नहीं होती हैं। हालाँकि, आप उन्हें अपने प्रोजेक्ट में `spring-boot-devtools` डिपेंडेंसी जोड़कर सक्षम कर सकते हैं। यह मॉड्यूल तेज डेवलपमेंट के लिए स्वचालित रीस्टार्ट और LiveReload जैसी सुविधाएँ प्रदान करता है।

### विवरण
1. **DevTools के बिना डिफ़ॉल्ट व्यवहार**:
   - `spring-boot-devtools` के बिना `mvn spring-boot:run` चलाने पर फाइल वॉचर्स या ऑटो-रिस्टार्ट शामिल नहीं होते हैं। Java classes, static resources, या templates में परिवर्तन लागू करने के लिए आपको मैन्युअल रूप से एप्लिकेशन को रोकना और पुनः आरंभ करना होगा।
   - Static resources (जैसे, HTML, CSS, JS) को पूर्ण रीबिल्ड या रीस्टार्ट की आवश्यकता हो सकती है, जब तक कि अन्यथा कॉन्फ़िगर न किया गया हो।

2. **`spring-boot-devtools` के साथ**:
   - **फाइल वॉचर्स**: DevTools Java फाइलों, properties, और कुछ resources (जैसे, `/resources`, `/static`, `/templates`) में परिवर्तनों के लिए classpath की निगरानी करता है।
   - **ऑटो-रिस्टार्ट**: जब classpath पर कोई फाइल बदलती है (जैसे, एक Java class या properties file), DevTools एप्लिकेशन का स्वचालित रूप से पुनरारंभ कर देता है। यह एक कोल्ड स्टार्ट से तेज है क्योंकि यह दो classloaders का उपयोग करता है: एक अपरिवर्तित third-party libraries (base classloader) के लिए और दूसरा आपके एप्लिकेशन कोड (restart classloader) के लिए।[](https://docs.spring.io/spring-boot/reference/using/devtools.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - **LiveReload**: Static resources (जैसे, `/static`, `/public`, या `/templates` में HTML, CSS, JS) या templates (जैसे, Thymeleaf) में परिवर्तन पूर्ण रीस्टार्ट के बजाय ब्राउज़र रिफ्रेश को ट्रिगर करते हैं, बशर्ते आपके पास एक LiveReload ब्राउज़र एक्सटेंशन इंस्टॉल हो (Chrome, Firefox, Safari के लिए समर्थित)।[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)
   - **एक्सक्लूजन**: डिफ़ॉल्ट रूप से, `/META-INF/maven`, `/META-INF/resources`, `/resources`, `/static`, `/public`, और `/templates` में resources रीस्टार्ट को ट्रिगर नहीं करते हैं लेकिन LiveReload को ट्रिगर करते हैं। आप इसे `spring.devtools.restart.exclude` के साथ कस्टमाइज़ कर सकते हैं।[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

3. **DevTools के लिए सेटअप**:
   अपने `pom.xml` में निम्नलिखित डिपेंडेंसी जोड़ें:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
   - `<optional>true</optional>` यह सुनिश्चित करता है कि DevTools प्रोडक्शन बिल्ड्स में शामिल नहीं है।[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)
   - एप्लिकेशन को `mvn spring-boot:run` के साथ चलाएं। DevTools स्वचालित रूप से फाइल देखने और ऑटो-रिस्टार्ट को सक्षम कर देगा।

4. **IDEs में व्यवहार**:
   - **Eclipse**: परिवर्तनों को सहेजने (Ctrl+S) से स्वचालित रूप से बिल्ड ट्रिगर होता है, जिसे DevTools डिटेक्ट करता है और एप्लिकेशन को रीस्टार्ट कर देता है।[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)
   - **IntelliJ IDEA**: DevTools को परिवर्तनों का पता लगाने के लिए आपको मैन्युअल रूप से एक बिल्ड ट्रिगर करना होगा (Ctrl+F9 या "Make Project"), जब तक कि आप ऑटो-बिल्ड कॉन्फ़िगर नहीं करते। वैकल्पिक रूप से, सीमलेस रीस्टार्ट के लिए IntelliJ सेटिंग्स में "Build project automatically" सक्षम करें।[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-restart-and-live-reload-in-intellij-idea)
   - LiveReload के लिए, http://livereload.com/extensions/ से ब्राउज़र एक्सटेंशन इंस्टॉल करें और इसे सक्षम करें।[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)

5. **विकल्प: Spring Loaded**:
   - DevTools के बजाय, आप अधिक उन्नत हॉट-स्वैपिंग (जैसे, method signature परिवर्तन) के लिए Spring Loaded का उपयोग कर सकते हैं। इसे `spring-boot-maven-plugin` में जोड़ें:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <dependencies>
             <dependency>
                 <groupId>org.springframework</groupId>
                 <artifactId>springloaded</artifactId>
                 <version>1.2.8.RELEASE</version>
             </dependency>
         </dependencies>
     </plugin>
     ```
   - Spring Loaded की सिफारिश DevTools से कम की जाती है, क्योंकि इसका रखरखाव उतना सक्रिय नहीं है और यह सभी फ्रेमवर्क्स का समर्थन नहीं कर सकता है।[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/howto-hotswapping.html)

6. **Static Resources का हॉट-रीलोडिंग**:
   - DevTools के बिना, आप `spring-boot-maven-plugin` की `addResources` property सेट करके static resources की हॉट-रीलोडिंग सक्षम कर सकते हैं:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <addResources>true</addResources>
         </configuration>
     </plugin>
     ```
   - यह `src/main/resources` को classpath में जोड़ता है, जिससे static files का इन-प्लेस एडिटिंग संभव होता है, लेकिन यह DevTools की तुलना में कम व्यापक है।[](https://docs.spring.io/spring-boot/maven-plugin/run.html)

7. **चेतावनियाँ**:
   - DevTools मल्टी-मॉड्यूल प्रोजेक्ट्स में classloading समस्याएं पैदा कर सकता है। यदि ऐसा होता है, तो `spring.devtools.restart.enabled=false` के साथ रीस्टार्ट अक्षम करने का प्रयास करें या उन्नत रीलोडिंग के लिए JRebel का उपयोग करें।[](https://docs.spring.io/spring-boot/reference/using/devtools.html)
   - गैर-क्लासपाथ फाइलों के लिए, अतिरिक्त निर्देशिकाओं की निगरानी करने के लिए `spring.devtools.restart.additional-paths` का उपयोग करें।[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - LiveReload के लिए एक ब्राउज़र एक्सटेंशन की आवश्यकता होती है और यह सभी फ्रंट-एंड सेटअप (जैसे, Webpack के साथ React) के लिए काम नहीं कर सकता है।[](https://stackoverflow.com/questions/49888724/hot-reload-for-spring-boot-backend-frontend)
   - यदि रीस्टार्ट धीमे हैं, तो फाइल देखने को अनुकूलित करने के लिए `spring.devtools.restart.poll-interval` और `spring.devtools.restart.quiet-period` को समायोजित करें।[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

### एक सरल ऐप के लिए कदम
1. एक बुनियादी Spring Boot ऐप बनाएं (जैसे, `spring-boot-starter-web` के साथ Spring Initializr का उपयोग करके)।
2. `pom.xml` में `spring-boot-devtools` डिपेंडेंसी जोड़ें।
3. `mvn spring-boot:run` चलाएं।
4. एक Java फाइल, properties फाइल, या static resource (जैसे, `src/main/resources/static` में HTML) संशोधित करें।
5. ऑटो-रिस्टार्ट (Java/properties के लिए) या ब्राउज़र रिफ्रेश (static resources के लिए LiveReload सक्षम होने पर) देखें।

### उदाहरण
एक REST controller के साथ एक सरल ऐप के लिए:
```java
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```
- DevTools जोड़ें, `mvn spring-boot:run` चलाएं, और `hello()` method का return value बदलें। ऐप स्वचालित रूप से पुनरारंभ हो जाएगा।
- `src/main/resources/static` में एक `index.html` जोड़ें, LiveReload एक्सटेंशन इंस्टॉल करें, और HTML संशोधित करें। ब्राउज़र बिना रीस्टार्ट के रिफ्रेश हो जाएगा।

### निष्कर्ष
एक सरल Spring Boot ऐप के लिए, फाइल वॉचर्स, ऑटो-रिस्टार्ट और हॉट-रीलोडिंग को सक्षम करने का सबसे आसान तरीका `spring-boot-devtools` जोड़ना है। एक सीमलेस डेवलपमेंट अनुभव के लिए DevTools के साथ `mvn spring-boot:run` का उपयोग करें। यदि आपको अधिक उन्नत हॉट-स्वैपिंग की आवश्यकता है, तो Spring Loaded या JRebel पर विचार करें, लेकिन अधिकांश मामलों के लिए DevTools पर्याप्त है।[](https://www.geeksforgeeks.org/hot-reload-with-spring-boot-devtools/)[](https://docs.spring.io/spring-boot/how-to/hotswapping.html)

---

नीचे आपके Spring Boot एप्लिकेशन में फाइल देखने, ऑटो-रिस्टार्ट और हॉट-रीलोडिंग के लिए `spring-boot-devtools` को कॉन्फ़िगर करने का एक उदाहरण दिया गया है, जो एक `application.yml` फाइल का उपयोग करता है। यह कॉन्फ़िगरेशन आपके `blog-server` प्रोजेक्ट के लिए तैयार किया गया है, जो आपके प्रदान किए गए लॉग्स पर आधारित है, जो दर्शाते हैं कि DevTools सक्रिय है और `target/classes` की निगरानी कर रहा है।

### `application.yml` कॉन्फ़िगरेशन
```yaml
spring:
  devtools:
    restart:
      # Enable auto-restart (default: true)
      enabled: true
      # Additional directories to monitor for restarts (e.g., custom config folder)
      additional-paths:
        - /home/lzw/Projects/blog-server/config
      # Files/directories to exclude from triggering restarts (default exclusions kept)
      exclude: static/**,public/**,templates/**,logs/**,generated/**
      # Poll interval for file changes (in milliseconds, default: 1000)
      poll-interval: 1000
      # Quiet period after file changes before restarting (in milliseconds, default: 400)
      quiet-period: 400
      # Optional: File to manually trigger restarts
      trigger-file: .restart
    livereload:
      # Enable LiveReload for browser refresh on static resource changes (default: true)
      enabled: true
```

### सेटिंग्स की व्याख्या
- **`spring.devtools.restart.enabled`**: क्लासपाथ फाइलों में परिवर्तन होने पर ऑटो-रिस्टार्ट सक्षम करता है (जैसे, `target/classes`, जैसा कि आपके लॉग में देखा गया: `file:/home/lzw/Projects/blog-server/target/classes/`)।
- **`spring.devtools.restart.additional-paths`**: रीस्टार्ट को ट्रिगर करने के लिए परिवर्तनों के लिए अतिरिक्त निर्देशिकाओं (जैसे, `/home/lzw/Projects/blog-server/config`) की निगरानी करता है।
- **`spring.devtools.restart.exclude`**: `static/`, `public/`, `templates/`, `logs/`, या `generated/` निर्देशिकाओं में परिवर्तनों के लिए रीस्टार्ट को रोकता है, जबकि static resources (जैसे, HTML, CSS, JS) के लिए LiveReload की अनुमति देता है।
- **`spring.devtools.restart.poll-interval`**: सेट करता है कि DevTools फाइल परिवर्तनों की जांच कितनी बार करता है (1000ms = 1 सेकंड)।
- **`spring.devtools.restart.quiet-period`**: रीस्टार्ट करने से पहले यह सुनिश्चित करने के लिए कि कोई और परिवर्तन लंबित नहीं है, परिवर्तन का पता लगाने के बाद 400ms प्रतीक्षा करता है।
- **`spring.devtools.restart.trigger-file`**: `.restart` को अपडेट करके मैन्युअल रीस्टार्ट की अनुमति देता है (जैसे, `touch /home/lzw/Projects/blog-server/.restart`)।
- **`spring.devtools.livereload.enabled`**: LiveReload सर्वर को सक्षम करता है, जो `static/` या `templates/` में परिवर्तनों के लिए ब्राउज़र रिफ्रेश को ट्रिगर करता है (इसके लिए LiveReload ब्राउज़र एक्सटेंशन की आवश्यकता होती है)।

### लागू करने के चरण
1. उपरोक्त कॉन्फ़िगरेशन के साथ `src/main/resources/application.yml` बनाएं या अपडेट करें।
2. सुनिश्चित करें कि `spring-boot-devtools` आपके `pom.xml` में है:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
3. `mvn spring-boot:run` चलाएं। DevTools `target/classes` और `/home/lzw/Projects/blog-server/config` (यदि जोड़ा गया है) की निगरानी करेगा, Java या properties फाइल परिवर्तनों पर ऐप को रीस्टार्ट करेगा और static resource परिवर्तनों पर ब्राउज़र को रिफ्रेश करेगा।
4. LiveReload के लिए, एक ब्राउज़र एक्सटेंशन इंस्टॉल करें (जैसे, http://livereload.com/extensions/ से) या अपने फ्रंट-एंड में एक LiveReload क्लाइंट इंटीग्रेट करें।

### नोट्स
- आपके लॉग एक तेज स्टार्टअप (0.8 सेकंड) दिखाते हैं, इसलिए डिफ़ॉल्ट `poll-interval` और `quiet-period` ठीक होने चाहिए। यदि एक बड़े प्रोजेक्ट में रीस्टार्ट सुस्त लगते हैं तो उन्हें समायोजित करें (जैसे, `poll-interval: 500`)।
- यदि आपको LiveReload की आवश्यकता नहीं है (जैसे, एक अलग फ्रंट-एंड डेव सर्वर का उपयोग करते हुए), `livereload.enabled: false` सेट करें।
- मैन्युअल रीस्टार्ट के लिए, अपने प्रोजेक्ट रूट में `.restart` बनाएं और आवश्यकता पड़ने पर इसे अपडेट करें।

यह YAML कॉन्फ़िगरेशन आपके सेटअप के साथ सीमलेस रूप से काम करना चाहिए, जिससे फाइल-वॉचिंग और ऑटो-रिस्टार्ट सुविधाएँ बढ़ जाएंगी जिन्हें आप पहले से ही देख रहे हैं।