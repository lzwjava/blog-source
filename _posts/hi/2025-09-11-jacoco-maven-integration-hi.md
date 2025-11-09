---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: जैकोको और मेवेन एकीकरण को समझना
translated: true
type: note
---

ठीक है—यहाँ बताया गया है कि **आपके POM फ़ाइल** में JaCoCo के हिस्से कैसे काम करते हैं, चरण दर चरण, और क्यों।

---

# यह POM जो दो कवरेज स्ट्रीम बनाता है

1. **यूनिट-टेस्ट कवरेज (Surefire पाथ)**

* आप JaCoCo का **`prepare-agent`** बिना किसी विशेष कॉन्फ़िग के बाइंड करते हैं:

  ```xml
  <execution>
    <id>prepare-agent</id>
    <goals><goal>prepare-agent</goal></goals>
  </execution>
  ```

  यह `argLine` प्रॉपर्टी के माध्यम से **Surefire** टेस्ट JVM में `-javaagent:...org.jacoco.agent-<ver>-runtime.jar` इंजेक्ट करता है।
  • डिफ़ॉल्ट **destfile** है `${project.build.directory}/jacoco.exec`।
  • डिफ़ॉल्ट **append** है `true` (JaCoCo एजेंट फ़ाइल पहले से मौजूद होने पर उसमें डेटा जोड़ता है)।
  • प्रभाव: जब आप `test` चरण के दौरान यूनिट टेस्ट (अगर कोई हो) चलाते हैं, तो कवरेज `target/jacoco.exec` में जाता है।

2. **इंटीग्रेशन-टेस्ट कवरेज (Jetty पाथ)**

* आप IT कवरेज के लिए एक **अलग फ़ाइल** डिफ़ाइन करते हैं:

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
  </properties>
  ```
* आप Jetty को **उसके अपने JaCoCo एजेंट** के साथ शुरू करते हैं जो उस फ़ाइल की ओर इशारा करता है:

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
        </jvmArgs>
        ...
      </configuration>
    </execution>
  </plugin>
  ```

  • Jetty एक **अलग JVM** के रूप में चलता है; इसका एजेंट `target/jacoco-it.exec` में लिखता है।
  • क्योंकि `append` निर्दिष्ट नहीं है, JaCoCo का डिफ़ॉल्ट `append=true` लागू होता है—इसलिए एकाधिक Jetty लॉन्च एक ही फ़ाइल में डेटा जोड़ते हैं, जब तक कि आप क्लीन नहीं करते या `append=false` सेट नहीं करते।

---

# लाइफसाइकिल फ़्लो (`mvn verify` पर क्या होता है)

1. **compile**

   * Spotless फॉर्मेट करता है (`spotless-maven-plugin`) और Checkstyle चलता है (`maven-checkstyle-plugin`)।
   * आपका WAR तैयार होता है (`maven-war-plugin`)।

2. **test (Surefire)**

   * अगर आपके पास यूनिट टेस्ट हैं, तो वे **`prepare-agent`** द्वारा इंजेक्ट किए गए argLine के तहत चलते हैं → कवरेज `target/jacoco.exec` में जाता है।

3. **pre-integration-test**

   * Jetty को **डेमन मोड में** शुरू किया जाता है:

     ```xml
     <daemon>true</daemon>
     ```

     Maven तुरंत नियंत्रण वापस पा लेता है; Jetty JaCoCo एजेंट के साथ चलता रहता है, और `jacoco-it.exec` में लिखता रहता है।

4. **integration-test**

   * आपके Python टेस्ट चल रहे ऐप पर हिट करते हैं:

     ```xml
     <plugin>
       <artifactId>exec-maven-plugin</artifactId>
       <execution>
         <id>python-integration-tests</id>
         <phase>integration-test</phase>
         <goals><goal>exec</goal></goals>
         <configuration>
           <executable>python3</executable>
           <workingDirectory>${project.parent.basedir}</workingDirectory>
           <arguments>
             <argument>-m</argument><argument>unittest</argument>
             <argument>discover</argument><argument>tests/</argument>
             <argument>-v</argument>
           </arguments>
         </configuration>
       </execution>
     </plugin>
     ```

     ये टेस्ट Jetty का उपयोग करते हैं, इसलिए कवरेज Jetty JVM के एजेंट के माध्यम से **`target/jacoco-it.exec`** में जमा होता है।

5. **post-integration-test**

   * Jetty को साफ़ तरीके से बंद किया जाता है:

     ```xml
     <execution>
       <id>stop-jetty</id>
       <phase>post-integration-test</phase>
       <goals><goal>stop</goal></goals>
       ...
     </execution>
     ```

6. **verify**

   * आप IT डेटा फ़ाइल और एक कस्टम आउटपुट डायरेक्टरी का उपयोग करके एक **अलग IT रिपोर्ट** जनरेट करते हैं:

     ```xml
     <execution>
       <id>report-it</id>
       <phase>verify</phase>
       <goals><goal>report</goal></goals>
       <configuration>
         <dataFile>${jacoco.it.exec}</dataFile>
         <outputDirectory>${project.reporting.outputDirectory}/jacoco-it
         </outputDirectory>
       </configuration>
     </execution>
     ```
   * परिणाम: HTML `target/site/jacoco-it/index.html` में जाता है जो केवल **इंटीग्रेशन** कवरेज (Jetty से) का सारांश देता है।

> नोट: अगर आप **यूनिट-टेस्ट** रिपोर्ट भी चाहते हैं, तो आप एक और `jacoco:report` एक्ज़िक्यूशन जोड़ सकते हैं जो डिफ़ॉल्ट `target/jacoco.exec` की ओर इशारा करे और आउटपुट `target/site/jacoco` पर दे—यूनिट और IT रिपोर्ट्स को अलग रखते हुए।

---

# `.exec` फ़ाइलों के लिए "नया बनाएं या बदलें?" के बारे में

* **JaCoCo एजेंट का डिफ़ॉल्ट है `append=true`**।

  * **यूनिट टेस्ट्स** के लिए, फ़ाइल `target/jacoco.exec` है। जब आप बार-बार **`clean` के बिना** `mvn verify` चलाते हैं, तो डेटा रन्स के बीच जुड़ सकता है।
  * **Jetty IT** के लिए, आपके `jvmArgs` `append` को ओवरराइड नहीं करते, इसलिए `target/jacoco-it.exec` भी डिफ़ॉल्ट रूप से **जुड़ जाता है**।

**बेस्ट प्रैक्टिस** (पुराने डेटा को मिलाने से बचने के लिए):

* `mvn clean verify` चलाएं, **या** Jetty एजेंट लाइन में `append=false` जोड़ें:

  ```xml
  -javaagent:...org.jacoco.agent-...-runtime.jar=destfile=${jacoco.it.exec},append=false
  ```
* अगर आप कभी जानबूझकर एकाधिक `.exec` फ़ाइलों को मर्ज करना चाहते हैं, तो `jacoco:report` से पहले `jacoco:merge` का उपयोग करें।

---

# आपके ओरिजिनल XML में प्रत्येक प्रासंगिक ब्लॉक क्या कर रहा है (रेफरेंस के अनुसार)

* **IT फ़ाइल लोकेशन**

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
    <it.report.skip>false</it.report.skip>
  </properties>
  ```

  इंटीग्रेशन कवरेज कहाँ स्टोर होगी, यह डिफ़ाइन करता है। `it.report.skip` डिक्लेयर किया गया है लेकिन अभी तक रिपोर्ट एक्ज़िक्यूशन में वायर नहीं किया गया है (नीचे टिप देखें)।

* **यूनिट टेस्ट एजेंट (Surefire पाथ)**

  ```xml
  <plugin>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>prepare-agent</id>
        <goals><goal>prepare-agent</goal></goals>
      </execution>
      ...
    </executions>
  </plugin>
  ```

* **IT के लिए JaCoCo के साथ Jetty**

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <jvmArgs>
      -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
    </jvmArgs>
    ...
  </plugin>
  ```

* **Jetty चलने के दौरान Python इंटीग्रेशन टेस्ट**

  ```xml
  <plugin>
    <artifactId>exec-maven-plugin</artifactId>
    <execution>
      <id>python-integration-tests</id>
      <phase>integration-test</phase>
      <goals><goal>exec</goal></goals>
      ...
    </execution>
  </plugin>
  ```

* **verify पर IT कवरेज रिपोर्ट जनरेट करना**

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

---

# प्रैक्टिकल टिप्स / छोटे सुधार

* **पुराने IT डेटा से बचें**
  Jetty एजेंट में `append=false` जोड़ें (ऊपर दिखाया गया है), या हमेशा `mvn clean verify` चलाएं।

* **अपने `it.report.skip` स्विच को वायर करें**
  अगर आप किसी प्रॉपर्टी के माध्यम से IT रिपोर्ट जनरेट करना स्किप करना चाहते हैं:

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <skip>${it.report.skip}</skip>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

* **यूनिट बनाम IT रिपोर्ट्स को अलग रखें**
  आपने पहले ही IT रिपोर्ट को `site/jacoco-it` पर अलग कर दिया है। अगर आपको यूनिट रिपोर्ट की भी आवश्यकता है, तो एक और `jacoco:report` जोड़ें (बिना `dataFile` ओवरराइड के) जो `site/jacoco` पर लिखे।

* **मल्टी-मॉड्यूल नोट**
  यह मॉड्यूल-लोकल सेटअप केवल **PlaygroundWeb** के लिए कवरेज रिपोर्ट करता है। अगर आप बाद में एक **कंबाइंड** व्यू चाहते हैं, तो `jacoco:merge` (`.exec` फ़ाइलों को कंबाइन करने के लिए) और/या `report-aggregate` का उपयोग करें, जो एक पैरेंट `pom` से हो (जिसका `packaging=pom` हो) (JaCoCo 0.8.8+)।

---

# संक्षेप में

* **यूनिट टेस्ट्स** → `prepare-agent` Surefire JVM में JaCoCo इंजेक्ट करता है → `target/jacoco.exec`।
* **इंटीग्रेशन टेस्ट्स** → Jetty अपने खुद के JaCoCo एजेंट के साथ शुरू होता है → `target/jacoco-it.exec`।
* **रिपोर्ट** → `verify` पर, `jacoco:report` **केवल IT** कवरेज को `target/site/jacoco-it` पर रेंडर करता है।
* **फ़ाइल बिहेवियर** → JaCoCo **डिफ़ॉल्ट रूप से जोड़ता है**; रन्स को मिलाने से बचने के लिए `mvn clean verify` या `append=false` को प्राथमिकता दें।