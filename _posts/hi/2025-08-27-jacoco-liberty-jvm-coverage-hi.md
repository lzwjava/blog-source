---
audio: false
generated: true
image: false
lang: hi
layout: post
title: लिबर्टी जेवीएम कवरेज के लिए जाकोको
translated: true
type: note
---

आप यह कर सकते हैं—JaCoCo को उस **Liberty JVM** से जोड़ें जो आपका EAR चलाती है। मुख्य बात यह है: JaCoCo को Liberty के साथ ही उसी JVM के अंदर होना चाहिए, न कि आपके Python रनर में।

यहां विश्वसनीय सेटअप दिए गए हैं (एक चुनें)।

---

## 1) सरल और मजबूत: JVM से निकलने पर फ़ाइल में लिखें

**कब उपयोग करें:** आप परीक्षणों के बाद Liberty सर्वर को रोक सकते हैं।

1. **एजेंट जार उपलब्ध कराएँ** (आपके बिल्ड में एक बार)

```xml
<!-- jacoco एजेंट को target/jacoco/jacocoagent.jar में कॉपी करें -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-dependency-plugin</artifactId>
  <version>3.6.1</version>
  <executions>
    <execution>
      <id>copy-jacoco-agent</id>
      <phase>prepare-package</phase>
      <goals><goal>copy</goal></goals>
      <configuration>
        <artifactItems>
          <artifactItem>
            <groupId>org.jacoco</groupId>
            <artifactId>org.jacoco.agent</artifactId>
            <version>0.8.12</version>
            <classifier>runtime</classifier>
            <destFileName>jacocoagent.jar</destFileName>
          </artifactItem>
        </artifactItems>
        <outputDirectory>${project.build.directory}/jacoco</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

2. **एक Liberty JVM विकल्प जोड़ें** (फ़ाइल: `wlp/usr/servers/<serverName>/jvm.options`)

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=file,append=false,includes=com.myco.*,excludes=org.slf4j.*,destfile=${server.output.dir}/jacoco/jacoco-it.exec
```

* `jacocoagent.jar` को `wlp/usr/servers/<serverName>/jacoco/` में रखें (या कोई भी पठनीय पथ)।
* अपने पैकेजों के अनुसार `includes`/`excludes` को समायोजित करें।

3. **रन फ्लो**

* Liberty शुरू करें (`server start <serverName>`), EAR डिप्लॉय करें।
* अपना Python `unittest` चलाएँ (वे एंडपॉइंट्स को हिट करते हैं)।
* Liberty रोकें (`server stop <serverName>`)।
  → एजेंट `${server.output.dir}/jacoco/jacoco-it.exec` लिखता है।

4. **रिपोर्ट जनरेट करें**

* यदि आपकी परियोजना मल्टी-मॉड्यूल (EAR + EJB + WAR) है, तो एक एग्रीगेटर pom और `report-aggregate` का उपयोग करें:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-aggregate</goal></goals>
      <configuration>
        <dataFile>${env.SERVER_OUTPUT_DIR}/jacoco/jacoco-it.exec</dataFile>
        <includes>
          <include>com/myco/**</include>
        </includes>
      </configuration>
    </execution>
  </executions>
</plugin>
```

(या `jacococli` का उपयोग करें:)

```bash
java -jar jacococli.jar report /path/to/jacoco-it.exec \
  --classfiles module1/target/classes --classfiles module2/target/classes \
  --sourcefiles module1/src/main/java --sourcefiles module2/src/main/java \
  --html target/jacoco-it-report
```

---

## 2) Liberty को रोके बिना लाइव डंप (TCP सर्वर मोड)

**कब उपयोग करें:** आप Liberty को चालू रखना चाहते हैं और आवश्यकतानुसार कवरेज प्राप्त करना चाहते हैं।

1. `jvm.options`:

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=tcpserver,address=*,port=6300,append=false,includes=com.myco.*
```

2. Liberty चलाएँ, Python टेस्ट एक्ज़िक्यूट करें, फिर **डंप** करें:

```bash
# TCP के माध्यम से कवरेज प्राप्त करता है और स्थानीय रूप से एक .exec लिखता है
java -jar jacococli.jar dump --address 127.0.0.1 --port 6300 --destfile jacoco-it.exec --reset
```

अब रिपोर्ट उपरोक्तानुसार जनरेट करें।
टिप: `--reset` काउंटर्स को रीसेट कर देता है ताकि आप लंबे रन के दौरान कई स्नैपशॉट ले सकें।

---

## 3) कंटेनर्स / CI (env-शैली)

* यदि आप Liberty को Docker/K8s में चलाते हैं, तो एजेंट को माउंट करें और सेट करें:

  * `jvm.options` उपरोक्तानुसार, **या**
  * `WLP_JAVA_OPTIONS` / `JAVA_TOOL_OPTIONS` env जिसमें वही `-javaagent=...` हो।
* कई Liberty JVM वाले क्लस्टर्स के लिए, प्रत्येक को एक अलग TCP पोर्ट या फ़ाइल पथ दें, फिर **मर्ज** करें:

```bash
java -jar jacococli.jar merge node1.exec node2.exec --destfile merged.exec
```

---

## नोट्स और सावधानियाँ

* **EAR लेआउट** JaCoCo के लिए मायने नहीं रखता; यह मेमोरी में बाइटकोड को इंस्ट्रूमेंट करता है। रिपोर्टिंग को केवल आपके मॉड्यूल्स (`target/classes`) से **मूल क्लास फ़ाइलों** और सुंदर HTML के लिए उनके स्रोतों की आवश्यकता होती है।
* Java 17/21 संगतता के लिए **हाल का JaCoCo (0.8.12+)** उपयोग करें (Liberty अक्सर OpenJ9/HotSpot पर चलती है—दोनों ठीक हैं)।
* तीसरे पक्ष की लाइब्रेरीज़ को गिनने से बचने के लिए `includes/excludes` पर ध्यान दें।
* यदि `.exec` खाली है, तो संभवतः आपने:

  * एजेंट को अटैच करना भूल गए हैं,
  * अपने पैकेजों को फ़िल्टर कर दिया है,
  * या कोड पर ट्रैफ़िक हिट होने से पहले डंप खींच लिया है।

---

यदि आप अपने EAR के मॉड्यूल लेआउट (EJB/WAR मॉड्यूल और पैकेज रूट्स) साझा करते हैं, तो मैं एक सटीक `report-aggregate` कॉन्फ़िग और एक छोटी सी स्क्रिप्ट दे सकता हूं जो: Liberty शुरू करे → Python टेस्ट चलाए → डंप प्राप्त करे → HTML रिपोर्ट बनाए, सब एक ही बार में।