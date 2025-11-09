---
audio: false
date: 2025-09-08
generated: true
image: false
lang: hi
layout: post
title: एकल जेवीएम एकीकरण कवरेज रणनीति
translated: true
type: note
---

आपको Jetty को दो बार चलाने या प्रत्येक मॉड्यूल के लिए अलग JaCoCo `.exec` फ़ाइल बनाने की आवश्यकता नहीं है। आपके WAR को सर्व करने वाले एकल JVM पर लगा एक एजेंट **उस JVM द्वारा लोड की गई सभी कक्षाओं** के लिए कवरेज रिकॉर्ड कर सकता है—जिसमें `PlaygroundUtils` भी शामिल है—**एक साझा exec फ़ाइल** में। फिर प्रत्येक मॉड्यूल उसी exec फ़ाइल की ओर इशारा करके अपनी स्वयं की रिपोर्ट जनरेट कर सकता है। एक बड़े रिएक्टर (10+ मॉड्यूल) के लिए, यह साफ-सुथरा तरीके से स्केल करता है।

नीचे आपके रेपो के लिए एक ठोस, न्यूनतम योजना और ड्रॉप-इन संपादन दिए गए हैं।

---

## रणनीति

1.  **पैरेंट लेवल पर एक एकल, साझा IT exec फ़ाइल का उपयोग करें।**
    Jetty को **एक बार** चलाएं, JaCoCo से इंस्ट्रूमेंटेड, जो `../target/it-coverage/jacoco-it.exec` (एक पैरेंट-स्कोप्ड पथ) में लिखे।
2.  **अपने बाहरी Python टेस्ट एक बार चलाएं।**
    वे डिप्लॉयड ऐप पर हिट करते हैं; एजेंट सभी लोड की गई कक्षाओं (वेब + लाइब्रेरीज़) के लिए हिट रिकॉर्ड करता है।
3.  **प्रति-मॉड्यूल रिपोर्ट जनरेट करें**, प्रत्येक मॉड्यूल साझा `jacoco-it.exec` की ओर इशारा करता है।
    `PlaygroundUtils` को एक रिपोर्ट मिल जाएगी भले ही उसके अपने कोई टेस्ट नहीं हैं—यह साझा exec को अपने स्वयं के `target/classes` पर मैप करता है।
4.  (वैकल्पिक) **पैरेंट पर एक समग्र HTML भी जनरेट करें** `report-aggregate` के साथ, या सिर्फ प्रति-मॉड्यूल रिपोर्ट रखें।

जब आपके पास वास्तव में **कई JVM** (जैसे, कई माइक्रोसर्विसेज) हों, तभी आपको कई exec फ़ाइलों और एक `jacoco:merge` चरण की आवश्यकता होती है। आपके वर्तमान सिंगल JVM (Jetty) बिल्ड के लिए, इसे एक exec तक सीमित रखें।

---

## सटीक संपादन

### 1) पैरेंट `pom.xml` (PlaygroundLib)

साझा गुण जोड़ें ताकि प्रत्येक मॉड्यूल एक ही exec फ़ाइल को रेफरेंस कर सके:

```xml
<properties>
  <!-- ... आपके मौजूदा वर्जन ... -->
  <it.coverage.dir>${project.basedir}/target/it-coverage</it.coverage.dir>
  <jacoco.it.exec>${it.coverage.dir}/jacoco-it.exec</jacoco.it.exec>
  <!-- प्रति-मॉड्यूल IT रिपोर्ट जनरेशन को टॉगल करें -->
  <it.report.skip>false</it.report.skip>
</properties>
```

(वैकल्पिक) यदि आप पैरेंट पर एक एकल **समग्र** HTML चाहते हैं, तो यह एक्जिक्यूशन जोड़ें:

```xml
<build>
  <pluginManagement>
    <!-- अपने मौजूदा ब्लॉक रखें -->
  </pluginManagement>

  <plugins>
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>it-aggregate-report</id>
          <phase>verify</phase>
          <goals>
            <goal>report-aggregate</goal>
          </goals>
          <configuration>
            <!-- Jetty रन द्वारा निर्मित साझा IT exec का उपयोग करें -->
            <dataFile>${jacoco.it.exec}</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

> यदि आपका JaCoCo वर्जन `report-aggregate` पर `<dataFile>` को रिजेक्ट करता है, तो इस वैकल्पिक ब्लॉक को छोड़ दें और नीचे दिए गए प्रति-मॉड्यूल रिपोर्ट्स पर भरोसा करें। आप बाद में `merge` + `report` चलाने के लिए हमेशा एक छोटा "कवरेज" एग्रीगेटर मॉड्यूल जोड़ सकते हैं।

---

### 2) `PlaygroundWeb/pom.xml`

Jetty एजेंट को **पैरेंट-लेवल** exec पथ की ओर इंगित करें और append सक्षम करें:

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.parent.basedir}/target/it-coverage/jacoco-it.exec,append=true,includes=org.lzw.*
        </jvmArgs>
        <httpConnector>
          <port>8080</port>
          <host>127.0.0.1</host>
        </httpConnector>
        <webApp><contextPath>/</contextPath></webApp>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals><goal>stop</goal></goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

अपने `PlaygroundWeb` में `jacoco:report` को **उसी** साझा exec को पढ़ने के लिए अपडेट करें:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
      <configuration>
        <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
        <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

आपका मौजूदा Exec Maven Plugin जो `python -m unittest discover tests -v` चलाता है, परफेक्ट है—इसे यथावत छोड़ दें।

---

### 3) `PlaygroundUtils/pom.xml`

एक **केवल-रिपोर्ट** एक्जिक्यूशन जोड़ें ताकि यह साझा exec को अपने स्वयं के क्लासेस पर मैप कर सके:

```xml
<build>
  <plugins>
    <!-- अपने मौजूदा प्लगइन्स रखें -->

    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>report-it</id>
          <phase>verify</phase>
          <goals><goal>report</goal></goals>
          <configuration>
            <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
            <skip>${it.report.skip}</skip>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

यह मॉड्यूल कभी भी Jetty स्टार्ट नहीं करता या Python नहीं चलाता; यह केवल साझा exec और अपने स्वयं के `target/classes` का उपयोग करता है। यदि टेस्ट्स के दौरान वेब ऐप द्वारा कोई `PlaygroundUtils` क्लासेस उपयोग की जाती हैं, तो वे कवरेज के साथ दिखाई देंगी। यदि उनका उपयोग नहीं किया जाता है, तो वे 0% होंगी—जो कि सही सिग्नल है।

---

## आप इसे कैसे चलाएंगे

रेपो रूट से:

```bash
mvn -pl PlaygroundWeb -am clean verify
```

बिल्ड ऑर्डर दोनों मॉड्यूल को कंपाइल करता है, एजेंट के साथ Jetty को एक बार स्टार्ट करता है, आपके Python टेस्ट चलाता है, Jetty को रोकता है, फिर जनरेट करता है:

*   `PlaygroundWeb/target/site/jacoco-it/index.html`
*   `PlaygroundUtils/target/site/jacoco-it/index.html`
*   वैकल्पिक रूप से, एक समग्र रिपोर्ट पैरेंट के अंतर्गत यदि आपने `report-aggregate` सक्षम किया है।

---

## जब आपके पास 10 मॉड्यूल होंगे

*   यदि सभी 10 **एक ही WAR/JVM** के अंदर आते हैं, तो **सिंगल साझा exec** पैटर्न रखें। प्रत्येक मॉड्यूल एक `report` एक्जिक्यूशन जोड़ता है जो साझा exec की ओर इशारा करता है। आप अभी भी Jetty को एक बार स्टार्ट करते हैं और Python को एक बार चलाते हैं।

*   यदि आपके पास **कई JVM** हैं (जैसे, अलग-अलग सर्विसेज), तो प्रत्येक JVM को अपनी स्वयं की `destfile` दें (जैसे, `it-coverage/serviceA.exec`, `serviceB.exec`), फिर पैरेंट में चलाएं:

  ```xml
  <plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>merge-it</id>
        <phase>post-integration-test</phase>
        <goals><goal>merge</goal></goals>
        <configuration>
          <destFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</destFile>
          <files>
            <file>${project.basedir}/target/it-coverage/serviceA.exec</file>
            <file>${project.basedir}/target/it-coverage/serviceB.exec</file>
            <!-- आवश्यकतानुसार और जोड़ें -->
          </files>
        </configuration>
      </execution>

      <execution>
        <id>aggregate-report</id>
        <phase>verify</phase>
        <goals><goal>report-aggregate</goal></goals>
        <configuration>
          <dataFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</dataFile>
          <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
        </configuration>
      </execution>
    </executions>
  </plugin>
  ```

*   यदि आप शोर सीमित करना चाहते हैं, तो एजेंट लाइन पर `includes=org.lzw.*` (पहले से दिखाया गया है) सेट करें या थर्ड-पार्टी लाइब्रेरीज़ को फ़िल्टर करने के लिए `excludes` जोड़ें।

---

## आपकी वर्तमान समस्या क्यों होती है

*   आप **प्रति-मॉड्यूल exec फ़ाइलें** बना रहे थे, इसलिए आपको प्रत्येक को पॉप्युलेट करने के लिए अलग-अलग एजेंट्स के साथ Jetty को दोबारा चलाने के लिए मजबूर महसूस हुआ। यह अनावश्यक है। एजेंट इसकी परवाह नहीं करता कि कोई क्लास किस मॉड्यूल से "संबंधित" है—यह किसी भी लोड की गई क्लास को रिकॉर्ड करता है। exec को केंद्रीकृत करें और प्रत्येक मॉड्यूल के `report` को उसकी ओर इंगित करें।

---

## त्वरित चेकलिस्ट

*   पैरेंट के अंतर्गत एक **साझा** `${jacoco.it.exec}`।
*   Jetty को **एक बार** `append=true` और `includes=org.lzw.*` के साथ स्टार्ट किया गया।
*   Python टेस्ट **एक बार** चलाए गए।
*   प्रत्येक मॉड्यूल के पास एक `jacoco:report` है जो साझा exec को पढ़ता है।
*   एकल टॉप-लेवल HTML के लिए वैकल्पिक पैरेंट `report-aggregate`।

इससे आपका सेटअप सरल और स्केलेबल दोनों हो जाना चाहिए। यदि आप चाहें, तो मैं इन परिवर्तनों के साथ आपकी वर्तमान POMs के लिए सटीक डिफ्स प्रदान कर सकता हूं।