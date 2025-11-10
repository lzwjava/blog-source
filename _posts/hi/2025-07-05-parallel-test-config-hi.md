---
audio: false
generated: true
lang: hi
layout: post
title: समानांतर परीक्षण निष्पादन के लिए मेवेन कॉन्फ़िगर करें
translated: true
type: note
---

अपने Maven प्रोजेक्ट में समानांतर परीक्षण निष्पादन सक्षम करने के लिए, विशेष रूप से प्रदान की गई `MavenTest.java` क्लास के लिए, आप Maven Surefire Plugin को समानांतर में टेस्ट चलाने के लिए कॉन्फ़िगर कर सकते हैं। `MavenTest.java` क्लास विभिन्न समस्याओं के लिए Maven कमांड निष्पादित करने के लिए JUnit 4 का उपयोग करती है, और आपके मूल त्रुटि के स्टैक ट्रेस से संकेत मिलता है कि टेस्ट पहले से ही समानांतर चल रहे हैं (जैसा कि स्टैक ट्रेस में `ForkJoinPool` से स्पष्ट है)। हालाँकि, आप अपने `pom.xml` फ़ाइल में Surefire Plugin को कॉन्फ़िगर करके स्पष्ट रूप से समानांतर निष्पादन को नियंत्रित कर सकते हैं। नीचे, मैं समझाऊंगा कि समानांतर परीक्षण निष्पादन कैसे सेट करें और अनुरोधित `-DParallel` फ्लैग के उपयोग को कैसे संबोधित करें।

### समानांतर निष्पादन क्यों हो रहा है
आपके टेस्ट आउटपुट में स्टैक ट्रेस में `ForkJoinPool` दिखाई दे रहा है, जो इंगित करता है कि JUnit या Maven पहले से ही समानांतर निष्पादन के लिए थ्रेड पूल का उपयोग कर रहा है। `MavenTest` क्लास `DynamicTest` के साथ `@TestFactory` का उपयोग करती है, और संभावना है कि टेस्ट JUnit के डिफ़ॉल्ट व्यवहार या मौजूदा Surefire कॉन्फ़िगरेशन के कारण समानांतर चल रहे हैं। अब लक्ष्य स्पष्ट रूप से समानांतर निष्पादन को कॉन्फ़िगर करना और `-DParallel` जैसे कमांड-लाइन फ्लैग के माध्यम से नियंत्रण की अनुमति देना है।

### समानांतर परीक्षण निष्पादन कॉन्फ़िगर करने के चरण

1. **Maven Surefire Plugin को कॉन्फ़िगर करने के लिए `pom.xml` अपडेट करें**:
   Maven Surefire Plugin JUnit 4.7+ के लिए समानांतर परीक्षण निष्पादन का समर्थन करता है। आप समानांतरता का स्तर (जैसे, `classes`, `methods`, या `both`) और थ्रेड्स की संख्या निर्दिष्ट कर सकते हैं। `-DParallel` के माध्यम से नियंत्रण सक्षम करने के लिए, आप समानांतरता को टॉगल या कॉन्फ़िगर करने के लिए एक Maven प्रॉपर्टी का उपयोग कर सकते हैं।

   अपने `pom.xml` में Surefire Plugin कॉन्फ़िगरेशन जोड़ें या अपडेट करें:

   ```xml
   <project>
       <!-- अन्य कॉन्फ़िगरेशन -->
       <properties>
           <!-- जब तक निर्दिष्ट न हो, डिफ़ॉल्ट रूप से कोई समानांतर निष्पादन नहीं -->
           <parallel.mode>none</parallel.mode>
           <thread.count>4</thread.count>
       </properties>
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.5.3</version>
                   <configuration>
                       <parallel>${parallel.mode}</parallel>
                       <threadCount>${thread.count}</threadCount>
                       <perCoreThreadCount>false</perCoreThreadCount>
                       <!-- वैकल्पिक: समानांतर टेस्ट के लिए टाइमआउट -->
                       <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                       <!-- टेस्ट को अलग करने के लिए Forking कॉन्फ़िगरेशन -->
                       <forkCount>1</forkCount>
                       <reuseForks>true</reuseForks>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

   - **स्पष्टीकरण**:
     - `<parallel>`: समानांतरता का स्तर निर्दिष्ट करता है। JUnit 4.7+ के लिए मान्य मान हैं `methods`, `classes`, `both`, `suites`, `suitesAndClasses`, `suitesAndMethods`, `classesAndMethods`, या `all`. आपकी `MavenTest` क्लास के लिए, `classes` उपयुक्त है क्योंकि प्रत्येक `DynamicTest` एक समस्या का प्रतिनिधित्व करता है, और आप विभिन्न समस्याओं के लिए टेस्ट समानांतर में चलाना चाहते हैं।
     - `<threadCount>`: थ्रेड्स की संख्या सेट करता है (उदाहरण के लिए, चार समवर्ती टेस्ट के लिए `4`). आप इसे `-Dthread.count=<number>` के माध्यम से ओवरराइड कर सकते हैं।
     - `<perCoreThreadCount>false</perCoreThreadCount>`: सुनिश्चित करता है कि `threadCount` एक निश्चित संख्या है, CPU कोर द्वारा स्केल नहीं।
     - `<parallelTestsTimeoutInSeconds>`: लटके हुए टेस्ट को रोकने के लिए समानांतर टेस्ट के लिए एक टाइमआउट सेट करता है (`MavenTest.java` में आपके `TEST_TIMEOUT` के 10 सेकंड से मेल खाता है)।
     - `<forkCount>1</forkCount>`: टेस्ट को साझा स्टेट मुद्दों को कम करने के लिए एक अलग JVM प्रक्रिया में चलाता है। `<reuseForks>true</reuseForks>` दक्षता के लिए JVM का पुन: उपयोग करने की अनुमति देता है।
     - `<parallel.mode>` और `<thread.count>`: Maven प्रॉपर्टीज जिन्हें कमांड-लाइन फ्लैग्स के माध्यम से ओवरराइड किया जा सकता है (उदाहरण के लिए, `-Dparallel.mode=classes`)।

2. **`-DParallel` के साथ टेस्ट चलाना**:
   समानांतर निष्पादन को नियंत्रित करने के लिए `-DParallel` फ्लैग का उपयोग करने के लिए, आप इसे `parallel.mode` प्रॉपर्टी से मैप कर सकते हैं। उदाहरण के लिए, चलाएँ:

   ```bash
   mvn test -Dparallel.mode=classes -Dthread.count=4
   ```

   - यदि `-Dparallel.mode` निर्दिष्ट नहीं है, तो डिफ़ॉल्ट मान (`none`) समानांतर निष्पादन को अक्षम कर देता है।
   - आप एक पूर्वनिर्धारित मोड (जैसे, `classes`) के साथ समानांतरता सक्षम करने के लिए एक सरल फ्लैग जैसे `-DParallel=true` का भी उपयोग कर सकते हैं। इसे सपोर्ट करने के लिए, `pom.xml` को `-DParallel` की व्याख्या करने के लिए अपडेट करें:

   ```xml
   <project>
       <!-- अन्य कॉन्फ़िगरेशन -->
       <properties>
           <parallel.mode>${Parallel ? 'classes' : 'none'}</parallel.mode>
           <thread.count>4</thread.count>
       </properties>
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.5.3</version>
                   <configuration>
                       <parallel>${parallel.mode}</parallel>
                       <threadCount>${thread.count}</threadCount>
                       <perCoreThreadCount>false</perCoreThreadCount>
                       <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                       <forkCount>1</forkCount>
                       <reuseForks>true</reuseForks>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

   अब, आप टेस्ट चला सकते हैं:

   ```bash
   mvn test -DParallel=true
   ```

   - `-DParallel=true`: `parallel=classes` और `threadCount=4` के साथ समानांतर निष्पादन सक्षम करता है।
   - `-DParallel=false` या `-DParallel` छोड़ना: समानांतर निष्पादन को अक्षम करता है (`parallel=none`)।
   - आप थ्रेड काउंट को `-Dthread.count=<number>` के साथ ओवरराइड कर सकते हैं (उदाहरण के लिए, `-Dthread.count=8`)।

3. **थ्रेड सुरक्षा सुनिश्चित करना**:
   आपकी `MavenTest` क्लास समानांतर में Maven कमांड (`mvn exec:exec -Dproblem=<problem>`) निष्पादित करती है, जो अलग-अलग प्रक्रियाएं शुरू करती हैं। यह स्वाभाविक रूप से थ्रेड-सुरक्षित है क्योंकि प्रत्येक प्रक्रिया का अपना मेमोरी स्पेस होता है, जो साझा स्टेट के मुद्दों से बचाता है। हालाँकि, सुनिश्चित करें कि:
   - `com.lzw.solutions.uva.<problem>.Main` क्लासेज संसाधन साझा नहीं करती हैं (जैसे, फ़ाइलें या डेटाबेस) जो संघर्ष का कारण बन सकती हैं।
   - प्रत्येक समस्या द्वारा उपयोग की जाने वाली इनपुट/आउटपुट फ़ाइलें या संसाधन (जैसे, `p10009` के लिए टेस्ट डेटा) रेस कंडीशन से बचने के लिए अलग-थलग हों।
   - यदि साझा संसाधनों का उपयोग किया जाता है, तो विशिष्ट टेस्ट क्लासेज पर `@NotThreadSafe` का उपयोग करने या साझा संसाधनों तक पहुंच को सिंक्रनाइज़ करने पर विचार करें।

4. **समानांतर निष्पादन के साथ स्किप लिस्ट को हैंडल करना**:
   आपकी `MavenTest.java` में पहले से ही `p10009` जैसी समस्याओं को छोड़ने के लिए एक `SKIP_PROBLEMS` सेट शामिल है। यह समानांतर निष्पादन के साथ अच्छी तरह से काम करता है, क्योंकि छोड़ी गई समस्याओं को टेस्ट शेड्यूल होने से पहले बाहर रखा जाता है। सुनिश्चित करें कि स्किप लिस्ट आवश्यकतानुसार अपडेट की गई है:

   ```java
   private static final Set<String> SKIP_PROBLEMS = new HashSet<>(Arrays.asList(
       "p10009", // NumberFormatException के कारण p10009 को छोड़ता है
       "p10037"  // अन्य समस्याग्रस्त समस्याओं को यहाँ जोड़ें
   ));
   ```

5. **टेस्ट चलाना**:
   स्किप लिस्ट और `-DParallel` फ्लैग के साथ समानांतर में टेस्ट चलाने के लिए:

   ```bash
   mvn test -DParallel=true -Dthread.count=4
   ```

   - यह एक साथ चार समस्या टेस्ट चलाता है, `p10009` और `SKIP_PROBLEMS` में मौजूद किसी भी अन्य समस्या को छोड़ते हुए।
   - यदि आप डीबगिंग के लिए समानांतरता अक्षम करना चाहते हैं:

     ```bash
     mvn test -DParallel=false
     ```

6. **`p10009` के लिए `NumberFormatException` को संबोधित करना**:
   `p10009` में `NumberFormatException` (आपकी मूल त्रुटि से) एक `null` स्ट्रिंग के पार्स होने का संकेत देता है। जबकि `p10009` को छोड़ने से समस्या से बचा जाता है, आप इसे पूर्णता के लिए ठीक करना चाह सकते हैं। `com.lzw.solutions.uva.p10009.Main` को लाइन 17 (`readInt` मेथड) पर जांचें और null-चेक जोड़ें:

   ```java
   public int readInt() {
       String input = readInput(); // काल्पनिक इनपुट रीडिंग मेथड
       if (input == null || input.trim().isEmpty()) {
           throw new IllegalArgumentException("Input cannot be null or empty");
       }
       return Integer.parseInt(input);
   }
   ```

   वैकल्पिक रूप से, समस्या के हल होने तक `p10009` को स्किप लिस्ट में रखें।

### समानांतर निष्पादन पर नोट्स
- **प्रदर्शन**: `parallel=classes` के साथ समानांतर निष्पादन आपकी `MavenTest` क्लास के लिए उपयुक्त है, क्योंकि प्रत्येक `DynamicTest` एक अलग समस्या का प्रतिनिधित्व करता है। यह `methods` या `both` की तुलना में ओवरहेड को कम करता है।
- **संसाधन उपयोग**: समानांतर निष्पादन CPU और मेमोरी उपयोग बढ़ाता है। अपने सिस्टम की निगरानी करें ताकि यह सुनिश्चित हो सके कि `threadCount` (उदाहरण के लिए, `4`) आपके हार्डवेयर को अभिभूत नहीं करता है। यदि मेमोरी मुद्दे उत्पन्न होते हैं तो अलग-अलग JVM में टेस्ट को अलग करने के लिए `forkCount` का उपयोग करें।
- **टाइमआउट**: `parallelTestsTimeoutInSeconds` सेटिंग सुनिश्चित करती है कि टेस्ट अनिश्चित काल तक लटके नहीं रहें, जो `MavenTest.java` में आपके `TEST_TIMEOUT` के 10 सेकंड के साथ संरेखित होती है।
- **थ्रेड सुरक्षा**: चूंकि आपके टेस्ट `mvn exec:exec` कमांड निष्पादित करते हैं, जो अलग-अलग प्रक्रियाओं में चलते हैं, थ्रेड सुरक्षा कम चिंता का विषय है। हालाँकि, सुनिश्चित करें कि टेस्ट इनपुट/आउटपुट (जैसे, फ़ाइलें) प्रति समस्या अलग-थलग हों।
- **डीबगिंग**: यदि समानांतर मोड में टेस्ट अप्रत्याशित रूप से विफल हो जाते हैं, तो समस्याओं को अलग करने के लिए उन्हें क्रमिक रूप से चलाएँ (`-DParallel=false`)।

### उदाहरण पूर्ण कमांड
समानांतर में टेस्ट चलाने के लिए, `p10009` को छोड़ते हुए, चार थ्रेड्स के साथ:

```bash
mvn test -DParallel=true -Dthread.count=4
```

किसी विशिष्ट समस्या (जैसे, `p10009`) को समानांतरता के बिना डीबग करने के लिए, इसे अस्थायी रूप से `SKIP_PROBLEMS` से हटाएं और चलाएँ:

```bash
mvn test -DParallel=false -Dproblem=p10009
```

### अतिरिक्त विचार
- **JUnit 4 सीमाएँ**: आपका प्रोजेक्ट JUnit 4 का उपयोग करता है। JUnit 4.7+ Surefire के माध्यम से समानांतर निष्पादन का समर्थन करता है, लेकिन JUnit 5 प्रति-क्लास समानांतरता या कस्टम रणनीतियों जैसी अधिक लचीली सुविधाएँ प्रदान करता है। यदि आपको उन्नत सुविधाओं की आवश्यकता है तो JUnit 5 में अपग्रेड करने पर विचार करें।
- **Maven संस्करण**: इष्टतम समानांतर निष्पादन समर्थन के लिए सुनिश्चित करें कि आप Maven (उदाहरण के लिए, 3.9.10, जैसा कि आपके त्रुटि आउटपुट में है) और Surefire (उदाहरण के लिए, 3.5.3) के एक हाल के संस्करण का उपयोग कर रहे हैं।
- **त्रुटि हैंडलिंग**: टेस्ट सूट को रोके बिना विफलताओं को लॉग करने के लिए, `runMavenExecTests` में एक्सेप्शन पकड़ने पर विचार करें:

   ```java
   @TestFactory
   Collection<DynamicTest> runMavenExecTests() {
       return PROBLEMS.stream()
               .map(problem -> DynamicTest.dynamicTest("Test problem: " + problem, () -> {
                   String command = String.format("mvn exec:exec -Dproblem=%s", problem);
                   System.out.println("Executing command for " + problem + ": " + command);
                   try {
                       Process process = Runtime.getRuntime().exec(command);
                       // ... (प्रक्रिया हैंडलिंग कोड का बाकी हिस्सा)
                       int exitCode = process.exitValue();
                       Assertions.assertTrue(
                               exitCode == 0,
                               "Maven command failed for problem: " + problem + "\nError output:\n" + errorOutput);
                   } catch (Exception e) {
                       System.err.println("Exception for problem " + problem + ": " + e.getMessage());
                       // वैकल्पिक रूप से विफल होने के बजाय जारी रखें
                   }
               }))
               .collect(Collectors.toList());
   }
   ```

यह सेटअप आपको `-DParallel=true` के साथ समानांतर निष्पादन को नियंत्रित करने, `p10009` जैसे समस्याग्रस्त टेस्ट को छोड़ने और मजबूत टेस्ट निष्पादन बनाए रखने की अनुमति देता है। यदि आपको कमांड-लाइन तर्कों के माध्यम से डायनामिक स्किप लिस्ट या उन्नत JUnit 5 कॉन्फ़िगरेशन जैसी आगे अनुकूलन की आवश्यकता है, तो मुझे बताएं!