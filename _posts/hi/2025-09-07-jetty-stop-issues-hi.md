---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hi
layout: post
title: फोर्क्ड जेटी स्टॉप समस्याओं का समाधान
translated: true
type: note
---

आपने वास्तव में ज्यादातर चीजें सही की हैं — हैंग लगभग हमेशा इसलिए होता है क्योंकि **स्टॉप गोल फोर्क किए गए Jetty तक नहीं पहुंच पाती** (गलत stopHost/port/key scope) या क्योंकि **`run-forked` अप्रत्याशित रूप से Maven को अटैच रखता है**। नीचे दो ठोस समाधान हैं; एक चुनें।

### विकल्प A — विश्वसनीय पैटर्न: `jetty:start` (डेमन) + `jetty:stop`

यह `run-forked` को पूरी तरह से टालता है और IT लाइफसाइकिल के लिए सबसे स्थिर है।

**क्या बदलना है**

1.  प्लगइन वर्जन पिन करें और `pre-integration-test` में `start` का `daemon=true` के साथ उपयोग करें।
2.  अपने Python ITs को `integration-test` में रखें।
3.  `post-integration-test` में `stop` का उपयोग करें।
4.  **दोनों** एक्ज़िक्यूशन में *समान* `stopHost/stopPort/stopKey` प्रदान करें।

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <configuration>
    <httpConnector>
      <port>8080</port>
      <host>127.0.0.1</host>
    </httpConnector>
  </configuration>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>start</goal>
      </goals>
      <configuration>
        <daemon>true</daemon>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
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

**यह "अटकने" को कैसे ठीक करता है**

* `daemon=true` `start` को तुरंत Maven को कंट्रोल वापस दे देता है, ताकि आपके ITs चल सकें।
* मेल खाते `stopHost/stopPort/stopKey` गारंटी देते हैं कि `stop` मोजो उसी Jetty तक पहुंचेगा।
* `run-forked` के मॉनिटर थ्रेड बिहेवियर पर कोई निर्भरता नहीं।

---

### विकल्प B — `run-forked` रखें, लेकिन स्टॉप को वास्तव में काम करने दें

यदि आप `run-forked` पसंद करते हैं, तो आम दिक्कतें हैं:

* `stopHost` डिफॉल्ट चाइल्ड बाइंडिंग (IPv6 बनाम IPv4) से अलग हो सकते हैं।
* `stopPort/stopKey` केवल स्टार्ट एक्ज़िक्यूशन पर सेट होते हैं लेकिन स्टॉप एक्ज़िक्यूशन पर **नहीं** दोहराए जाते।
* अगर कॉन्फ़िग गलत जगह है तो चाइल्ड स्टॉप हैंडलर एक्सपोज़ नहीं करता।

**कॉन्फ़िग को इस तरह कस लें:**

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>run-forked</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>

        <httpConnector>
          <host>127.0.0.1</host>
          <port>8080</port>
        </httpConnector>

        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
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

**अतिरिक्त सुरक्षा**

* अगर आपका macOS/Java IPv6 चुनता है और स्टॉप गोल IPv4 का उपयोग करता है, तो चाइल्ड `jvmArgs` में `-Djava.net.preferIPv4Stack=true` जोड़ें:

  ```
  <jvmArgs>
    -Djava.net.preferIPv4Stack=true
    -javaagent:...
  </jvmArgs>
  ```
* सुनिश्चित करें कि `8081` पर और कुछ नहीं चल रहा है। अगर है, तो स्टार्ट+स्टॉप दोनों को किसी दूसरे फ्री पोर्ट पर बदलें।
* अगर आपके ITs क्रैश हो जाते हैं या अटक जाते हैं, तो `post-integration-test` कभी नहीं चल सकता; उस स्थिति में, एक `verify`-फेज किल फॉलबैक जोड़ें (नीचे देखें)।

---

### वैकल्पिक सेफ्टी नेट — अगर `stop` फेल हो तो चाइल्ड को किल करें

एक फाइल में लिखे गए PID द्वारा फोर्क किए गए Jetty को जबरन किल करने के लिए एक छोटा हेल्पर जोड़ें:

1.  `run-forked`/`start` कॉन्फ़िग में:

```
<pidFile>${project.build.directory}/jetty.pid</pidFile>
```

2.  `post-integration-test` के बाद, `verify` में एक `exec-maven-plugin` जोड़ें जो pid फाइल चेक करे और अगर प्रोसेस अभी भी जीवित है तो उसे खत्म कर दे।

---

### आपके लॉग से कुछ छोटे नोट्स

* `No Spring WebApplicationInitializer types detected` सामान्य है अगर आप `web.xml` + DispatcherServlet का उपयोग करते हैं; स्टॉप हैंग से संबंधित नहीं है।
* ITs को **maven-failsafe-plugin** पर ले जाने पर विचार करें (यह `integration-test`/`verify` से बंधता है) और यूनिट टेस्ट्स को surefire पर रखें। आपका वर्तमान `exec-maven-plugin` तरीका काम करता है, लेकिन failsafe IT लाइफसाइकिल के साथ बेहतर एकीकृत करता है।

---

अगर आप चाहें, तो अपना **पूरा** Jetty प्लगइन ब्लॉक + कोई भी `settings.xml` mirrors (लोकल रिपो पाथ के लिए) पेस्ट करें और मैं आपके रिपो के लिए सटीक न्यूनतम डिफ तैयार कर दूंगा।